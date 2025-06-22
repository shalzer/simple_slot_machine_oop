from abc import ABC, abstractmethod

class Spinable(ABC):
    @abstractmethod
    def get_value(self, symbol):
        pass

class Valuable(ABC):
    @abstractmethod
    def get_value(self, symbol):
        pass

class Accountable(ABC):
    @abstractmethod
    def deposit(self, amount):