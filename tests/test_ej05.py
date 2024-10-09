import pytest 
from src.ej05_def2 import calcula_precio

def calcula_precio():
    assert calcula_precio
    assert calcula_precio(10, 2, 1, 2, 1, 1) == 10.5
    assert calcula_precio( -10, 2, 1, 2, 1, 1) == "Error: Cantidad de productos negativa"
    assert calcula_precio(10, 21, 1, 2, 1, 1) == "Error: IVA fuera de rango (0-100)"