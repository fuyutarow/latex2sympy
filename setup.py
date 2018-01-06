import os
import re
from setuptools import setup

try:
    with open('README.md') as f:
        long_description = f.read()
except:
    long_description = ''

d_include_dir = []
for root, folders, files in os.walk("latex2sympy/gen"):
    buff = []
    d_include_dir.append(
        re.sub("\\\\", "/", re.sub("latex2sympy/", "", root)) + "/*.*")
    for f in files:
        buff.append(f)

setup(
    name='latex2sympy3',
    version='0.1.1',
    description='Sympy generator from LaTeX expressions.',
    long_description=long_description,
    maintainer='jack',
    maintainer_email='jack@bancast.net',
    url='https://github.com/jackatbancast/latex2sympy',
    packages=['latex2sympy'],
    package_data={'latex2sympy': d_include_dir},
    license='MIT',
    install_requires=['antlr4-python3-runtime==4.5.3', 'sympy'])
