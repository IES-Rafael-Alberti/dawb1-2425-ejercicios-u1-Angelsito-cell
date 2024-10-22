import pytest
from src.prueba1 import mayor_numero


@pytest.mark.parametrize(

    "a, b, expected",
    [
        (5, 5, 0),
        (5, 6, 6)
    ]
)


def test_mayornum(a, b, expected):
    assert mayor_numero(a, b) == expected