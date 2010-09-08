def encodeX10HouseCode(house_code):
    return {"A" : 0x6,
            "B" : 0xE,
            "C" : 0x2,
            "D" : 0xA,
            "E" : 0x1,
            "F" : 0x9,
            "G" : 0x5,
            "H" : 0xD,
            "I" : 0x7,
            "J" : 0xF,
            "K" : 0x3,
            "L" : 0xB,
            "M" : 0x0,
            "N" : 0x8,
            "O" : 0x4,
            "P" : 0xC
            }[house_code]

def encodeX10DeviceCode(device_code):
    return {"1" : 0x6,
            "2" : 0xE,
            "3" : 0x2,
            "4" : 0xA,
            "5" : 0x1,
            "6" : 0x9,
            "7" : 0x5,
            "8" : 0xD,
            "9" : 0x7,
            "10" : 0xF,
            "11" : 0x3,
            "12" : 0xB,
            "13" : 0x0,
            "14" : 0x8,
            "15" : 0x4,
            "16" : 0xC
            }[device_code]


def encodeX10Address(x10addr):
    res = encodeX10HouseCode(x10addr[0]) << 4
    res += encodeX10DeviceCode(x10addr[1])
    return res






