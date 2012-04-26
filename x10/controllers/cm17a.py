#-----------------------------------------------------------
# X10 Firecracker CM17A Interface Driver
#
# Copyright (c) 2011 Guillaume Libersat
# Copyright (c) 2010 Collin J. Delker
#
# based on Collin J. Delker's implementation
#
#-----------------------------------------------------------
#
#   X10 Firecracker CM17A protocol specificaiton:
#   ftp://ftp.x10.com/pub/manuals/cm17a_protocol.txt
#
#-----------------------------------------------------------

import time

from .abstract import SerialX10Controller

from ..utils import encodeX10HouseCode, encodeX10UnitCode, encodeX10Address

from x10.protocol import functions

class CM17a(SerialX10Controller):
    """
    Firecracker spec requires at least 0.5ms between bits
    """
    DELAY_BIT = 0.001
    DELAY_FIN = 1

    # -----------------------------------------------------------
    # House and unit code table
    # -----------------------------------------------------------
    HOUSE_ENCMAP = {
        "A": 0x6000,
        "B": 0x7000,
        "C": 0x4000,
        "D": 0x5000,
        "E": 0x8000,
        "F": 0x9000,
        "G": 0xA000,
        "H": 0xB000,
        "I": 0xE000,
        "J": 0xF000,
        "K": 0xC000,
        "L": 0xD000,
        "M": 0x0000,
        "N": 0x1000,
        "O": 0x2000,
        "P": 0x3000
        }
    
    UNIT_ENCMAP = {
        "1": 0x0000,
        "2": 0x0010,
        "3": 0x0008,
        "4": 0x0018,
        "5": 0x0040,
        "6": 0x0050,
        "7": 0x0048,
        "8": 0x0058,
        "9": 0x0400,
        "10": 0x0410,
        "11": 0x0408,
        "12": 0x0400,
        "13": 0x0440,
        "14": 0x0450,
        "15": 0x0448,
        "16": 0x0458
        }

    # -----------------------------------------------------------
    # Command Code Masks
    # -----------------------------------------------------------
    CMD_ON   = 0x0000
    CMD_OFF  = 0x0020
    CMD_BRT  = 0x0088
    CMD_DIM  = 0x0098

    # -----------------------------------------------------------
    # Data header and footer, for writes
    # -----------------------------------------------------------
    DATA_HDR = 0xD5AA # Data header
    DATA_FTR = 0xAD # Data footer
    
    def ack(self):
        return True

    def do(self, function, x10addr=None, amount=None):
        cmd = 0x00000000
        
        house = x10addr[0]
        unit = int(x10addr[1])

        # Add in the house code
        cmd = cmd | encodeX10HouseCode(house, self)

        # Add in the unit code. Ignore if bright or dim command,
        # which just applies to last unit.
        if function not in (functions.BRIGHT, functions.DIM):
            cmd = cmd | encodeX10UnitCode(unit, self)
        
        # Add the action code
        if function == functions.ON:
            cmd = cmd | self.CMD_ON
        elif function == functions.OFF:
            cmd = cmd | self.CMD_OFF
        elif function == functions.BRIGHT:
            cmd = cmd | self.CMD_BRT
        elif function == functions.DIM:
            cmd = cmd | self.CMD_DIM

        # Write everything to the device
        self.write(self.DATA_HDR) # Send data header
        self.write(cmd) # Send data
        self.write(self.DATA_FTR) # Send footer
        
        time.sleep(self.DELAY_FIN) # Wait for firecracker to finish transmitting

    
