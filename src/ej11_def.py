def procesar_numero(numero):
    resultado = numero ** 2
    return f"El cuadrado de {numero} es {resultado}."

numero_ingresado = int(input("Ingrese un número: "))
resultado = procesar_numero(numero_ingresado)
print(resultado)
