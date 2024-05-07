import datetime
from mammal import Human, Staff
from logger import log_msg


class Appointment:

    # constructor
    def __init__(self, date: datetime, name: str, participants: list = None):
        self.__date = date
        self.__name = name
        if participants is None:
            self.__participants = []
        else:
            self.__participants = participants

    # get and set methods
    def get_date(self) -> datetime:
        return self.__date

    def set_date(self, date: datetime) -> None:
        self.__date = date

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_participants(self) -> list:
        return self.__participants

    def set_participants(self, participants: list) -> None:
        self.__participants = participants

    # methods
    def add_participant(self, participant: Human) -> None:
        self.__participants.append(participant)
        log_msg("New participant added.", "INFO")

    def inform_participants(self) -> None:
        log_msg("Alert participants", "INFO")
        Staff.alert(self.__participants, self.__name)
