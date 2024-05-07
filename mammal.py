from logger import *
import datetime


class Mammal:

    # constructor
    def __init__(self, name: str, birthdate: datetime, weight: float, race: str, info: str):
        self.__name = name
        self.__birthdate = birthdate

        if weight >= 0:
            self.__weight = weight
        else:
            self.__weight = 0

        self.__race = race
        self.__info = info

    # get and set methods
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name) -> None:
        self.__name = name

    def get_birthdate(self) -> datetime:
        return self.__birthdate

    def set_birthdate(self, birthdate) -> None:
        self.__birthdate = birthdate

    def get_weight(self) -> float:
        return self.__weight

    def set_weight(self, weight) -> None:
        self.__weight = weight

    def get_race(self) -> str:
        return self.__race

    def set_race(self, race) -> None:
        self.__race = race

    def get_info(self) -> str:
        return self.__info

    def set_info(self, info) -> None:
        self.__info = info

    def get_age(self) -> int:
        today = datetime.date.today()
        year = today.year - self.__birthdate.year
        age = year - ((today.month, today.day) < (self.__birthdate.month, self.__birthdate.day))
        return age

    # shows all attributs without race and info
    def show_data(self) -> str:
        return F"- Name:{self.__name}\n- Birthdate:{self.__birthdate} ({self.get_age()})\n- Weight:{self.__weight}"


class Dog(Mammal):
    __dog_count: int = 0

    # constructor
    def __init__(self, name: str, birthdate: datetime, weight: float, race: str, info: str):
        super().__init__(name, birthdate, weight, race, info)
        Dog.__dog_count += 1

    # destructor
    def __del__(self):
        Dog.__dog_count -= 1
        log_msg("A dog died.", "INFO")

    @staticmethod
    def get_dog_population() -> int:
        return Dog.__dog_count


class Cat(Mammal):
    __cat_count: int = 0

    # constructor
    def __init__(self, name: str, birthdate: datetime, weight: float, race: str, info: str):
        super().__init__(name, birthdate, weight, race, info)
        Cat.__cat_count += 1

    # destructor
    def __del__(self):
        Cat.__cat_count -= 1
        log_msg("A cat died.", "INFO")

    @staticmethod
    def get_cat_population() -> int:
        return Cat.__cat_count
