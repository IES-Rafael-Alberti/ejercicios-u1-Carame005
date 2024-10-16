def grados_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)




def main():
    entrada = input("Introduce la temperatura en grados Fahrenheit: ")
    fahrenheit = float(entrada)
    resultado = grados_celsius(fahrenheit)
    print(f"La temperatura en grados Celsius es: {resultado}")

if __name__ == "__main__":
    main()