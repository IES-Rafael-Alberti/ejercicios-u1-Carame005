import pytest
from src.ej11_def import procesar_numero

def procesar_numero():
    assert procesar_numero
    assert procesar_numero(10) == (10, 2, 5)
    assert procesar_numero(20) == (20, 4, 5)
    assert procesar_numero(30) == (30, 6, 5)
    assert procesar_numero(40) == (40, 8, 5)