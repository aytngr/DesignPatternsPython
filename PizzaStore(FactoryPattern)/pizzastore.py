from abc import ABC, abstractmethod
class PizzaStore(ABC):

    def order_pizza(self,type):
        pizza = self.create_pizza(type)
        pizza.prepare()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self,type):
        pass