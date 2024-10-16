def calcular_importe_total(horas, coste_por_hora):
    return horas * coste_por_hora

def main():
    horas_trabajadas =float(input("Dime las horas trabajadas: "))
    coste_por_hora = float(input("Dime el coste por hora: "))
    importe_total = calcular_importe_total(horas_trabajadas, coste_por_hora)
    print(f"El importe total es: {importe_total}€")
    
if __name__ == "__main__":
    main()
