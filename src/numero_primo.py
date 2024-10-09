print('DETERMINADOR DE NUMEROS PRIMOS')
n=input('DIME UN NUMERO')
n=int(n)
primo=1
divisor=n-1
while(divisor>1):
    resto=n%divisor
    if(resto==0):
        print('ES DIVISIBLE ENTRE' , divisor)
        primo=0
    divisor=divisor-1
if(primo==1):
    print('ES PRIMO')
