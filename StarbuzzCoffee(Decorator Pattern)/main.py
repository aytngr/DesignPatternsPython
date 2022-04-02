from beverage import Beverage
from espresso import Espresso
from mocha import Mocha

beverage = Espresso()
print(f"{beverage.get_description()}, {beverage.cost()}")

beverage2 = Espresso()
beverage2 = Mocha(beverage2)
print(f"{beverage2.get_description()}, {beverage2.cost()}")