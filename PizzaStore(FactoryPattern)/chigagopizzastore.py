from pizzastore import PizzaStore
from cheesepizza import CheesePizza
from veggie import VeggiePizza
class ChigagoPizzaStore(PizzaStore):
    def create_pizza(self,type):
        if type == "cheese":
            return CheesePizza()
        if type == "veggie":
            return VeggiePizza()