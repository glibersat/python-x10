import logging

import usb

from ..exceptions import NoDeviceFoundError
from .cm15 import CM15

logger = logging.getLogger(__name__)

class USBScanner(object):
    devices = (CM15,)

    def findDevice(self, anUsbX10ControllerClass):
        """
        For a given X10 Controller class, scan the USB busses trying to find it.
        raises NoDeviceFoundError if none is found.
        """
        busses = usb.busses()

        for bus in busses:
            for dev in bus.devices:
                if dev.idVendor == anUsbX10ControllerClass.vendorId and \
                        dev.idProduct == anUsbX10ControllerClass.productId:
                    logger.info("Found device %s" % anUsbX10ControllerClass)
                    return anUsbX10ControllerClass(dev)

        raise NoDeviceFoundError()
        

    def findDevices(self):
        """
        For each known device, scan the USB bus and yield it if found
        """
        for X10DeviceClass in self.devices:
            try:
                yield self.findDevice(X10DeviceClass)
            except NoDeviceFoundError, e:
                pass
