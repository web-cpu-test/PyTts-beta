class Tagger:

    def __init__(self):
        self.weights = data.load('tagger_weights')
        self.tagdict = data.load('tagger_dict')

    def tag(self, tokens):
        prev, prev2 = "-START-","-START2-"
        output = []
        context = ["-START-", "-START2-"] + tokens + ["-END-", "-END2-"]
        for i, word in enumerate(tokens):
            tag = self.tagdict.get(word)
            if not tag:
                features = self._get_features(i, word, context, prev, prev2)
                tag = self.predict(features)
            output.append((word, tag))
            prev2 = prev
            prev = tag
        return output

    def _get_features(self, i, word, context, prev, prev2):
        i += 2
        features = []
        add = features.append
        add("bias")
        add(" ".join(["i suffix",word[-3:]]))
        add(" ".join(["i pref1",word[0]]))
        add(" ".join(["i-1 tag",prev]))
        add(" ".join(["i-2 tag",prev2]))
        add(" ".join(["i tag+i-2 tag",prev, prev2]))
        add(" ".join(["i word",context[i]]))
        add(" ".join(["i-1 tag+i word",prev, context[i]]))
        add(" ".join(["i-1 word",context[i - 1]]))
        add(" ".join(["i-1 suffix",context[i - 1][-3:]]))
        add(" ".join(["i-2 word",context[i - 2]]))
        add(" ".join(["i+1 word",context[i + 1]]))
        add(" ".join(["i+1 suffix",context[i + 1][-3:]]))
        add(" ".join(["i+2 word",context[i + 2]]))
        return features
		
    def predict(self, features):
        scores = {}
        for feat in features:
            if feat not in self.weights:
                continue
            weights = self.weights[feat]
            for label, weight in weights.items():
                try:
                    scores[label] += weight
                except:
                    scores[label] = weight
        best_label = max([i for i in scores], key=lambda label: (scores[label], label))
        return best_label

class tokenizer:
    _REGEXP = r"""(
      (?:
      https?:
        (?:
          /{1,3}
          |
          [a-z0-9%]
                                           
        )
        |
                                           
        [a-z0-9.\-]+[.]
        (?:[a-z]{2,13})
        /
      )
      (?:
        [^\s()<>{}\[\]]+
        |
        \([^\s()]*?\([^\s()]+\)[^\s()]*?\)
        |
        \([^\s]+?\)
      )+
      (?:
        \([^\s()]*?\([^\s()]+\)[^\s()]*?\)
        |
        \([^\s]+?\)
        |
        [^\s`!()\[\]{};:'".,<>?«»“”‘’]
      )
      |
      (?:
            (?<!@)
        [a-z0-9]+
        (?:[.\-][a-z0-9]+)*
        [.]
        (?:[a-z]{2,13})
        \b
        /?
        (?!@)
                                
      )
    |
        (?:
          (?:
            \+?[01]
            [ *\-.\)]*
          )?
          (?:
            [\(]?
            \d{3}
            [ *\-.\)]*
          )?
          \d{3}
          [ *\-.\)]*
          \d{4}
        )|
        (?:
          [<>]?
          [:;=8]
          [\-o\*\']?
          [\)\]\(\[dDpP/\:\}\{@\|\\]
          |
          [\)\]\(\[dDpP/\:\}\{@\|\\]
          [\-o\*\']?
          [:;=8]
          [<>]?
          |
          <3
        )|<[^>\s]+>|[\-]+>|<[\-]+|(?:@[\w_]+)|(?:\#+[\w_]+[\w\'_\-]*[\w_]+)|[\w.+-]+@[\w-]+\.(?:[\w-]\.?)+[\w-]|
        (?:[^\W\d_](?:[^\W\d_]|['\-_])+[^\W\d_])
        |
        (?:[+\-]?\d+[,/.:-]\d+[+\-]?)
        |
        (?:[\w_]+)
        |
        (?:\.(?:\s*\.){1,})
        |
        (?:\S)
        )"""

    def __init__(self):
        self._WORD_RE = regex.compile(self._REGEXP, regex.VERBOSE | regex.I | regex.UNICODE)
        self._HANG_RE = regex.compile(r"([^a-zA-Z0-9])\1{3,}")

    def tokenize(self,text):
        safe_text = self._HANG_RE.sub(r"\1\1\1", text)
        words = self._WORD_RE.findall(safe_text)
        return words

    def __call__(self,text):
        return self.tokenize(text)

