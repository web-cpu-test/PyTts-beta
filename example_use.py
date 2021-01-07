from PyTts.TTS import engine

path_to_model = 'C:\\fake\\path\\to\\model\\MYModel'

tts = engine.TTS(path_to_model) #Define The tts model

tts.load('this is going to be spoken') # load text to RAM

tts.export('words.wav') # save to wav file
tts.export('words.mp3') # save to mp3 file

tts.play(volume = 1.0) # 0.0(lowest) to 1.0(highest)

# you can load multiple texts at once

tts.load('first going to be spoken')
tts.load('after that this is going to be spoken')
tts.load('at last this is going to be spoken')

tts.play()
