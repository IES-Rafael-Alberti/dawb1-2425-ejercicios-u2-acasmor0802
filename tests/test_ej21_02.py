import pytest
from src.condicionales.ej21_02 import comprobar_contraseña

@pytest.mark.parametrize(
    "intento, contraseña, expected",
    [
        ("password", "password", True),
        ("PASSWORD", "password", True),
        ("Password", "password", True),
        ("pass", "password", False),
        ("12345", "password", False),
        ("password123", "password", False),
    ]
)
def test_comprobar_contraseña(intento, contraseña, expected):
    assert comprobar_contraseña(intento, contraseña) == expected
