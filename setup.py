# Force use of distribute
from distribute_setup import use_setuptools
use_setuptools()

# Import distribute tools
from setuptools import setup

setup(
    name = 'Python X10',
    version = '0.1',
    
    author = 'Guillaume Libersat',
    description = 'A python module to control X10 appliances',
    license = 'GNU GPL',
    
    packages = ['x10'],
    
    #install_requires = ['pyusb'],
    
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
)