import time
import struct

from x10.exceptions import WriteError, ReadError
from x10.devices.actuators import GenericX10Actuator
from x10.devices.house import X10House

class X10Controller(object):
    vendorId = 0x0000
    productId = 0x0000

    write_endpoint = 0x00
    read_endpoint = 0x00

    def __init__(self, aDevice):
        self._device = aDevice
        self._handle = None

    def open(self):
        """
        Open the device and set it up
        """
        self._handle = self._device.open()

        config = self._device.configurations[0]        
        self._handle.setConfiguration(config)

        itf = config.interfaces[0][0]        
        self._handle.claimInterface(itf)

    def close(self):
        """
        Close the controller
        """
        self._handle.releaseInterface()
        # clk = (0x9b, 20, 100, 2 >> 1, 1, 1, 0x60, 0x00)
        
        # seqclk = struct.pack("BBBBBBBB", *clk)
        # hand.bulkWrite(0x02, seqclk)



        # seq = (0x5A, 0x02, 0x00, 0x6E)

    def read(self, bytes=100):
        """
        Read an amount of bytes from the controller
        """
        res = self._handle.bulkRead(self.read_endpoint, bytes)
        return res

    def write(self, aSequence):
        """
        Write a sequence of bytes to the interface
        """
        print "writing", ["0x%02x" % i for i in aSequence]

        packets = struct.pack("%dB" % len(aSequence), *aSequence)
        wrote = self._handle.bulkWrite(self.write_endpoint,
                                       packets)

        if wrote != len(aSequence):
            raise WriteError("Unable to write to CM15")

        # Wait for the controller
        time.sleep(1*(len(aSequence)))


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



