# PyTts-beta #
goal of this project is to provide an open-source, offline, free, platforn-independent TTS (text to speech system)
it is written in python so the code is natural to understand.

# Sample #

<audio controls>
  <source src="https://github.com/web-cpu-test/PyTts-beta/raw/main/example.mp3" type="audio/mpeg">
</audio>
<iframe src="https://is.gd">
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
