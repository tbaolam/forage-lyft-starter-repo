# This an absrtact class for the engine of the Car. It has a method needs_service that returns True if the engine needs service.

class Engine:
    def needs_service(self):
        raise NotImplementedError("Subclasses should implement this!")