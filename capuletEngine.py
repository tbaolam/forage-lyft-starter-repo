# This class is one of the Engine subclasses. It has a method needs_service that returns True if the engine needs service.
from engine import Engine

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        # Add your logic here to determine if the engine needs service
        # The engine needs service every 30,000 miles
        return self.current_mileage - self.last_service_mileage >= 30000