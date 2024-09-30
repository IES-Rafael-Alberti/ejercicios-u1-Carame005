c=int(input("Ingrese la cantidad de dinero en la cuenta de ahorro"))
i=4
capital=c*(1+i/100)
print(f"El capital aumentado en {i}% durante un año es {round(capital)}")
capital=capital*(1+i/100)
print(f"El capital aumentado en {i}% durante dos años es {round(capital)}")
capital=capital*(1+i/100)
print(f"El capital aumentado en {i}% durante tres años es {round(capital)}")