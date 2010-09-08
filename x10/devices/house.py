from x10.protocol import functions

class X10House(object):
    def __init__(self, x10houseCode, aX10Controller):
        self.x10houseCode = x10houseCode
        self.x10ctrl = aX10Controller

    def unitsOff(self):
        self.x10ctrl.do(functions.ALLUOFF, self.x10houseCode)

    def lightsOff(self):
        self.x10ctrl.do(functions.ALLLOFF, self.x10houseCode)

    def lightsOn(self):
        self.x10ctrl.do(functions.ALLLON, self.x10houseCode)






