import pytest
from Calendar import Calendar  # Предположим, что ваш класс находится в модуле calendar_module
from data_test.DataTest import PositiveTestCase, NegativeTestCase


@pytest.fixture
def calendar():
    return Calendar()

class TestExceptionEmpty():
    def test_get_year_without_date(calendar):
        # Проверяем, что вызов метода get_year() без предварительной установки даты вызывает исключение
        with pytest.raises(Exception):
            calendar.get_year()

    def test_get_month_without_date(calendar):
        # Проверяем, что вызов метода get_month() без предварительной установки даты вызывает исключение
        with pytest.raises(Exception):
            calendar.get_month()

    def test_get_day_without_date(calendar):
        # Проверяем, что вызов метода get_day() без предварительной установки даты вызывает исключение
        with pytest.raises(Exception):
            calendar.get_day()


@pytest.mark.parametrize("test_case", [

    PositiveTestCase(year=1, month=1, day=1),  # Минимальные значения
    PositiveTestCase(year=999, month=12, day=31),  # Максимальные значения
    PositiveTestCase(year=2023, month=2, day=28),  # Не високосный год, февраль
    PositiveTestCase(year=2024, month=2, day=29),  # Високосный год, февраль
    NegativeTestCase(year=2.3, month=10, day=31),  # Некорректный тип данных для года
    NegativeTestCase(year=2024, month=13, day=32),  # Некорректный месяц и день - для работы нужна логика на даты у класса Calendar
    NegativeTestCase(year='sdsd', month='sdsd', day='sdsd'),  # Некорректный тип данных
                                                          ])
def test_calendar_methods(calendar, test_case):
    if isinstance(test_case, PositiveTestCase):
        year = calendar.get_year(test_case.year)
        month = calendar.get_month(test_case.month)
        day = calendar.get_day(test_case.day)
        assert year == test_case.year
        assert month == test_case.month
        assert day == test_case.day
    elif isinstance(test_case, NegativeTestCase):
        with pytest.raises(TypeError):
            calendar.get_year(test_case.year)
            calendar.get_month(test_case.month)
            calendar.get_day(test_case.day)