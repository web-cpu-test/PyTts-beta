class wav():
    def __init__(self, file_name, rate, *, sampwidth = 2):
        self.wav_file = wave.open(file_name, "w")
        self.wav_file.setnchannels(1)
        self.wav_file.setsampwidth(sampwidth)
        self.wav_file.setframerate(rate)

    def write(self, data):
        self.wav_file.writeframes(data.tobytes())

    def flush(self):
        self.wav_file.close()

def __load_modules__(**args):
    for name,module in args.items():
        globals()[name] = module