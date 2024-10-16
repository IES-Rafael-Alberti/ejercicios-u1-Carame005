import pytest 
from src.prueba1 import comparador

def test_comparador():

    assert comparador(5, 7) == 7 
    assert comparador(14, 5) == 14
    assert comparador(5, 4) == 5
    assert comparador(10, 5) == 10
    assert comparador(5, 9) == 9

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (5, 7, 7),
        (14, 5, 14),
        (5, 4, 5),
        (10, 5, 10),
        (5, 9, 9),
    ]
)
def test_comparador(input_n1, input_n2, expected):
    assert comparador(input_n1, input_n2) == expected