v=int(input("Ingrese el numero de barras de pan vendidas no frescas")) 
p=3.49
nf=3.49*(60/100)
t=v*nf
print(f"La barra de pan normal cuesta {p},la no fresca tiene un descuento del 60% y el precio total a pagar de las barras de pan no frescas es {round(t)} euros")