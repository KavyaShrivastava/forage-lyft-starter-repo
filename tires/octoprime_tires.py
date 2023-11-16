from .tires import Tires

class Octoprime(Tires):
    def __init__(self, wear_sensors:list[float]):
        if len(wear_sensors) != 4:
            raise ValueError("Array must contain exactly four elements")
        for wear in wear_sensors:
            if wear < 0 or wear > 1:
                raise ValueError("Elements must be between 0 and 1")
        self.wear_sensors = wear_sensors
    
    #Octoprime tires should be serviced only when the sum of all values in the tire wear array is greater than or equal to 3.
    def need_service(self)->bool:
        sum = self._sum_of_wear_sensors()
        return sum>=3
        
    def _sum_of_wear_sensors(self):
        sum=0
        for i in self.wear_sensors:
            sum+=i
        return sum