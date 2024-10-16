def es_mayor_de_edad(edad):
    if edad<18:
        return False
    
def comprobar_edad(valor):
    int(valor)
    if valor <= 0:
        return False
def introducir_edad(msj):
    valor=input(msj)
    while not comprobar_edad(valor):
        print("Error: Debes introducir una edad válida.")
        valor = input(msj)
    return int(valor)
def main():
    edad=introducir_edad("Introduce tu edad")
    if es_mayor_de_edad(edad):
        print("Eres legal")
    else:
        print("No eres legal")
        
if __name__ == "__main__":
    main()