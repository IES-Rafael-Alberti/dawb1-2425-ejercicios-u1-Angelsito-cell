import pytest

import sys
import os

# Agregar el directorio raíz del proyecto (practica6) al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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