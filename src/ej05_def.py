def calcular_importe_con_iva(importe_sin_iva, tipo_iva):
    importe_con_iva = importe_sin_iva * (1 + tipo_iva / 100)
    
    print(f"Importe sin IVA: {importe_sin_iva:.2f}€")
    print(f"Tipo de IVA: {tipo_iva}%")
    print(f"Importe total con IVA: {importe_con_iva:.2f}€")

importe = int(input("Introduce el importe sin IVA: ")) 
tipo_iva = 21  
calcular_importe_con_iva(importe, tipo_iva)
