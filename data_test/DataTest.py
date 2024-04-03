from dataclasses import dataclass


@dataclass
class TestCase:
    year: int
    month: int
    day: int

@dataclass
class PositiveTestCase(TestCase):
    pass

@dataclass
class NegativeTestCase(TestCase):
    pass