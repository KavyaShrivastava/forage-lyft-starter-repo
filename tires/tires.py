from abc import ABC, abstractmethod

class Tires(ABC):
    # def __init__(self, wear_sensors: List[int]):
    #     self.wear_sensors = wear_sensors

    @abstractmethod
    def need_service(self) -> bool:
        pass