h=input("Onda en Hz? ")
if float(h)<(300e6):
    print("La onda es una onda de radio")
elif float(h)<(300e9):
    print("La onda es una onda de microondas")
elif float(h)<(384e12):
    print("La onda es una onda de infrarojo")
elif float(h)<(789e12):
    print("La onda es una onda visible")
elif float(h)<(30e15):
    print("La onda es una onda de ultravioleta")
elif float(h)<(30e18):
    print("La onda es una onda de rayos X")
else :
    print("La onda es una onda de rayos gamma")