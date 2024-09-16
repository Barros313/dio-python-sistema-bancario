from abc import ABC, abstractmethod


class ITransaction(ABC):
    @property
    @abstractmethod
    def value(self): pass

    @classmethod
    @abstractmethod
    def register(self, account): pass