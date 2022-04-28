from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area():
        pass

    @abstractmethod
    def calculate_perimeter():
        pass
