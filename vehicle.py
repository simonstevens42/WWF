from abc import abstractmethod


class Vehicle:
    type_name: str
    current_speed = float
    __vehicle_count = int = 0

    # constructor
    def __init__(self, type_name):
        if Vehicle.__vehicle_count < 100:
            self.__type_name = type_name
            self.__current_speed = 0
            Vehicle.__vehicle_count += 1
        else:
            raise RuntimeError("Maximum number of 100 vehicles reached!")

    # destructor
    def __del__(self):
        Vehicle.__vehicle_count -= 1
        print("A vehicle has disappeared.")

    # get and set methods
    def get_type_name(self):
        return self.__type_name

    def set_type_name(self, type_name):
        self.__type_name = type_name

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
    door_count: int

    # constructor
    def __init__(self, type_name, door_count):
        super().__init__(type_name)
        if 1 <= door_count <= 5:
            self.__door_count = door_count
        else:
            self.__door_count = 1

    # get and set methods
    def get_door_count(self):
        return self.__door_count

    def set_door_count(self, door_count):
        self.__door_count = door_count

    # implementation of abstract methods
    def stop(self):
        self.set_current_speed(0)
        print("Car engine stops.")

    def start(self):
        print("Car engine starts.")

    # methods
    def accelerate(self, accelerate):
        new_current_speed = self.get_current_speed() + accelerate
        if new_current_speed < 200:
            self.set_current_speed(new_current_speed)
            print(f"The car accelerates to {new_current_speed}km/h")
        else:
            print("The acceleration failed.")

    def decelerate(self, decelerate):
        new_current_speed = self.get_current_speed() - decelerate
        if new_current_speed >= 0:
            self.set_current_speed(new_current_speed)
            print(f"The car decelerates to {new_current_speed}km/h")
        else:
            print("The deceleration failed.")


class Bicycle(Vehicle):
    # constructor
    def __int__(self, type_name):
        super().__init__(type_name)

    # implementation of abstract methods
    def stop(self):
        self.set_current_speed(0)
        print("Bicycle engine stops.")

    def start(self):
        print("Bicycle engine starts.")

    # methods
    @staticmethod
    def ring(time: int):
        i = 0
        while i < time:
            print("RING RING RING")
            i += 1
