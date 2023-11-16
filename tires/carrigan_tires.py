from .tires import Tires

class Carrigan(Tires):
    def __init__(self, wear_sensors:list[float]):
        if len(wear_sensors) != 4:
            raise ValueError("Array must contain exactly four elements")
        for wear in wear_sensors:
            if wear < 0 or wear > 1:
                raise ValueError("Elements must be between 0 and 1")
        self.wear_sensors = wear_sensors
    
    #Carrigan tires should be serviced only when one or more of the values in the tire wear array is greater than or equal to 0.9.
    def need_service(self)->bool:
        for i in self.wear_sensors:
            if i >=0.9:
                return True
        return False