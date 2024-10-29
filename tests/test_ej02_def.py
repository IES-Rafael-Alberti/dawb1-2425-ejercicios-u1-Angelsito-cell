import pytest
from src.ej02_def import horario


@pytest.mark.parametrize(

    "h, c, expected",
    [
        (1, 2, "Importe total: 2 €")
    ]
)


def test_horario(h,c,expected):
    assert horario(h, c) == expected