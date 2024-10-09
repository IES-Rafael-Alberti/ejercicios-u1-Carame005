def calcula_precio(importe: float, iva: float) -> str:
    if iva < 0 or iva > 100:
        iva = 21.0  

    precio_final = importe * (1 + iva / 100)

    return f"El precio final del artículo con IVA ({iva:.2f}) es {precio_final:.2f}€."

def main():
    resultado = calcula_precio(100, 21)
    print(resultado)  

if __name__ == "__main__":
    main()