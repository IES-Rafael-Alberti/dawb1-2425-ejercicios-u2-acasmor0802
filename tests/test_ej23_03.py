import pytest
from src.excepciones.ej23_03 import cuenta_atras

@pytest.mark.parametrize(
    "numero, expected",
    [
        (5, ["5", "4", "3", "2", "1", "0"]),
        (3, ["3", "2", "1", "0"]),
        (0, ["0"]),
        (10, ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]),
    ]
)
def test_cuenta_atras(numero, expected):
    assert cuenta_atras(numero) == expected
