n1=int(input("Dime un  numero "))
n2=int(input("Dime otro numero "))
if n1>n2:
    n=n1-n2
    print(f"{n2} es el menor y entre ellos hay {n} numeros")
else:
    if n2>n1:
        n=n2-n1
    print(f"{n1} es el menor y entre ellos hay {n} numeros")