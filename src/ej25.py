fecha_str = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")



dia, mes, anio = fecha_str.split("/")

dia = dia.zfill(2)  
mes = mes.zfill(2)  

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")