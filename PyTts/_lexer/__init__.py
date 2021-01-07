from .lex import Lexer
from .lex import __load_modules__ as lex__load_modules__

def __start_load_modules__(**args):
    lex__load_modules__(**args)
