import pytest
from src.bucles.ej22_19 import comprobar

@pytest.mark.parametrize(
    "opcion, expected",
    [
        (1, True),
        (2, True),
        (3, True),
        (0, False),
        (4, False),
        (-1, False),
    ]
)
def test_comprobar(opcion, expected):
    assert comprobar(opcion) == expected