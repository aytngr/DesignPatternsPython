from abc import ABC,abstractmethod

class Subject(ABC):
    @abstractmethod
    def register_observer(self,observer):
        pass
    def remove_observer(self,observer):
        pass
    def notify_observers(self):
        pass

