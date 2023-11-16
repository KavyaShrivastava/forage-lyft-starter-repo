import unittest
from tires.carrigan_tires import Carrigan
from tires.octoprime_tires import Octoprime

class CarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        wear_sensors = [0, 0.99, 0.3, 0.4]
        tires = Carrigan(wear_sensors)
        self.assertTrue(tires.need_service())
    
    def test_tires_should_not_be_serviced(self):
        wear_sensors = [0, 0.7, 0.3, 0.4]
        tires = Carrigan(wear_sensors)
        self.assertFalse(tires.need_service())

class OctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        wear_sensors = [0, 1, 1, 1]
        tires = Octoprime(wear_sensors)
        self.assertTrue(tires.need_service())
    
    def test_tires_should_not_be_serviced(self):
        wear_sensors = [0, 0.7, 0.3, 0.4]
        tires = Octoprime(wear_sensors)
        self.assertFalse(tires.need_service())     
        
if __name__ == '__main__':
    unittest.main()

