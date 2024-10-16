def comprobar_entero(cadena:str)-> bool:
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith('-') and cadena[1:].isdigit())

def dar_entero()-> int:
    cadena=input("Ingrese un número entero: ")
    comprobar_entero(cadena)
    while not comprobar_entero(cadena):
        cadena=input("\n***Error***\n\nDame un número entero")
        
        return int(cadena)  

def main():
    n=dar_entero()
    print(f"Has introducido el número:{n} ")

if __name__ == "__main__":
    main()