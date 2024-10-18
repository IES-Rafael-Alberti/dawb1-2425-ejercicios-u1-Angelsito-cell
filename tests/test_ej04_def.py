import pytest 

from src.ej04_def2 import calculo

@pytest.mark.parametrize(

    "celsius, expected",
    [
        (6, "6.00 grados Celsius son 42.80 grados fahrenheit")
    ]
)


def test_horario(celsius,expected):
    assert calculo(celsius) == expected