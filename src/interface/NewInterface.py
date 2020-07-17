import abc

"""
This is the New DB Interface.
"""

class NewInterface(metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def _create(self): pass