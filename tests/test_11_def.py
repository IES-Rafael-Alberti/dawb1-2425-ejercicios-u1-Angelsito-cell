import pytest

from src.ej11_def import resultado

@pytest.mark.parametrize(
    "num, expected"
    [
        (4, "El resultado es: 12.5"),
    ]
)


def test_resultado(num, expected):
    assert resultado(num) == expected