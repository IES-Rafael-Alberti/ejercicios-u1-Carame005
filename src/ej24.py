precio_str = input("Introduce el precio del producto en euros (con dos decimales): ")


precio = float(precio_str)
    
if precio < 0:
    print("El precio no puede ser negativo.")
else:
    euros = int(precio)  
    centimos = int(round((precio - euros) * 100)) 
    
    print(f"Número de euros: {euros}")
    print(f"Número de céntimos: {centimos}")
