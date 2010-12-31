from .abstract import X10Controller

__author__ = "fabriceb@theodo.fr"
__date__ = "2010-12-31"

class MockX10Controller(X10Controller):
    """
    Mock class to be able to test python code dependent on python-x10
    """
    def ack(self):
        return True

    def do(self, function, x10addr=None, amount=None):
        pass
