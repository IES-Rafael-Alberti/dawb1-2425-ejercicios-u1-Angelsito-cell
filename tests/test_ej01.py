import pytest
from src.ej01_def import saludo

@pytest.mark.parametrize(

    "nombre, expected",
    [
        ("Pepe", "Hola, Pepe."),
        ("888", "Hola, 888."),
        ("Ingeniero Petroquímico", "Hola, Ingeniero Petroquímico.")
    ]
)

def test_saludar(nombre, expected): 
    assert saludo(nombre) == expected