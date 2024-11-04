import pytest
from src.condicionales.ej21_01 import mostrar_anios_cumplidos

@pytest.mark.parametrize(
    "edad, expected",
    [
        (17, "No eres mayor de edad"),
        (18, "Eres mayor de edad"),
        (20, "Eres mayor de edad"),
        (15, "No eres mayor de edad"),
        (30, "Eres mayor de edad"),
    ]
)
def test_mostrar_anios_cumplidos(edad, expected):
    assert mostrar_anios_cumplidos(edad) == expected
