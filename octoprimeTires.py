from tires import Tires

class Octoprimes(Tires):
    # Tire has  wear sensors produce an array of four numbers between 0 and 1 inclusive, representing how worn each of the tires are.
    def __init__(self, wear_sensors):
        self.wear_sensors = wear_sensors

    def needs_service(self) -> bool:
        # Octoprime tires should be serviced only when the sum of all values in the tire wear array is greater than or equal to 3.
        if sum(self.wear_sensors) >= 3:
            return True
        return False