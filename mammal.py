import datetime


class Mammal:
    name: str
    birthdate: datetime
    weight: float
    race: str
    info: str

    # constructor
    def __init__(self, name, birthdate, weight, race, info):
        self.__name = name
        self.__birthdate = birthdate

        if weight >= 0:
            self.__weight = weight
        else:
            self.__weight = 0

        self.__race = race
        self.__info = info

    # get and set methods
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_birthdate(self):
        return self.__birthdate

    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_race(self):
        return self.__race

    def set_race(self, race):
        self.__race = race

    def get_info(self):
        return self.__info

    def set_info(self, info):
        self.__info = info

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.__birthdate.year - ((today.month, today.day) < (self.__birthdate.month, self.__birthdate.day))
        return age

    # shows all attributs without race and info
    def show_data(self):
        return f"- Name:{self.__name}\n- Birthdate:{self.__birthdate} ({self.get_age()})\n- Weight:{self.__weight}"


class Dog(Mammal):
    _dog_count: int = 0

    # constructor
    def __init__(self, name, birthdate, weight, race, info):
        super().__init__(name, birthdate, weight, race, info)
        Dog._dog_count += 1

    # destructor
    def __del__(self):
        Dog._dog_count -= 1
        print("A dog died.")

    @staticmethod
    def get_dog_population():
        return Dog._dog_count


class Cat(Mammal):
    _cat_count: int = 0

    # constructor
    def __init__(self, name, birthdate, weight, race, info):
        super().__init__(name, birthdate, weight, race, info)
        Cat._cat_count += 1

    # destructor
    def __del__(self):
        Cat._cat_count -= 1
        print("A cat died.")

    @staticmethod
    def get_cat_population():
        return Cat._cat_count
