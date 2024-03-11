n1=input("Número 1? ")
n2=input("Número 2? ")
d=float(n1)/float(n2)
e=float(n1)//float(n2)
if d-e==0:
    print(str(n1)+" es múltiplo de "+str(n2))
else:
    print(str(n1)+" no es múltiplo de "+str(n2))