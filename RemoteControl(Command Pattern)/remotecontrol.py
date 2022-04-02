class RemoteControl:
    on_commands = []
    off_commands = []

    def __init__(self):
        for i in range(0,7):
            self.on_commands[i] = None
            self.off_commands[i] = None

    def set_command(self, slot, on_command, off_command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pressed(self,slot):
        self.on_commands[slot].execute()

    def off_button_pressed(self,slot):
        self.off_commands[slot].execute()
