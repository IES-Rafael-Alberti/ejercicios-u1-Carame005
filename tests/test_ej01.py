import pytest 
from src.ej01_def import saludar

def test_saludar():
    assert saludar("Caramela") == "¡Hola, Caramela! Espero que tengas un gran día."
    assert saludar("Python") == "¡Hola, Python! Espero que tengas un gran día."

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        ("Caramela", "¡Hola, Caramela! Espero que tengas un gran día."),
        ("Python", "¡Hola, Python! Espero que tengas un gran día."),
    ]
)
def test_saludar(input_n1, expected):
    assert saludar(input_n1) == expected