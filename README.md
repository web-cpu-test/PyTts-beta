[![Made with Python](https://img.shields.io/badge/Made%20with-Python-orange?style=for-the-badge&logo=Python)](https://www.python.org/)

[![GitHub license](https://img.shields.io/github/license/web-cpu-test/PyTts-beta.svg)](https://github.com/web-cpu-test/PyTts-beta/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/web-cpu-test/PyTts-beta.svg)](https://GitHub.com/web-cpu-test/PyTts-beta/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/web-cpu-test/PyTts-beta.svg)](https://GitHub.com/web-cpu-test/PyTts-beta/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/web-cpu-test/PyTts-beta.svg)](https://GitHub.com/web-cpu-test/PyTts-beta/issues?q=is%3Aissue+is%3Aclosed)

[![GitHub forks](https://img.shields.io/github/forks/web-cpu-test/PyTts-beta.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/web-cpu-test/PyTts-beta/network/)
[![GitHub stars](https://img.shields.io/github/stars/web-cpu-test/PyTts-beta.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/web-cpu-test/PyTts-beta/stargazers/)
[![GitHub watchers](https://img.shields.io/github/watchers/web-cpu-test/PyTts-beta.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/web-cpu-test/PyTts-beta/watchers/)
[![GitHub followers](https://img.shields.io/github/followers/web-cpu-test.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/web-cpu-test?tab=followers)


# PyTts-beta #
goal of this project is to provide an open-source, offline, free, platforn-independent TTS (text to speech system)
it is written in python so the code is natural to understand.

# Sample #

[![](https://raw.githubusercontent.com/web-cpu-test/PyTts-beta/main/audio.png)](http://webcputestexample.pythonanywhere.com/example.mp3)


this sample has been made by and model (unofficial copy of amazon justin) which is under build and will be released when complete.

# Installing #
###  Build from source ###
```setup.py bdist_wheel install```

### Install from compiled ###
```pip install PyTts-1.0.0-py3-none-any.whl```


# Dependencies #
1. pygame [ audio handling   ]
1. numpy  [ model prediction ]

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



[![web-cpu-test github stats](https://github-readme-stats.vercel.app/api?username=web-cpu-test)](https://github.com/web-cpu-test)
