from usb import Device

from x10.utils import encodeX10Address, encodeX10HouseCode
from x10.protocol import functions

from .abstract import X10Controller

class CM15(X10Controller):
    vendorId = 0x0BC7
    productId = 0x0001

    write_endpoint = 0x02
    read_endpoint = 0x81

    def ack(self): 
        """
        Get if the device did well respond or not
        """
        res = self.read()
        # 0x55 is a Ack
        return (res[0] == 0x55)

    def _select(self, x10addr):
        # 0x04 selects a device
        sel_seq = (0x04, encodeX10Address(x10addr))
        self.write(sel_seq)

    def do(self, function, x10addr=None, amount=None):
        """
        Execute a function on the controller. E.g. Turn on a light.
        """
        # If we address a specific device, select it
        if len(x10addr) == 2:
            self._select(x10addr)

        # 0x06 execute a command
        fn = encodeX10HouseCode(x10addr[0]) << 4
        fn += function
        cmd = [0x06, fn]

        if function in (functions.DIM,
                        functions.BRIGHT):
            cmd.append((amount*2))

        self.write(cmd)

        #self.ack()






