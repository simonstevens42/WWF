import datetime
from logger import log_msg


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

    # methods
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


class Human(Mammal):
    __id_count: int = 0

    # constructor
    def __init__(self, name: str, birthdate: datetime, weight: float, race: str, info: str):
        super().__init__(name, birthdate, weight, race, info)
        self.__id = Human.__id_count
        Human.__id_count += 1

    # methods
    @staticmethod
    def get_id_count() -> int:
        return Human.__id_count


class Staff:
    __staff_id_count: int = 0

    # constructor
    def __init__(self, human: Human, job: str):
        self.__human = human
        self.__job = job
        self.__appointments = []
        Staff.__staff_id_count += 1
        self.__staff_id = Staff.__staff_id_count

    # get and set Methods
    def get_human(self) -> Human:
        return self.__human

    def set_human(self, human: Human) -> None:
        self.__human = human

    def get_job(self) -> str:
        return self.__job

    def set_job(self, job: str) -> None:
        self.__job = job

    def get_appointments(self) -> list:
        return self.__appointments

    def set_appointments(self, appointment) -> None:
        self.__appointments.append(appointment)

    def get_staff_id(self) -> int:
        return self.__staff_id

    def set_staff_id(self, staff_id) -> None:
        self.__staff_id = staff_id

    # methods
    @staticmethod
    def alert(participants: list, event: str) -> None:
        for participant in participants:
            log_msg(F"[!]Reminder for {event} for {participant.get_name()}[!]", "INFO")

    @staticmethod
    def get_staff_id_count() -> int:
        return Staff.__staff_id_count
