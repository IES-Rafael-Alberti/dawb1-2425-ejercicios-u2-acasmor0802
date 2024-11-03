import pytest
from src.bucles.ej22_11 import reverir

@pytest.mark.parametrize(
    "palabra, expected",
    [
        ("hola", "aloh"),
        ("Python", "nohtyP"),
        ("12345", "54321")
    ]
)
def test_reverir(palabra, expected):
    assert reverir(palabra) == expected
