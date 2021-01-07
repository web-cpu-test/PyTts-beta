class SoundNotFound(Exception):
    pass
class DifferentRates(Exception):
    pass

class Trainer():
    def __init__(self,path,**mcon):
        self.path = path
        self.sep = os.sep
        self.folder = path.split(self.sep)[-1]
        self.config = {**mcon}
        self.sounds = load('sounds')
        no = 0
        self.np_tmf = tempfile('wb')
        err = False
        for sound in self.sounds:
            try:
                open(self.path+self.sep+sound+'.wav','rb')
            except:
                print(sound+'.wav','not exists')
                err = True
                no = no + 1
        if err:
            raise SoundNotFound(f'{no} of 70 sound file not present')

    def __save_name(self):
        return '.'.join([self.folder, 'PyTts'])

    def train(self):
        self.data = {}
        self.rate = []
        for sound in self.sounds:
            rate, data = read(self.path + self.sep + sound + '.wav')
            self.data[sound] = data
            self.rate.append(rate)
        self.rate = list(set(self.rate))
        if len(self.rate) != 1:
            raise DifferentRates('BitRate of files should be equal but different rates are found')
        self.config['rate'] = self.rate[0]
        self.__save()

    def __save(self):
        np.savez(self.np_tmf.tmfile(), **self.data)
        zipf = ZipFile(self.np_tmf.path, 'a')
        json_tmf = tempfile('w')
        read_tmf = tempfile('w')
        read_tmf.tmfile().write(load('msg'))
        read_tmf.close()
        json_tmf.tmfile().write(json.dumps(self.config))
        json_tmf.close()
        zipf.write(json_tmf.path, 'config.json')
        zipf.write(read_tmf.path, '__README__.txt')
        zipf.close()
        with open(self.__save_name(),'wb') as f:
             f.write(self.np_tmf.content())
        self.np_tmf.remove()
        read_tmf.remove()
        json_tmf.remove()
            
def __load_modules__(**args):
    for name,module in args.items():
        globals()[name] = module
