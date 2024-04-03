import datetime


class Calendar:
    def get_year(self, in_year: int) -> int:
        if isinstance(in_year, int):
            year = in_year
            return year
        else:
            raise TypeError("Год может быть только integer")

    def get_month(self, in_month: int) -> int:
        if isinstance(in_month, int):
            month = in_month
            return month
        else:
            raise TypeError("Месяц может быть только  integer")

    def get_day(self, in_day: int) -> int:
        if isinstance(in_day, int):
            day = in_day
            return day
        else:
            raise TypeError("День может быть только integer")

