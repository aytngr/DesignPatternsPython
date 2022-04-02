from observer import Observer
from display_element import DisplayElement
from subject import Subject

class DisplayCurrentConditions(Observer,DisplayElement):
    temperature = int()
    humidity=int()
    pressure=int()

    def __init__(self,weatherdata):
        self.weatherdata=weatherdata
        weatherdata.register_observer(self)

    def update(self,temperature,humidity,pressure):
        self.temperature=temperature
        self.humidity=humidity
        self.pressure=pressure
        self.display()

    def display(self):
        print(f"Temperature: {self.temperature}, Humidity: {self.humidity}, Pressure: {self.pressure}")