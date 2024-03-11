letra=input("Letra? ")
minu=(65,69,73,79,85,97,101,105,111,117)
if ord(letra)in minu:
    print(str(letra)+" es una vocal")
else:
    print(str(letra)+" es una consonante")