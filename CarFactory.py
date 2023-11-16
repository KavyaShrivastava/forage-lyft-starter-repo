from datetime import date
from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery

class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        eng = CapuletEngine(current_mileage, last_service_mileage)
        bat = SpindlerBattery(last_service_date, current_date)
        return Car(eng,bat)
    
    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        eng = WilloughbyEngine(current_mileage, last_service_mileage)
        bat = SpindlerBattery(last_service_date, current_date)
        return Car(eng,bat)
    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool)-> Car:
        eng = SternmanEngine(warning_light_on)
        bat = SpindlerBattery(last_service_date, current_date)
        return Car(eng,bat)
    
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int)-> Car:
        eng = WilloughbyEngine(current_mileage, last_service_mileage)
        bat = NubbinBattery(last_service_date, current_date)
        return Car(eng, bat)
    
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        eng = CapuletEngine(current_mileage, last_service_mileage)
        bat = NubbinBattery(last_service_date, current_date)
        return Car(eng,bat)
        
        

        
        
        
    