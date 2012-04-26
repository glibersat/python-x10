def encodeX10HouseCode(house_code, anX10Controller):
    """
    Given an X10 House Code (e.g. "A"), return the value for this
    specific controller
    """
    return anX10Controller.HOUSE_ENCMAP[house_code]

def encodeX10UnitCode(unit_code, anX10Controller):
    """
    Given an X10 Unit Code (e.g. "6"), return the value for this
    specific controller
    """
    return anX10Controller.UNIT_ENCMAP[str(unit_code)]

def encodeX10Address(x10addr, controller):
    """
    Given an X10 Address (e.g. "B8"), return the value for this
    specific controller
    """
    res = encodeX10HouseCode(x10addr[0], controller) << 4
    res += encodeX10UnitCode(x10addr[1], controller)
    return res






