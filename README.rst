=========================================
A python module to control X10 appliances
=========================================

Current state: alpha and incomplete

:Authors: Guillaume Libersat <glibersat@sigill.org>

:Contributors:
  Axel Haustant <noirbizarre@gmail.com>

:License: GPL v3 (see COPYING)

Contributions are welcomed !

------------
Requirements
------------

python-x10 requires:

- Python 2.5
- PyUSB 0.x (http://pyusb.berlios.de/)

--------
Features
--------

Drivers
=======

- CM15

Actuators
=========

- Switchable (On/Off state)
- Dimmable (Variable state)
- Generic (Used to talk to any X10 device)

Meta-modules
============

- House (Something like a "group" of devices)

-----------
API Example
-----------

::

 # Retrieve USB CM15 Device
 scanner = USBScanner()
 dev = scanner.findDevices()
 dev.open()

 # Use a single module
 lamp = dev.actuator("A2")
 lamp.dim(10)
 lamp.off()
 
 # Use a group
 house = dev.house("B")
 house.lightsOff()

More samples in tests.