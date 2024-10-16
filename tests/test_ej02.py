import pytest 
from src.ej02_def import calcular_importe_total

def test_calcular_importe_total():
    assert calcular_importe_total(25,14) == 350.0
    assert calcular_importe_total(36,54) == 1944.0
    assert calcular_importe_total(46,18) == 828.0
    
    
@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (25, 14, 350.0),
        (36, 54, 1944.0),
        (46, 18, 828.0),
    ]
)
def test_calcular_importe_total(input_n1, input_n2, expected):
    assert calcular_importe_total(input_n1, input_n2) == expected