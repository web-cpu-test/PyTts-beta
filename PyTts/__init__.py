# EXTERNAL MODULES
import numpy
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from pygame import mixer

# BUILT-IN MODULES
import os
import wave
import json
from functools import lru_cache
import sys
import re
import warnings
import struct
from zipfile import ZipFile

# PACKAGE MODULES
from . import _data as _data_
from . import _lexer as _lexer_
from . import _WaveFile as _WaveFile_
from . import _voice as _voice_
from . import _pronouncer as _pronouncer_
from . import _tempfile as _tempfile_
from . import _AudioCodecs as _AudioCodecs_
from . import TTS as _TTS_

_data_.__start_load_modules__(
    numpy       = numpy,
    os          = os,
    json        = json,
)

_pronouncer_.__start_load_modules__(
    np          = numpy,
    data        = _data_,
    regex       = re,
)

_tempfile_.__start_load_modules__(
    os          = os,
)

_lexer_.__start_load_modules__(
    re          = re,
)

_voice_.__start_load_modules__(
    np          = numpy,
    ZipFile     = ZipFile,
    json        = json,
    tempfile    = _tempfile_.tempfile.tempfile,
    os          = os,
    load        = _data_.load,
    read        = _WaveFile_.read,
)

_WaveFile_.__start_load_modules__(
    struct      = struct,
    sys         = sys,
    warnings    = warnings,
    numpy       = numpy,
)

_AudioCodecs_.__start_load_modules__(
    np          = numpy,
    wave        = wave,
    lameenc     = _AudioCodecs_.mp3.lameenc,
)

_TTS_.__start_load_modules__(
    numpy       = numpy,
    json        = json,
    audio_enc   = _AudioCodecs_,
    pronounce   = _pronouncer_.pronouncer(lru_cache).pronounce,
    mixer       = mixer,
)

trainer = _voice_.train.Trainer
