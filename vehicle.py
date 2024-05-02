from abc import ABC, abstractmethod
from logger import *


class Vehicle(ABC):
    __vehicle_count = int = 0

    # constructor
    def __init__(self, model, price):
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
    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_current_speed(self):
        return self.__current_speed

    def set_current_speed(self, current_speed):
        self.__current_speed = current_speed

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @staticmethod
    def vehicle_count():
        return Vehicle.__vehicle_count


class Car(Vehicle):

    # constructor
    def __init__(self, model, price, door_count, fuel, ps):
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
    def get_door_count(self):
        return self.__door_count

    def set_door_count(self, door_count):
        self.__door_count = door_count

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self, fuel):
        self.__fuel = fuel

    def get_ps(self):
        return self.__ps

    def set_ps(self, ps):
        self.__ps = ps

    # implementation of abstract methods
    def stop(self):
        self.set_current_speed(0)
        log_msg("Car engine stops.", "INFO")

    def start(self):
        log_msg("Car engine starts.", "INFO")

    # methods
    def accelerate(self, accelerate):
        new_current_speed = self.get_current_speed() + accelerate
        if new_current_speed < 200:
            self.set_current_speed(new_current_speed)
            log_msg(F"The car accelerates to {new_current_speed}km/h", "INFO")
        else:
            log_msg("The acceleration failed.", "WARNING")

    def decelerate(self, decelerate):
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
    def __init__(self, model, price, door_count, fuel, ps, usage_liter_km, tank_capacity):
        super().__init__(model, price, door_count, fuel, ps)
        self.__usage_liter_km = usage_liter_km
        self.__tank_capacity = tank_capacity
        self.__fuel_level = tank_capacity / 2

    # get and set methods
    def get_usage_liter_km(self):
        return self.__usage_liter_km

    def set_usage_liter_km(self, usage_liter_km):
        self.__usage_liter_km = usage_liter_km

    def get_tank_capacity(self):
        return self.__tank_capacity

    def set_tank_capacity(self, tank_capacity):
        self.__tank_capacity = tank_capacity

    def get_fuel_level(self):
        return self.__fuel_level

    def set_fuel_level(self, fuel_level):
        self.__fuel_level = fuel_level

    # implementation of abstract methods
    def eco_friendly(self):
        log_msg(F"{self.get_fuel()} engines have a poor environmental balance.", "INFO")

    # methods
    def refuel(self, fuel):
        combined_fuel = self.get_fuel_level() + fuel
        if combined_fuel <= self.get_tank_capacity():
            self.set_fuel_level(combined_fuel)
            log_msg("Successful refueling.", "INFO")
        else:
            log_msg("You can't overfill your tank.", "WARNING")


class ElectricCar(Car):
    # constructor
    def __init__(self, model, price, door_count, fuel, ps, usage_kwh_km, battery_capacity):
        super().__init__(model, price, door_count, fuel, ps)
        self.__usage_kwh_km = usage_kwh_km
        self.__battery_capacity = battery_capacity
        self.__battery_level = battery_capacity / 2

    # get and set methods
    def get_usage_kwh_km(self):
        return self.__usage_kwh_km

    def set_usage_kwh_km(self, usage_kwh_km):
        self.__usage_kwh_km = usage_kwh_km

    def get_battery_capacity(self):
        return self.__battery_capacity

    def set_battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity

    def get_battery_level(self):
        return self.__battery_level

    def set_battery_level(self, battery_level):
        self.__battery_level = battery_level

    # implementation of abstract methods
    def eco_friendly(self):
        log_msg(F"{self.get_fuel()} engines have a good environmental balance.", "INFO")

    # methods
    def recharge(self, plug, mode, charge):
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
    def __int__(self, model, price):
        super().__init__(model, price)

    # implementation of abstract methods
    def stop(self):
        self.set_current_speed(0)
        log_msg("Bicycle engine stops.", "INFO")

    def start(self):
        log_msg("Bicycle engine starts.", "INFO")

    # methods
    @staticmethod
    def ring(time: int):
        i = 0
        while i < time:
            log_msg("RING RING RING", "INFO")
            i += 1
