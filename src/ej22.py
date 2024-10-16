frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

if len(vocal) != 1 or vocal.lower() not in 'aeiou':
    print("Por favor, introduce una sola vocal válida (a, e, i, o, u).")
else:
    frase_modificada = frase.replace(vocal, vocal.upper()).replace(vocal.upper(), vocal.upper())
    
    print("Frase modificada:", frase_modificada)
