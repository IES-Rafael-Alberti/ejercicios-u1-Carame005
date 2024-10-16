import pytest 
from src.ej04_def2 import grados_celsius

def test_grados_celsius():
    assert grados_celsius(69) == 20.56
    assert grados_celsius(48) == 8.89
    assert grados_celsius(777) == 413.89
    assert grados_celsius(16) == -8.89
    

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (69, 20.56),
        (48, 8.89),
        (777, 413.89),
        (16, -8.89)
    ]
)
def test_grados_celsius(input_n1, expected):
    assert grados_celsius(input_n1) == expected