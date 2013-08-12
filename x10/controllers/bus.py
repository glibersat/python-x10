import logging

import usb
import usb.core

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
        device = usb.core.find(idVendor=anUsbX10ControllerClass.vendorId,
                               idProduct=anUsbX10ControllerClass.productId)

        if device:
            logger.info("Found device %s" % anUsbX10ControllerClass)
            return anUsbX10ControllerClass(device)

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
