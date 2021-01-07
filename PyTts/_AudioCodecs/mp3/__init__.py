from .mp3 import __load_modules__ as mp3__load_modules__
from . import lameenc

def __start_load_modules__(**args):
    mp3__load_modules__(**args)
