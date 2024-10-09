import pytest 
from src.ej04_def2 import grados_celsius

def grados_celsius():
    assert grados_celsius(0) == -273.15
    assert grados_celsius(100) == 37.77777777777778
    assert grados_celsius(212) == 100.0
    assert grados_celsius(-459.67) == -233.15