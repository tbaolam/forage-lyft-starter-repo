# this is an abstract battery class that has a needs_service method:
class Battery:
    def needs_service(self) -> bool:
        raise NotImplementedError("Subclasses should implement this!")