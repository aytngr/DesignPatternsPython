class Duck:
    flyBehaviour = None
    quackBehaviour = None

    def performQuack(self):
        self.quackBehaviour.quack()
    def performFly(self):
        self.flyBehaviour.fly()