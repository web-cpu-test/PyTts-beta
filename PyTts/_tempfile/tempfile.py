class tempfile():
    def __init__(self, mode, name=False):
        try:
            temp_dir = os.environ['TMP']
        except:
            temp_dir = os.environ['TEMP']
        if name:
            self.name = name
        else:
            self.name = 'PyTts-' + ''.join(['abcdefghijklmnopqrstuvwxyz'[int(i)] for i in ''.join([str(x) for x in os.urandom(26)])[:20]]) + '.tmp'
        self.path = temp_dir + os.sep + self.name
        self.__mode = mode
        with open(self.path, 'w'): pass
        self.__file = open(self.path, self.__mode)
        self.file = self.__file
        
    def tmfile(self):
        return self.__file

    def content(self):
        if self.__mode in ['r','rb']:
            content = self.__file.read()
        else:
            self.__file.close()
            self.__file = open(self.path, 'rb')
            content = self.__file.read()
            self.__file.close()
            self.__file = open(self.path, self.__mode)
        return content

    def seek(self, mode = 'r'):
        if mode == 0:
            self.__file.close()
            self.__file = open(self.path, self.__mode)
        elif mode == 1:
            self.__file = open(self.path, self.__mode)
        else:
            self.__file.close()
            self.__file = open(self.path, mode)

    def close(self):
        self.__file.close()
        self.__file = None

    def reopen(self):
        self.__file = open(self.path, self.__mode)

    def remove(self):
        try:
            self.__file.close()
        except:
            pass
        os.remove(self.path)
        self.remove = self.file = self.content = self.seek = self.reopen = self.close = lambda *arg,**args: f'FILE {self.name} WAS REMOVED'

def __load_modules__(**args):
    for name,module in args.items():
        globals()[name] = module
