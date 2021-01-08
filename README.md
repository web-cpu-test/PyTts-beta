# PyTts-beta #
goal of this project is to provide an open-source, offline, free, platforn-independent TTS (text to speech system)
it is written in python so the code is natural to understand.

# Sample #

[![](data:image/png;base64,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)](https://github.com/web-cpu-test/PyTts-beta/raw/main/example.mp3)


this sample has been made by and model (unofficial copy of amazon justin) which is under build and will be released when complete.

# Installing #
###  Build from source ###
```setup.py bdist_wheel install```

### Install from compiled ###
```pip install PyTts-1.0.0-py3-none-any.whl```


# Dependencies #
1. pygame [audio handling]
1. numpy [model prediction]

# examples #


##### Train #####
```python
from PyTts import trainer

path_to_data_folder = 'C:\\path\\to\\data\\folder\\OBAMA_SOUND'

# this folder should contain 70 .wav files
# with name in format <containded_sound>.wav
# there should be 70 sounds as listed bellow
#
# AA0.wav   AA1.wav   AA2.wav   AE0.wav   AE1.wav
# AE2.wav   AH0.wav   AH1.wav   EH2.wav   EH1.wav  
# AH2.wav   ER0.wav   EY1.wav   EY2.wav   F.wav  
# AO0.wav   ER1.wav   G.wav     HH.wav    IH0.wav  
# AO1.wav   EY0.wav   IH1.wav   IH2.wav   IY0.wav  
# AO2.wav   ER2.wav   IY1.wav   IY2.wav   JH.wav  
# AW0.wav   K.wav     L.wav     M.wav     N.wav  
# AW1.wav   NG.wav    OW0.wav   OW1.wav   OW2.wav  
# AW2.wav   OY0.wav   OY1.wav   OY2.wav   P.wav  
# AY0.wav   R.wav     S.wav     SH.wav    T.wav  
# AY1.wav   TH.wav    UH2.wav   UW2.wav   W.wav  
# AY2.wav   UH0.wav   UW.wav    UW1.wav   Y.wav  
# B.wav     UH1.wav   UW0.wav   V.wav     Z.wav  
# CH.wav    ZH.wav    D.wav     DH.wav    EH0.wav   
#
# [MAIN-SOUND][FORCE].wav
# i.e. AA1.wav, AA0.wav
# @ MAIN-SOUND the sound of the letters
# @ FORCE is the duration or emphasis on the sound
#
# soon we will provide with detail guide on model training
# and some pre trained models :)

model = trainer(path_to_data_folder,pause=0.4) # pause between words
model.train() # this will generate OBAMA_SOUND.PyTts
```


##### Use #####

```python
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
```

# License #
```Apache license 2.0``` can be found in the root directory
