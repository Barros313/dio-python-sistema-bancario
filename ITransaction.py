from abc import ABC, abstractmethod


class ITransaction(ABC):
    @abstractmethod
    def register(self, account): pass