def main(cache):
    class G2p():
        def __init__(self):
            self.word_tokenize = tokenizer().tokenize
            self.pos_tag = Tagger().tag
            idx = data.load('g2idx_idx2p')
            self.g2idx, self.idx2p = idx['g2idx'], idx['idx2p']
            self.cmu = data.load('cmu')
            self.homograph2features = data.load('homograph')
            self.variables = data.load('checkpoint')
            self.enc_emb = self.variables["enc_emb"]
            self.enc_w_ih = self.variables["enc_w_ih"]
            self.enc_w_hh = self.variables["enc_w_hh"]
            self.enc_b_ih = self.variables["enc_b_ih"]
            self.enc_b_hh = self.variables["enc_b_hh"]
            self.dec_emb = self.variables["dec_emb"]
            self.dec_w_ih = self.variables["dec_w_ih"]
            self.dec_w_hh = self.variables["dec_w_hh"]
            self.dec_b_ih = self.variables["dec_b_ih"]
            self.dec_b_hh = self.variables["dec_b_hh"]
            self.fc_w = self.variables["fc_w"]
            self.fc_b = self.variables["fc_b"]
        
        def _grucell(self, x, h, w_ih, w_hh, b_ih, b_hh):
            rzn_ih = np.matmul(x, w_ih.T) + b_ih
            rzn_hh = np.matmul(h, w_hh.T) + b_hh
            rz_ih, n_ih = rzn_ih[:, :rzn_ih.shape[-1] * 2 // 3], rzn_ih[:, rzn_ih.shape[-1] * 2 // 3:]
            rz_hh, n_hh = rzn_hh[:, :rzn_hh.shape[-1] * 2 // 3], rzn_hh[:, rzn_hh.shape[-1] * 2 // 3:]
            rz = 1 / (1 + np.exp(-(rz_ih + rz_hh)))
            r, z = np.split(rz, 2, -1)
            n = np.tanh(n_ih + r * n_hh)
            h = (1 - z) * n + z * h
            return h

        def _gru(self, x, steps, w_ih, w_hh, b_ih, b_hh, h0=None):
            if h0 is None:
                h0 = np.zeros((x.shape[0], w_hh.shape[1]), np.float32)
            h = h0
            outputs = np.zeros((x.shape[0], steps, w_hh.shape[1]), np.float32)
            for t in range(steps):
                h = self._grucell(x[:, t, :], h, w_ih, w_hh, b_ih, b_hh)
                outputs[:, t, ::] = h
            return outputs

        def _encode(self, word):
            chars = list(word) + ["</s>"]
            x = [self.g2idx.get(char, self.g2idx["<unk>"]) for char in chars]
            x = np.take(self.enc_emb, np.expand_dims(x, 0), axis=0)
            return x

        @cache(maxsize=500)
        def _predict(self, word):
            enc = self._encode(word)
            enc = self._gru(enc, len(word) + 1, self.enc_w_ih, self.enc_w_hh,self.enc_b_ih, self.enc_b_hh, h0=np.zeros((1, self.enc_w_hh.shape[-1]), np.float32))
            last_hidden = enc[:, -1, :]
            dec = np.take(self.dec_emb, [2], axis=0)
            h = last_hidden
            preds = []
            for i in range(20):
                h = self._grucell(dec, h, self.dec_w_ih, self.dec_w_hh, self.dec_b_ih, self.dec_b_hh)
                logits = np.matmul(h, self.fc_w.T) + self.fc_b
                pred = logits.argmax()
                if pred == 3: break
                preds.append(pred)
                dec = np.take(self.dec_emb, [pred], axis=0)
            preds = [self.idx2p.get(str(idx), "<unk>") for idx in preds]
            return preds

        @cache(maxsize=500)
        def pronounce(self, text):
            words = self.word_tokenize(text)
            tokens = self.pos_tag(words)
            prons = []
            for word, pos in tokens:
                if not word.isalpha():
                    pron = [word]
                elif word in self.homograph2features:
                    pron1, pron2, pos1 = self.homograph2features[word]
                    if pos.startswith(pos1):
                        pron = pron1
                    else:
                        pron = pron2
                elif word in self.cmu:
                    pron = self.cmu[word][0]
                else:
                    pron = self._predict(word)
                prons.append(pron)
            return prons
    return G2p()

def __load_modules__(**args):
    for name,module in args.items():
        globals()[name] = module
