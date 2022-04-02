from abc import ABC, abstractmethod

class Pizza(ABC):
    name = ""
    
    def prepare(self):
        print("Pizza is preparing")

    def box(self):
        print("Pizza boxed")