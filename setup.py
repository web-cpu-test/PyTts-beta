from distutils.core import setup
from setuptools import find_packages
import os

with open('MANIFEST.in','w') as f:
    for dirname, dirnames, filenames in os.walk('PyTts'):
        if '__pycache__' not in dirname:
            for fn in filenames:
                f.write('include ' + os.path.join(dirname,fn) + '\n')
setup(
	name='PyTts',
	version='1.0.0',
	license='apache-2.0',
	description='Text To Speech in Pure Python',
	author='Himanshu Jha',
	url='https://github.com/web-cpu-test/PyTts-beta',
	download_url='https://github.com/web-cpu-test/PyTts-beta',
	install_requires=['pygame', 'numpy'],
        include_package_data= True,
        packages = find_packages(),
)
