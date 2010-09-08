import math
from x10.protocol import functions

class AbstractX10Actuator(object):
    def __init__(self, x10addr, aX10Controller):
        self.x10addr = x10addr
        self.x10ctrl = aX10Controller


class SwitchableX10Actuator(AbstractX10Actuator):
    def on(self):
        """
        Turn on
        """
        self.x10ctrl.do(functions.ON, self.x10addr)

    def off(self):
        """
        Turn off
        """
        self.x10ctrl.do(functions.OFF, self.x10addr)

class DimmableX10Actuator(AbstractX10Actuator):
    def dim(self, amount):
        """
        Reduce voltage
        """
        self.x10ctrl.do(functions.DIM, self.x10addr, amount=amount)

    def bright(self, amount):
        """
        Augment voltage
        """
        self.x10ctrl.do(functions.BRIGHT, self.x10addr, amount=amount)

    def adjust(self, amount):
        """
        Augment or reduce voltage
        """
        if amount > 0:
            self.bright(amount)
        else:
            self.dim(int(math.fabs(amount)))

class GenericX10Actuator(SwitchableX10Actuator,
                         DimmableX10Actuator):
    pass
                         





