from subject import Subject

class WeatherData(Subject):
    temperature = int()
    humidity = int()
    pressure = int()

    def __init__(self):
        self.observers = []

    def register_observer(self,observer):
        self.observers.append(observer)

    def remove_observer(self,observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature,self.humidity,self.pressure)

    def measurements_changed(self,temperature,humidity,pressure):
        self.temperature=temperature
        self.humidity=humidity
        self.pressure=pressure
        self.notify_observers()
