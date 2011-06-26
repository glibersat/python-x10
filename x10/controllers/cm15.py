from x10.utils import encodeX10Address, encodeX10HouseCode
from x10.protocol import functions

from .abstract import UsbX10Controller

class CM15(UsbX10Controller):
    vendorId = 0x0BC7
    productId = 0x0001

    write_endpoint = 0x02
    read_endpoint = 0x81

    HOUSE_ENCMAP = {
        "A": 0x6,
        "B": 0xE,
        "C": 0x2,
        "D": 0xA,
        "E": 0x1,
        "F": 0x9,
        "G": 0x5,
        "H": 0xD,
        "I": 0x7,
        "J": 0xF,
        "K": 0x3,
        "L": 0xB,
        "M": 0x0,
        "N": 0x8,
        "O": 0x4,
        "P": 0xC
        }

    UNIT_ENCMAP = {
        "1": 0x6,
        "2": 0xE,
        "3": 0x2,
        "4": 0xA,
        "5": 0x1,
        "6": 0x9,
        "7": 0x5,
        "8": 0xD,
        "9": 0x7,
        "10": 0xF,
        "11": 0x3,
        "12": 0xB,
        "13": 0x0,
        "14": 0x8,
        "15": 0x4,
        "16": 0xC
        }
    
    def ack(self): 
        """
        Get if the device did well respond or not
        """
        res = self.read()
        # 0x55 is a Ack
        return (res[0] == 0x55)

    def _select(self, x10addr):
        # 0x04 selects a device
        sel_seq = (0x04, encodeX10Address(x10addr, self))
        self.write(sel_seq)

    def do(self, function, x10addr=None, amount=None):
        # If we address a specific device, select it
        if len(x10addr) == 2:
            self._select(x10addr)

        # 0x06 execute a command
        fn = encodeX10HouseCode(x10addr[0], self) << 4
        fn += function
        cmd = [0x06, fn]

        if function in (functions.DIM,
                        functions.BRIGHT):
            cmd.append((amount*2))

        self.write(cmd)






