productos_str = input("Introduce los productos de la cesta de la compra, separados por comas: ")

productos = [producto.strip() for producto in productos_str.split(",")]

print("\nLos productos en tu cesta de la compra son:")
for producto in productos:
    print(producto)
