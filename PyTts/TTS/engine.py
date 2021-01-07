from .SoundObj import Sound

class FormatNotSupported(Exception): pass

class TTS():
    def __init__(self, model):
        self.obj = Sound(model)
        self.config = self.obj.config
        self.audio_mixer = mixer
        self.audio_mixer.init(frequency=self.config['rate'], size=-16, channels=1)

    def load(self, text):
        self.obj(text)
    
    def export(self, file_name, encoding = None):
        if encoding == None:
            encoding = file_name.split('.')[-1]
            if encoding not in ['wav', 'mp3']:
                raise FormatNotSupported(f'{format} sound format is not supported')
        else:
            if encoding not in ['wav', 'mp3']:
                raise FormatNotSupported(f'{format} sound format is not supported')
        if encoding == 'wav': encoder = audio_enc.wav.wav.wav(file_name, self.config['rate'])
        if encoding == 'mp3': encoder = audio_enc.mp3.mp3.mp3(file_name, self.config['rate'])
        for chunk in self.obj.audio():
            encoder.write(chunk)
        encoder.flush()

    def play(self, volume = 1.0):
        if volume != self.audio_mixer.get_volume() : self.audio_mixer.set_volume(volume)
        for chunk in self.obj.audio():
            snd = self.audio_mixer.Sound(array=chunk)
            snd.play()
            while self.audio_mixer.get_busy(): pass

def __load_modules__(**args):
    for name,module in args.items():
        globals()[name] = module
        





























