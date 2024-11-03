import pytest
from src.captura_de_excepciones.ej23_02 import generar_imp

@pytest.mark.parametrize(
    "numero, expected",
    [
        (1, ["1"]),
        (2, ["1"]),
        (5, ["1", "3", "5"]),
        (10, ["1", "3", "5", "7", "9"]),
        (0, []),
    ]
)
def test_generar_imp(numero, expected):
    assert generar_imp(numero) == expected