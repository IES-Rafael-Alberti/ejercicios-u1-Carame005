correo = input("Introduce tu correo electrónico: ")
if "@" in correo:
    nombre, _ = correo.split("@", 1)
    nuevo_correo = f"{nombre}@ceu.es"
    print("Tu nuevo correo es:", nuevo_correo)
else:
    print("Por favor, introduce un correo electrónico válido.")
