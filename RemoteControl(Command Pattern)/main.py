from garage import Garage
from garagedooropen import GarageDoorOpenCommand
from light import Light
from lightoncommand import LightOnCommand
from remotecontrol import SimpleRemoteControl

remote = SimpleRemoteControl()
light = Light()
garage = Garage()
lighton = LightOnCommand(light)
gardooropen = GarageDoorOpenCommand(garage)

remote.set_command(lighton)
remote.set_command(gardooropen)
remote.button_pressed()