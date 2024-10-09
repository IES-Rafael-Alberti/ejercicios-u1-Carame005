import pytest 
from src.prueba1 import comparador

def test_comparador():

    assert comparador(5, 7) == -1
    assert comparador(7, 5) == 1
    assert comparador(5, 5) == 0
    assert comparador(10, 5) == 5
    assert comparador(5, 10) == -5
    assert comparador("5", 7) == "Error: ambos valores deben ser numéricos"
    assert comparador(5, "7") == "Error: ambos valores deben ser numéricos"
    assert comparador("5", "7") == "Error: ambos valores deben ser numéricos"
    assert comparador(5.5, 7) == "Error: ambos valores deben ser numéricos"
    assert comparador(5, 7.5) == "Error: ambos valores deben ser numéricos"