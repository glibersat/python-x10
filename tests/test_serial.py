import logging

from x10.controllers.cm17a import CM17a

logger = logging.getLogger()
hdlr = logging.StreamHandler() # Console
formatter = logging.Formatter('%(module)s - %(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.DEBUG)

dev = CM17a('/dev/ttyUSB')
dev.open()

livinglamp = dev.actuator("A1")

livinglamp.on()

dev.close()






