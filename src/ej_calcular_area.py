import math

def tiene_mas_de_un_punto(valor: str):
    pos_punto=valor.find(".")
    if pos_punto>= 0 and valor.find(".",pos_punto+1):
        return False
    else:
        return True
    
def contiene_solo_digitos_y_punto(valor: str):
    for i in range(len(valor)): # 0..len(valor) - 1:
        if not (valor[i].isdigit() or valor[1] == "."):
            return False
    return True


def comprobar_numero(valor: str):
    if valor[:1] == "-":
        valor = valor[1:]
        if len(valor) == 0:
            return False

    if tiene_mas_de_un_punto(valor):
        return False
    
    return contiene_solo_digitos_y_punto(valor)




def calcular_area(lado_a, lado_b, lado_c):
    semiperimetro = (lado_a + lado_b + lado_c) / 2
    area=math.sqrt(semiperimetro * (semiperimetro - lado_a) * (semiperimetro - lado_b) * (semiperimetro - lado_c))
    return area


def dame_numero(msj:str):
    num = (input(msj)).strip()
    while comprobar_numero(num) == False:
        print("Error: Debes introducir un número válido.")
        num = float(input(msj)).strip()
    return float(num)

def main():
    print("Introduce los lados del triángulo:")
    
    lado_a = dame_numero("Lado A: ")
    lado_b = dame_numero("Lado B: ")
    lado_c = dame_numero("Lado C: ")
    
    area=calcular_area(lado_a, lado_b, lado_c)
    print(f"El área del triángulo es: {area:.2f}")

if __name__ == "__main__":
    main()