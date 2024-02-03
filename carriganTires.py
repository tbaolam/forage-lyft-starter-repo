from tires import Tires

class CarriganTires(Tires):
    # Tire has  wear sensors produce an array of four numbers between 0 and 1 inclusive, representing how worn each of the tires are.
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self) -> bool:
        # Carrigan tires should be serviced only when one or more of the values in the tire wear array is greater than or equal to 0.9.
        for wear in self.wear_sensors:
            if wear >= 0.9:
                return True
        return False