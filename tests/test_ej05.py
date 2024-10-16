import pytest 
from src.ej05_def2 import calcula_precio

def test_calcula_precio():
    assert calcula_precio(18, 14) == 20.52
    assert calcula_precio(28, 49) == 41.72
    assert calcula_precio(10, 21) == 12.10
    

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (18, 14, 20.52),
        (28, 49, 41.72),
        (10, 21, 12.10),
    ]
)
def test_calcula_precio(input_n1, input_n2, expected):
    assert calcula_precio(input_n1, input_n2) == expected