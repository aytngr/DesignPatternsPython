from command import Command

class GarageDoorOpenCommand(Command):
    def __init__(self,garage):
        self.garage = garage
    def execute(self):
        self.garage.up()
