def saludar(nombre):
    return f"¡Hola, {nombre}! Espero que tengas un gran día."

def main():
    n=input("Dime tu nombre: ")
    resultado = saludar(n)
    print(resultado)
    
if __name__ == "__main__":
    main()
