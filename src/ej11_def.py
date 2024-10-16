def procesar_numero(numero)-> int:
    resultado = numero ** 2
    return resultado

def main():
    numero_ingresado = int(input("Ingrese un número: "))
    resultado = procesar_numero(numero_ingresado)
    print(resultado)

if __name__ == "__main__":
    main()