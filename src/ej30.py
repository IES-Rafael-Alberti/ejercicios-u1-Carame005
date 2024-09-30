n1 = int(input("Dame un número: "))
n2 = int(input("Dame un incremento: "))
n3 = int(input("Dame el último número de la serie: "))

if n2 <= 0 or n3 <= 0:
    print("Error: los valores deben ser positivos")
else:
    serie = []  # 
    while n1 <= n3:  
        serie.append(str(n1))  
        n1 += n2  
    resultado = "-".join(serie)  
    print("SERIE =>", resultado) 
