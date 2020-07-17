import abc

"""
This is the Find Interface.
"""

class FindInterface(metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def _getDatabase(self): pass
