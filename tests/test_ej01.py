import pytest 
from src.ej01_def import saludar

def saludar():
    assert saludar("Caramela") == "Hola, Caramela!"
    assert saludar("Python") == "Hola, Python!"