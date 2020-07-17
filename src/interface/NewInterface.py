import abc

"""
This is the New DB Interface.
"""

class NewInterface(metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def create(self): pass