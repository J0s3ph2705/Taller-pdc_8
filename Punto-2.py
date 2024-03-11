n1=input("Número 1? ")
n2=input("Número 2? ")
n3=input("Número 3? ")
if float(n1)>float(n2) and float(n1)>float(n3):
    print("El número "+str(n1)+" es el mayor")
elif float(n2)>float(n1) and float(n2)>float(n3):
    print("El número "+str(n2)+" es el mayor")
else:
    print("El número "+str(n3)+" es el mayor")