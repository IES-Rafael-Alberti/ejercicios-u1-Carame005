nombre_producto = input("Introduce el nombre del producto: ")

precio_str = input("Introduce el precio del producto (en euros): ")

unidades_str = input("Introduce el número de unidades: ")

precio = float(precio_str)
unidades = int(unidades_str)

coste_total = precio * unidades

print(f"{nombre_producto: <30} {precio: >6.2f} € x {unidades: >3} unidades = {coste_total: >8.2f} €")


