import pytest
from src.ej11_def import procesar_numero

def test_procesar_numero():
    assert procesar_numero(10) == 100
    assert procesar_numero(20) == 40
    assert procesar_numero(30) == 900
    assert procesar_numero(40) == 1600
    
@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (10, 100),
        (20, 400),
        (30, 900),
        (40, 1600)
    ]
)
def test_procesar_numero(input_n1, expected):
    assert procesar_numero(input_n1) == expected