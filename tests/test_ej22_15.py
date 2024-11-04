import pytest
from src.bucles.ej22_15 import suma

@pytest.mark.parametrize(
    "num, total, expected",
    [
        (5, 10, 15),
        (0, 0, 0),
        (-3, 5, 2),
        (10, 10, 20),
    ]
)
def test_suma(num, total, expected):
    assert suma(num, total) == expected