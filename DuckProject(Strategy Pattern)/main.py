from Duck import Duck
from FlyNoWay import FlyNoWay
from Quack import Quack

normal_duck = Duck()
plastic_duck = Duck()

normal_duck.quackBehaviour = Quack()
normal_duck.performQuack()

plastic_duck.flyBehaviour = FlyNoWay()
plastic_duck.performFly()