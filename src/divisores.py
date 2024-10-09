def divisores(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def main():
    numero = int(input("Ingrese un número: "))
    print(divisores(numero))

if __name__ == "__main__":
    main()
