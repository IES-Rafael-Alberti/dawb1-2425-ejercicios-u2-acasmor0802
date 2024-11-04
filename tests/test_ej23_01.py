import pytest
from src.excepciones.ej23_01 import mostrar_anios

@pytest.mark.parametrize(
    "anios, expected",
    [
        (["1", "2", "3"], "1, 2, 3"),
        (["10", "20"], "10, 20"),
        ([], ""),
        (["2020", "2021", "2022"], "2020, 2021, 2022"),
    ]
)
def test_mostrar_anios(anios, expected):
    assert mostrar_anios(anios) == expected
