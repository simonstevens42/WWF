from abc import ABC, abstractmethod
from logger import *


class Vehicle(ABC):
    __vehicle_count = int = 0

    # constructor
    def __init__(self, model: str, price: float):
        if Vehicle.__vehicle_count < 100:
            self.__model = model
            self.__current_speed = 0
            self.__price = price
            Vehicle.__vehicle_count += 1
        else:
            log_msg("Maximum number of 100 vehicles reached!", "CRITICAL")
            raise RuntimeError("Maximum number of 100 vehicles reached!")

    # destructor
    def __del__(self):
        Vehicle.__vehicle_count -= 1
        log_msg("A vehicle has disappeared.", "INFO")

    # get and set methods
    def get_model(self) -> str:
        return self.__model

    def set_model(self, model: str) -> None:
        self.__model = model

    def get_current_speed(self) -> float:
        return self.__current_speed

    def set_current_speed(self, current_speed: float) -> None:
        self.__current_speed = current_speed

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @staticmethod
    def vehicle_count() -> int:
        return Vehicle.__vehicle_count


class Car(Vehicle):

    # constructor
    def __init__(self, model: str, price: float, door_count: int, fuel: str, ps: int):
        super().__init__(model, price)
        if 1 <= door_count <= 5:
            self.__door_count = door_count
        else:
            self.__door_count = 1
        self.__ps = ps
        if "gasoline" in fuel or "diesel" in fuel or "electric" in fuel:
            self.__fuel = fuel
        else:
            log_msg("No valid fuel has been selected.", "CRITICAL")
            raise ValueError("No valid fuel has been selected.")

    # get and set methods
    def get_door_count(self) -> int:
        return self.__door_count

    def set_door_count(self, door_count: int) -> None:
        self.__door_count = door_count

    def get_fuel(self) -> str:
        return self.__fuel

    def set_fuel(self, fuel: str) -> None:
        self.__fuel = fuel

    def get_ps(self) -> int:
        return self.__ps

    def set_ps(self, ps: int) -> None:
        self.__ps = ps

    # implementation of abstract methods
    def stop(self) -> None:
        self.set_current_speed(0)
        log_msg("Car engine stops.", "INFO")

    def start(self) -> None:
        log_msg("Car engine starts.", "INFO")

    # methods
    def accelerate(self, accelerate: float) -> None:
        new_current_speed = self.get_current_speed() + accelerate
        if new_current_speed < 200:
            self.set_current_speed(new_current_speed)
            log_msg(F"The car accelerates to {new_current_speed}km/h", "INFO")
        else:
            log_msg("The acceleration failed.", "WARNING")

    def decelerate(self, decelerate: float) -> None:
        new_current_speed = self.get_current_speed() - decelerate
        if new_current_speed >= 0:
            self.set_current_speed(new_current_speed)
            log_msg(F"The car decelerates to {new_current_speed}km/h", "INFO")
        else:
            log_msg("The deceleration failed.", "WARNING")

    @abstractmethod
    def eco_friendly(self):
        pass


class CombustionCar(Car):
    # constructor
    def __init__(self, model: str, price: float, door_count: int, fuel: str,
                 ps: int, usage_liter_km: float, tank_capacity: float):

        super().__init__(model, price, door_count, fuel, ps)
        self.__usage_liter_km = usage_liter_km
        self.__tank_capacity = tank_capacity
        self.__fuel_level = tank_capacity / 2

    # get and set methods
    def get_usage_liter_km(self) -> float:
        return self.__usage_liter_km

    def set_usage_liter_km(self, usage_liter_km: float) -> None:
        self.__usage_liter_km = usage_liter_km

    def get_tank_capacity(self) -> float:
        return self.__tank_capacity

    def set_tank_capacity(self, tank_capacity) -> None:
        self.__tank_capacity = tank_capacity

    def get_fuel_level(self) -> float:
        return self.__fuel_level

    def set_fuel_level(self, fuel_level) -> None:
        self.__fuel_level = fuel_level

    # implementation of abstract methods
    def eco_friendly(self) -> None:
        log_msg(F"{self.get_fuel()} engines have a poor environmental balance.", "INFO")

    # methods
    def refuel(self, fuel: float) -> None:
        combined_fuel = self.get_fuel_level() + fuel
        if combined_fuel <= self.get_tank_capacity():
            self.set_fuel_level(combined_fuel)
            log_msg("Successful refueling.", "INFO")
        else:
            log_msg("You can't overfill your tank.", "WARNING")


class ElectricCar(Car):
    # constructor
    def __init__(self, model: str, price: float, door_count: int, fuel: str,
                 ps: int, usage_kwh_km: float, battery_capacity: float):

        super().__init__(model, price, door_count, fuel, ps)
        self.__usage_kwh_km = usage_kwh_km
        self.__battery_capacity = battery_capacity
        self.__battery_level = battery_capacity / 2

    # get and set methods
    def get_usage_kwh_km(self) -> float:
        return self.__usage_kwh_km

    def set_usage_kwh_km(self, usage_kwh_km) -> None:
        self.__usage_kwh_km = usage_kwh_km

    def get_battery_capacity(self) -> float:
        return self.__battery_capacity

    def set_battery_capacity(self, battery_capacity: float) -> None:
        self.__battery_capacity = battery_capacity

    def get_battery_level(self) -> float:
        return self.__battery_level

    def set_battery_level(self, battery_level: float) -> None:
        self.__battery_level = battery_level

    # implementation of abstract methods
    def eco_friendly(self) -> None:
        log_msg(F"{self.get_fuel()} engines have a good environmental balance.", "INFO")

    # methods
    def recharge(self, plug: str, mode: int, charge: float) -> None:
        combined_charge = self.get_battery_level() + charge
        if "Type-1" in plug or "Type-2" in plug or "CCS" in plug or "CHAdeMO" in plug:
            if 0 < mode < 5:
                if combined_charge <= self.get_battery_capacity():
                    self.set_battery_level(combined_charge)
                    log_msg("Successfully charged", "INFO")
                else:
                    log_msg("You can't overload your battery.", "WARNING")
            else:
                log_msg("No valid charging mode.", "WARNING")
        else:
            log_msg("No valid plug.", "WARNING")


class Bicycle(Vehicle):
    # constructor
    def __int__(self, model: str, price: float):
        super().__init__(model, price)

    # implementation of abstract methods
    def stop(self) -> None:
        self.set_current_speed(0)
        log_msg("Bicycle engine stops.", "INFO")

    def start(self) -> None:
        log_msg("Bicycle engine starts.", "INFO")

    # methods
    @staticmethod
    def ring(time: int) -> None:
        i = 0
        while i < time:
            log_msg("RING RING RING", "INFO")
            i += 1
