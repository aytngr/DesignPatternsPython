from abc import ABC,abstractmethod
from beverage import Beverage

class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self):
        pass