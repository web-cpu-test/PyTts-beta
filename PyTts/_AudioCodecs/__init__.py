from .mp3 import __start_load_modules__ as mp3__start_load_modules__
from .wav import __start_load_modules__ as wav__start_load_modules__


def __start_load_modules__(**args):
    mp3__start_load_modules__(**args)
    wav__start_load_modules__(**args)