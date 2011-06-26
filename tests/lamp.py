import logging

from x10.controllers.bus import USBScanner

logger = logging.getLogger()
hdlr = logging.StreamHandler() # Console
formatter = logging.Formatter('%(module)s - %(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)

b = USBScanner()
devices = list(b.findDevices())

if len(devices) == 0:
    print "No device found"
    exit()

dev = devices[0]

dev.open()

livinglamp = dev.actuator("A1")

roomlamp = dev.actuator("A2")
#roomlamp.on()

roomlamp.on()

#livinglamp.on()

#livinglamp.adjust(100)

#house = dev.house("A")

#house.unitsOff()

#house.lightsOff()
#house.lightsOn()

dev.close()






