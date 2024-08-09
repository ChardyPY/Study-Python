from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def calculate_total_price(self):
        pass


