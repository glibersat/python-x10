=========================================
A python module to control X10 appliances
=========================================

Current state: working but incomplete API

:Authors: Guillaume Libersat (@glibersat)

:Contributors:
  Axel Haustant (@noirbizarre), Riccardo Ferrazzo (@rferrazz)

:License: GPL v3 (see COPYING)

Contributions are welcomed !

------------
Requirements
------------

python-x10 requires:

- Python 2.5
- PyUSB 0.x (http://pyusb.berlios.de/)
- pySerial (http://pyserial.sourceforge.net/)

--------
Features
--------

Drivers
=======

- CM11/12 (thanks Riccardo!)
- CM15
- CM17a (Need testing!)

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

------------------------------------
Ideas and drivers that may be merged
------------------------------------

- CM19a driver: http://www.cuddon.net/search/label/CM19a
- Another CM19a driver:
  http://m.lemays.org/projects/x10-cm19a-linux-driver
- PyXAL X10netc client/server
