n1=input("Dame tu nombre")
n2=int(input("Dame tu edad"))

if n2<0 or n2>125:
    print("Edad no válida")
    
else:
    print(f"Te llamas {n1} y tienes {n2} años")