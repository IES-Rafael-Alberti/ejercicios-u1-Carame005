import pytest 
from src.ej02_def import calcular_importe_total

def calcular_importe_total():
    assert calcular_importe_total(10, 20, 30) == 60
    assert calcular_importe_total(15, 25, 35) == 75
    assert calcular_importe_total(5, 10, 15) == 30
    assert calcular_importe_total(20, 30, 40) == 90