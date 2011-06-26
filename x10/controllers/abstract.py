import time
import struct
import logging

import serial

from x10.devices.actuators import GenericX10Actuator
from x10.devices.house import X10House
from x10.exceptions import WriteError

logger = logging.getLogger(__name__)

class X10Controller(object):
    HOUSE_ENCMAP = {} # Encoding Map for House Code
    UNIT_ENCMAP = {} # Encoding Map for Unit Code

    def __init__(self, aDevice):
        self._device = aDevice
        self._handle = None

    def do(self, function, x10addr=None, amount=None):
        """
        Execute a function on the controller. E.g. Turn on a light.
        """
        raise NotImplementedError()

    def open(self):
        """
        Open the device and set it up
        """
        raise NotImplementedError()

    def close(self):
        """
        Close the controller
        """
        raise NotImplementedError()

    def read(self, bytes=100):
        """
        Read an amount of bytes from the controller
        """
        raise NotImplementedError()

    def write(self, aSequence):
        """
        Write a sequence of bytes to the interface
        """
        raise NotImplementedError()

    def ack(self):
        """
        Get if the device did well respond or not
        """
        raise NotImplementedError()

    def actuator(self, x10addr, aX10ActuatorKlass=None):
        """
        Given an address, return a device object.
        If an actuator class is provided, use it.
        """
        if aX10ActuatorKlass:
            return aX10ActuatorKlass(x10addr, self)
        else:
            return GenericX10Actuator(x10addr, self)

    def house(self, x10HouseCode):
        """
        Given a house code, return a House object
        """
        return X10House(x10HouseCode, self)


class SerialX10Controller(X10Controller):
    """
    Abstract Class for a Serial Controller (that can be used with an
    USB-Serial adapter too).

    Replace "device" with the default serial port your controller is
    connected to. In Windows, this could be "COM1" etc. On Mac/Unix,
    this will be '/dev/tty.something'. With an usb-to-serial adapter,
    it shows up as '/dev/tty.usbserial'. To find available ports, type
    'ls /dev/tty.*' at the terminal prompt.
    """
    DELAY_BIT = 0.001 # Seconds between bits
    DELAY_FIN = 1     # Seconds to wait before disabling after transmit

    def open(self):
        self._handle = serial.Serial(self._device)

    def _set_standby(self):
        """
        Put the device in standby
        """
        self._handle.setDTR(True)
        self._handle.setRTS(True)

    def _set_off(self):
        """
        Turn the device "off"
        """
        self._handle.setDTR(False)
        self._handle.setRTS(False)

    def write(self, aSequence):
        logger.debug("Writing %s", ["0x%02x" % i for i in aSequence])

        byte_count = len(hex(aSequence)) - 2

        mask = 1 << (byte_count - 1)
        
        self._set_standby()
        time.sleep(self.DELAY_BIT)    
        
        for i in range(0, byte_count):
            bit = aSequence & mask
            if bit == mask:
                self._handle.setDTR(False)
            elif bit == 0:
                self._handle.setRTS(False)
        
            time.sleep(self.DELAY_BIT)
            self._set_standby()
            
            # Then stay in standby before next bit
            time.sleep(self.DELAY_BIT)
            
            # Move to next bit in sequence
            aSequence = aSequence << 1


    def close(self):
        self._set_off()
        self._handle.close()

class UsbX10Controller(X10Controller):
    """
    Abstract Class for an USB Controller
    """
    vendorId = 0x0000
    productId = 0x0000

    write_endpoint = 0x00
    read_endpoint = 0x00

    def open(self):
        self._handle = self._device.open()

        config = self._device.configurations[0]        
        self._handle.setConfiguration(config)

        itf = config.interfaces[0][0]        
        self._handle.claimInterface(itf)

    def close(self):
        self._handle.releaseInterface()
        # clk = (0x9b, 20, 100, 2 >> 1, 1, 1, 0x60, 0x00)
        
        # seqclk = struct.pack("BBBBBBBB", *clk)
        # hand.bulkWrite(0x02, seqclk)
        # seq = (0x5A, 0x02, 0x00, 0x6E)

    def read(self, bytes=100):
        res = self._handle.bulkRead(self.read_endpoint, bytes)
        logger.debug( "Read %s", ["0x%02x" % i for i in res])
        return res

    def write(self, aSequence):
        logger.debug("Writing %s", ["0x%02x" % i for i in aSequence])

        packets = struct.pack("%dB" % len(aSequence), *aSequence)
        wrote = self._handle.bulkWrite(self.write_endpoint,
                                       packets)

        if wrote != len(aSequence):
            raise WriteError("Unable to write to the controller")

        # Wait for the controller
        time.sleep(1*(len(aSequence)))

