import serial

from .abstract import SerialX10Controller, X10Controller

from ..utils import encodeX10HouseCode, encodeX10UnitCode, encodeX10Address

from x10.protocol import functions

class CM11(SerialX10Controller):
    
    # -----------------------------------------------------------
    # House and unit code table
    # -----------------------------------------------------------
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
    
    HD_SEL = 0x04
    HD_FUN = 0x06
    
    def __init__(self, aDevice):
        X10Controller.__init__(self, aDevice)
        self._baudrate = 4800
        
    def open(self):
        SerialX10Controller.open(self)
        while True:
            data = self.read()
            print data
            if data == 0xA5:
                self.write(0x9B)
            if data == "":
                break
    
    def ack(self):
        return True
    
    def actuator(self, x10addr, aX10ActuatorKlass=None):
        select = (encodeX10HouseCode(x10addr[0], self) << 4) | encodeX10UnitCode(x10addr[1:], self)
        checksum = 0x00
        
        while checksum != self.HD_SEL+select:
            self.write(self.HD_SEL)
            self.write(select)
            checksum = self.read()
        self.write(0x00)
        self.read()
        return SerialX10Controller.actuator(self, x10addr, aX10ActuatorKlass=aX10ActuatorKlass)
    
    def do(self, function, x10addr=None, amount=None):
        cmd = (encodeX10HouseCode(x10addr[0], self) << 4) | function
        checksum = 0x00
        
        while checksum != self.HD_FUN+cmd:
            self.write(self.HD_FUN)
            self.write(cmd)
            checksum = self.read()
        self.write(0x00)
        self.read()