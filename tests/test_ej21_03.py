import pytest
from src.condicionales.ej21_03 import dividir

@pytest.mark.parametrize(
    "numero1, numero2, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (0, 1, 0),
        (1, 2, 0.5),
    ]
)
def test_dividir(numero1, numero2, expected):
    assert dividir(numero1, numero2) == expected
