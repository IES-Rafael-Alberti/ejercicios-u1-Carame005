def convertir_temperatura():
    fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
    
    celsius = (fahrenheit - 32) * 5/9
    
    resultado = f"{celsius:.2f}ºC ({fahrenheit:.2f}ºF)"
    
    return resultado

temperatura_convertida = convertir_temperatura()
print(temperatura_convertida)
