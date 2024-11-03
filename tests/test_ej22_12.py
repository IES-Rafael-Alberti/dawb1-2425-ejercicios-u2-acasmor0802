import pytest
from src.bucles.ej22_12 import comprobacion

@pytest.mark.parametrize(
    "letra, frase, expected",
    [
        ("a", "banana", 3),
        ("b", "banana", 1),
        ("n", "banana", 2),
        ("z", "banana", 0),
        (" ", "a b c", 2),
    ]
)
def test_comprobacion(letra, frase, expected):
    assert comprobacion(letra, frase) == expected
