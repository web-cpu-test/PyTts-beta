class Sound():
    def __init__(self, model):
        self.config = { }
        self.text = [ ]
        self.word = 0
        self.model = numpy.load(model)
        self.config = json.loads(self.model['config.json'].decode())
        self.pause = numpy.zeros(self.config['rate'] * int(self.config['pause']))
        
    def __call__(self, text):
        self.text = self.text + pronounce(text)
        self.word = 0
          
    def __toSound(self, words):
        sound = numpy.empty(0)
        for word in words:
            sound = numpy.append(sound, self.model[word])
        if len(self.text) == self.word+1: return numpy.array(sound, dtype = numpy.int16)
        sound = numpy.array(numpy.append(sound, self.pause), dtype = numpy.int16)
        return sound
           
    def audio(self):
        while not len(self.text) == self.word:
            yield self.__toSound(self.text[self.word])
            self.word = self.word + 1
        self.text = [ ]
        self.word = 0

def __load_modules__(**args):
    for name,module in args.items():
        globals()[name] = module

