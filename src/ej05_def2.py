def calcula_precio(importe: float, iva: float) -> str:
    if iva < 0 or iva > 100:
        iva = 21  
    precio_final = importe + (importe * iva / 100)
    return precio_final

def main():
    importe = float(input("Introduce el importe: "))
    iva = float(input("Introduce el porcentaje de IVA: "))
    resultado = calcula_precio(importe, iva)
    print(resultado)



if __name__ == "__main__":
    main()
