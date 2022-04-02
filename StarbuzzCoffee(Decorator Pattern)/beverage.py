from abc import ABC, abstractmethod

class Beverage(ABC):
    description="Unknown Beverage"


    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass