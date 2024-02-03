# This is a CarFactory class that creates a car object 
# and returns the car object to the main program.

from array import array
from datetime import date
from car import Car
from spindlerBattery import SpindlerBattery
from nubbinBattery import NubbinBattery
from capuletEngine import CapuletEngine
from willoughbyEngine import WilloughbyEngine
from sternmanEngine import SternmanEngine
from carriganTires import CarriganTires
from octoprimeTires import OctoprimeTires

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, wear_sensors: array[int]):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = wear_sensors
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, wear_sensors: array[int]):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = wear_sensors
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, wear_sensors: array[int]):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = wear_sensors
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, wear_sensors: array[int]):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = wear_sensors
        return Car(engine, battery, tires)
    
    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, wear_sensors: array[int]):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = wear_sensors
        return Car(engine, battery, tires)
