def comparador(n1, n2):
    if n1 > n2:
        return n1 
    elif n1 < n2:
        return n2
    
def main():
    n1=int(input("Ingrese el primer número: "))
    n2=int(input("Ingrese el segundo número: "))
    print(comparador(n1, n2))

if __name__ == "__main__":
    main()