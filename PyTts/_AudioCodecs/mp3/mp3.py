class mp3():
    def __init__(self, file_name, rate, *, bit_rate = 64, quality = 4):
        self.encoder = lameenc.Encoder()
        self.encoder.silence()
        self.encoder.set_bit_rate(bit_rate)
        self.encoder.set_in_sample_rate(rate)
        self.encoder.set_channels(1)
        self.encoder.set_quality(quality)
        self.mp3_data = b''
        self.mp3_file = open(file_name, 'wb')

    def write(self, data):
        self.mp3_file.write(self.encoder.encode(data))

    def flush(self):
        self.mp3_file.close()

def __load_modules__(**args):
    for name,module in args.items():
        globals()[name] = module
