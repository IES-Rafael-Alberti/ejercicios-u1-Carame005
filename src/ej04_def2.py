def grados_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)

def main():
    resultado = grados_celsius(100.00)
    print(resultado)  # Debería imprimir 37.78

if __name__ == "__main__":
    main()