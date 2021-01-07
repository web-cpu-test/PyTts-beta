def __start_load_modules__(**args):
    for name,module in args.items():
        globals()[name] = module
    main()

def lines(_file):
    return [i.strip() for i in _file if i != '']

def text(_file):
    return _file.read()

def main():
    global basedir, sep, listdir, loaders
    basedir = os.path.dirname(os.path.realpath(__file__))
    sep = os.sep
    listdir = {}
    for x in os.listdir(basedir):
        if x != '__init__.py' and x != '__pycache__':
            listdir[x.split('.')[0]] = x.split('.')[-1]
    loaders = {
    'json' : ( json.load,  'r' ),
    'npz'  : ( numpy.load, 'rb'),
    'dict' : ( json.load,  'r' ),
    'lines': ( lines,      'r' ),
    'txt'  : ( text,       'r' ),
    }
        
def load(name):
    loader , mode = loaders[listdir[name]]
    file_name = basedir + sep + '.'.join([name,listdir[name]])
    file = open(file_name,mode)
    return loader(file)
