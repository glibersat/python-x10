from distutils.core import setup

setup(
    name = 'Python-X10',
    version = '0.1',

    author = 'Guillaume Libersat',
    description = 'A python module to control X10 appliances',
    url = 'https://github.com/glibersat/python-x10',

    license = 'GNU GPL',

    install_requires=[
        'pyusb>=1.0.0a1',
        'pyserial>=2'
    ],
    
    packages = ['x10', 'x10/controllers', 'x10/devices']
)
