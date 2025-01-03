from abc import ABC, abstractmethod
import logging
from colorama import Fore, Style

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_info(message: str, highlight: str = "") -> None:
    """Logs an info-level message with optional highlighted text."""
    if highlight:
        message = message.replace(
            highlight, Fore.YELLOW + highlight + Style.RESET_ALL
        )
    logger.info(Fore.GREEN + message + Style.RESET_ALL)


# Abstract class Vehicle
class Vehicle(ABC):
    """
    Abstract base class representing a generic vehicle.
    Contains the common attributes make, model, and region_spec, and an
    abstract method start_engine.
    """

    def __init__(self, make: str, model: str, region_spec: str):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self) -> None:
        """Abstract method to start the engine."""
        pass


# Class Car inheriting from Vehicle
class Car(Vehicle):
    """
    Represents a car. Implements the start_engine method to simulate
    starting the engine.
    """

    def start_engine(self) -> None:
        log_info(
            f"{self.make} {self.model} ({self.region_spec}):"
            f" Engine started",
            "Engine started",
        )


# Class Motorcycle inheriting from Vehicle
class Motorcycle(Vehicle):
    """
    Represents a motorcycle. Implements the start_engine method to
    simulate starting the motor.
    """

    def start_engine(self) -> None:
        log_info(
            f"{self.make} {self.model} ({self.region_spec}): "
            f"Motor started",
            "Motor started",
        )


# Abstract class VehicleFactory
class VehicleFactory(ABC):
    """
    Abstract factory class for creating vehicles. Defines methods to
    create cars and motorcycles.
    """

    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        """Abstract method to create a car."""
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        """Abstract method to create a motorcycle."""
        pass


# Factory class for US vehicles
class USVehicleFactory(VehicleFactory):
    """
    Concrete factory for creating vehicles with US specifications.
    """

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US Spec")


# Factory class for EU vehicles
class EUVehicleFactory(VehicleFactory):
    """
    Concrete factory for creating vehicles with EU specifications.
    """

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU Spec")


# Usage example
if __name__ == "__main__":
    # Create a factory for US vehicles
    us_factory = USVehicleFactory()
    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    vehicle2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()

    # Create a factory for EU vehicles
    eu_factory = EUVehicleFactory()
    vehicle3 = eu_factory.create_car("Volkswagen", "Golf")
    vehicle3.start_engine()

    vehicle4 = eu_factory.create_motorcycle("BMW", "R1250")
    vehicle4.start_engine()
