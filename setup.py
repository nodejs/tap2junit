# coding: utf-8

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tap2junit',
    version='0.1.4',
    description='Tap13 to jUnit',
    long_description=long_description,
    url='https://github.com/jbergstroem/tap2junit',
    author='Johan Bergström',
    author_email='bugs@bergtroem.nu',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        'Programming Language :: Python :: 2',
    ],
    keywords='tap13 junit',
    packages=['tap2junit'],
    install_requires=['yamlish', 'junit-xml'],
    entry_points={
        'console_scripts': [
            'tap2junit = tap2junit.__main__:main',
        ],
    },
)
