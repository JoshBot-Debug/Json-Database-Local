import abc

"""
This is the Create Interface.
"""

class CreateInterface(metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def table(self,Name: str): pass


    @abc.abstractmethod
    def keys(self,Keys: list): pass


    @abc.abstractmethod
    def _getTable(self): pass


    @abc.abstractmethod
    def _getRows(self): pass