from x10.controllers.bus import USBScanner
from x10.protocol import functions

b = USBScanner()
dev = b.findDevices()
dev.open()

livinglamp = dev.actuator("A1")

roomlamp = dev.actuator("A2")
#roomlamp.on()

roomlamp.on()

livinglamp.off()

#livinglamp.adjust(100)

#house = dev.house("A")

#house.unitsOff()

#house.lightsOff()
#house.lightsOn()

#dev.close()






