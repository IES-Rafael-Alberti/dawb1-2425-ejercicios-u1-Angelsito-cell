import pytest
from src.prueba1 import mayor_numero

@pytest.mark.parametrize(

    "a, b, expected"
    [
        (5, 6, "El número mayor es: 6")
    ]
)


def test_mayornum(a, b,expected):
    assert mayor_numero(a, b) == expected