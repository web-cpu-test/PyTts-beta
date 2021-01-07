from .SoundObj import __load_modules__ as SoundObj__load_modules__
from .engine import __load_modules__ as engine__load_modules__

def __start_load_modules__(**args):
    SoundObj__load_modules__(**args)
    engine__load_modules__(**args)
