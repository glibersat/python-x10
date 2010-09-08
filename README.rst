=========================================
A python module to control X10 appliances
=========================================

Current state: alpha and incomplete

Authors::
- Guillaume Libersat <glibersat@sigill.org>

Contributions are welcomed !

--------
Features
--------

Drivers
=======

- CM15

Actuators
=========

- Switch (On/Off state)
- Generic (Used to talk to any X10 device)

Meta-modules
============

- House (Something like a "group" of devices)

-----------
API Example
-----------

::

 lamp = dev.actuator("A2")
 lamp.dim(10)
 lamp.off()
 house = dev.house("B")
 house.lightsOff()
