def fibonacci_hasta(n):
    serie = []
    a, b = 0, 1
    while a <= n:
        serie.append(a)
        a, b = b, a + b
    return serie

numero = int(input("Ingrese un número: "))
print(fibonacci_hasta(numero))
