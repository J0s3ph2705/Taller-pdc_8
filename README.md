# Taller-pdc_8

### Equipo y Logo: Pantalla Azul

<div align='center'>
<figure> <img src="https://github.com/J0s3ph2705/Taller-pdc_8/assets/159032718/b0dd65be-48ba-400b-a302-63eb8381cf65" alt="" width="1000" height="auto"/></br>
</figure>

</div> 

### Integrantes:

1. Joseph Lievano (1052383083)
2. Hernan Javier Casilimas Vega (1007366398)
3. Juan José	Tobar Álvarez (1112042373)

# Taller

1. Realice el <a href="https://pythonspot.com/python-tests-quizes/">quiz</a> *Python Beginner Quiz* (20 preguntas) y adjunte pantallazo con el resultado (mínimo 90% bien).
<div align='center'>
<figure> <img src="https://github.com/J0s3ph2705/Taller-pdc_8/assets/159032718/9f46d8e8-9429-43af-a408-9d0ff13c586f" alt="" width="1000" height="auto"/></br>
</figure>
</div> 
<div align='center'>
<figure> <img src="https://github.com/J0s3ph2705/Taller-pdc_8/assets/159032718/be751ce7-b453-42b6-a572-34f28e07f62f" alt="" width="1000" height="auto"/></br>
</figure>
</div> 
<div align='center'>
<figure> <img src="https://github.com/J0s3ph2705/Taller-pdc_8/assets/159032718/fd104740-8fa8-42d9-949f-1956f0582e2f" alt="" width="1000" height="auto"/></br>
</figure>


</div> 

2. Realice un programa que lea tres números reales y determine cuál es el mayor.
   
  Se toma los números y se comparan entre sí para determinar el número mayor
```python
  #El programa toma los números

n1=input("Número 1? ")
n2=input("Número 2? ")
n3=input("Número 3? ")

#El programa compara los números e imprime el mayor

if float(n1)>float(n2) and float(n1)>float(n3):
    print("El número "+str(n1)+" es el mayor")
elif float(n2)>float(n1) and float(n2)>float(n3):
    print("El número "+str(n2)+" es el mayor")
else:
    print("El número "+str(n3)+" es el mayor")
```
3. Realice un programa que lea un número enteros y determine si es par o impar.
   
  Se toma el número entero y se saca el módulo entre 2, si da 0 entonces el número es par
```python
  #Se toma el número

n1=input("Número? ")

#Se saca el módulo entre 2, si es 0 el número es par

if int(n1)%2==0:
    print("El número "+str(n1)+" es par")
else:
    print("El número "+str(n1)+" es impar")
```
<div align='center'>
<figure> <img src="https://github.com/J0s3ph2705/Taller-pdc_8/assets/159032718/95495fc3-aa21-4a3f-b125-6fe539c7ab71" alt="" width="600" height="auto"/></br>
</figure>
</div> 

4. Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.
   
  Se toman los dos números y se dividen con decima y para que de entero, así un número da cifras decimales (si las tiene) y el otro da un número exacto. Si los 2 números son iguales, entonces es múltiplo, ya que se divide en el otro número exactamente.
```python
  #Se toma los números

n1=input("Número 1? ")
n2=input("Número 2? ")

#Se dividen los números (para que de decimal)

d=float(n1)/float(n2)

#Se dividen los números exactamente (para qeue de un número entero)

e=float(n1)//float(n2)

#Si se restan los resultados y da 0, significa que los dos resultaods son el mismo número, el cual tiene que ser entero, si es entero significa que el primer número si es múltiplo del segundo número.

if d-e==0:
    print(str(n1)+" es múltiplo de "+str(n2))
else:
    print(str(n1)+" no es múltiplo de "+str(n2))
```

<figure> <img src="https://github.com/J0s3ph2705/Taller-pdc_8/assets/159032718/504d3cfb-7358-4457-bbd6-b065a72c7644" alt="" width="600" height="auto"/></br>
</figure>
</div> 
5. Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.
   
  Se toman los 3 números, se da un valor a una variable equivalente a la suma de los 2 primeros números. Luego se compara la variable con el tercer número.
```python
  #se toman los números

n1=input("Número 1? ")
n2=input("Número 2? ")
n3=input("Número 3? ")

#Se suman el primer y segundo número

suma=float(n1)+float(n2)

#Se comparan los resultados con el tercer número.

if float(n3)>suma:
    print(str(n3)+" es mayor que "+str(n2)+"+"+str(n1))
elif float(n3)==suma:
    print(str(n3)+" es igual que "+str(n2)+"+"+str(n1))
else:
    print(str(n3)+" es menor que "+str(n2)+"+"+str(n1))

```
6. Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.
   
  Se toma la letra y se traduce a ASCII, luego se revisa si el número está en la lista con los códigos ASCII de todas las vocales, si está, es una vocal, sino, una consonante.
```python
  
#Se pide la letra

letra=input("Letra? ")

#Se hace un conjunto con los carácteres ASCII de las vocales

minu=(65,69,73,79,85,97,101,105,111,117)

#Si el ASCII de la letra está en el conjunto "minu", la letra es una vocal.

if ord(letra)in minu:
    print(str(letra)+" es una vocal")
else:
    print(str(letra)+" es una consonante")
```
7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número
    
  Se toman los números y se hace cada operación, una por una, diferenciando con paréntesis las operaciones que se deben resolver primero.
  Luego, se hacen muuuuchas comparaciones entre los valores de los 5 números y así poder determinar el orden ascendente y descendente.
  Luego, se toman el valor mayor y el menor para la potencia y la raíz.
```python
  #Se pide los números

n1=float(input("Número 1? "))
n2=float(input("Número 2? "))
n3=float(input("Número 3? "))
n4=float(input("Número 4? "))
n5=float(input("Número 5? "))

#Se saca el promedio, la mediana y el primedio multiplicativo, uno por uno y se imprimen

promedio=(float(n1)+float(n2)+float(n3)+float(n4)+float(n5))/5
print("El promedio es igual a "+str(promedio))
mediana=(float(n1)+float(n2)+float(n3)+float(n4)+float(n5))//5
print("La mediana es igual a "+str(mediana))
promedio_multiplicativo=(float(n1)*float(n2)*float(n3)*float(n4)*float(n5))**(1/5)
print("El promedio multiplicativo es igual a "+str(promedio_multiplicativo))

#Se comparan los 5 valores para organizarlos del mayor al menor y viceversa

if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5:
    menor = n1
    if n2 <= n3 and n2 <= n4 and n2 <= n5:
        medio1 = n2
        if n3 <= n4 and n3 <= n5:
            medio2 = n3
            if n4 <= n5:
                medio3 = n4
                mayor = n5
            else:
                medio3 = n5
                mayor = n4
        elif n4 <= n3 and n4 <= n5:
            medio2 = n4
            if n3 <= n5:
                medio3 = n3
                mayor = n5
            else:
                medio3 = n5
                mayor = n3
        else:
            medio2 = n5
            if n3 <= n4:
                medio3 = n3
                mayor = n4
            else:
                medio3 = n4
                mayor = n3
    elif n3 <= n2 and n3 <= n4 and n3 <= n5:
        medio1 = n3
        if n2 <= n4 and n2 <= n5:
            medio2 = n2
            if n4 <= n5:
                medio3 = n4
                mayor = n5
            else:
                medio3 = n5
                mayor = n4
        elif n4 <= n2 and n4 <= n5:
            medio2 = n4
            if n2 <= n5:
                medio3 = n2
                mayor = n5
            else:
                medio3 = n5
                mayor = n2
        else:
            medio2 = n5
            if n2 <= n4:
                medio3 = n2
                mayor = n4
            else:
                medio3 = n4
                mayor = n2
    elif n4 <= n2 and n4 <= n3 and n4 <= n5:
        medio1 = n4
        if n2 <= n3 and n2 <= n5:
            medio2 = n2
            if n3 <= n5:
                medio3 = n3
                mayor = n5
            else:
                medio3 = n5
                mayor = n3
        elif n3 <= n2 and n3 <= n5:
            medio2 = n3
            if n2 <= n5:
                medio3 = n2
                mayor = n5
            else:
                medio3 = n5
                mayor = n2
        else:
            medio2 = n5
            if n2 <= n3:
                medio3 = n2
                mayor = n3
            else:
                medio3 = n3
                mayor = n2
    else:
        medio1 = n5
        if n2 <= n3 and n2 <= n4:
            medio2 = n2
            if n3 <= n4:
                medio3 = n3
                mayor = n4
            else:
                medio3 = n4
                mayor = n3
        elif n3 <= n2 and n3 <= n4:
            medio2 = n3
            if n2 <= n4:
                medio3 = n2
                mayor = n4
            else:
                medio3 = n4
                mayor = n2
        else:
            medio2 = n4
            if n2 <= n3:
                medio3 = n2
                mayor = n3
            else:
                medio3 = n3
                mayor = n2
elif n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5:
    menor = n2
    if n1 <= n3 and n1 <= n4 and n1 <= n5:
        medio1 = n1
        if n3 <= n4 and n3 <= n5:
            medio2 = n3
print("Números ordenados ascendentemente " + str(menor) + " , " + str(medio1) + " , " + str(medio2) + " , " + str(medio3) + " , " + str(mayor) + " ")
print("Números ordenados descendentemente " + str(mayor) + " , " + str(medio3) + " , " + str(medio2) + " , " + str(medio1) + " , " + str(menor) + " ")

# Luego con el valor del menor y el mayor se saca la potencia y la raíz, y se imprimen.

potencia = mayor**menor
print("La potencia de el número mayor ("+str(mayor)+") a la de el número menor ("+str(menor)+") es "+str(potencia))
raiz=menor**(1/3)
print("La raíz cúbica del número menor ("+str(menor)+") es igual a "+str(raiz))
```
8. Escriba un programa al que se le ingrese la frecuencia de una onda en *hz* y como salida arroje en que parte del <a href="https://es.wikipedia.org/wiki/Espectro_electromagn%C3%A9tico">espectro electromagnético se encuentra</a>.
   
  Se toma la frecuencia y se compara con los valores iniciales de cada espectro electromagnético, en primero que sea mayor se determina el espectro electromagnético de la onda.
```python
  #Se pide la frecuencia en Hz

h=input("Onda en Hz? ")

#Se determina entre qué rango de frecuencia está, cada "elif" ´contiene´ un campo electromagnético, asi que cuando la frecuencia queda en un grupo, el programa imprime el programa al cual pertenece

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
```
<figure> <img src="https://github.com/J0s3ph2705/Taller-pdc_8/assets/159032718/e95dfafd-43b2-46d9-a895-1fdea61b4cc6" alt="1200" width="1200" height="auto"/></br>
</figure>
</div> 


9. Escriba un programa que reciba el nombre en minúsculas de un país de **America** y retorne la ciudad capital, si el país no pertenece al continente debe arrojar *país no identificado*.
    
Se toma el país y se compara con una "if" que tiene el nombre del pais ingresado, el cual devuelve como texto el país y su capital. Si no llega a coincidir en un "if", se da el texto "El país no es de América"
```python
  #Se pide el país en minúsculas
p = input("Ingresar un país de América en letras minusculas y sin tilde: ")
if p == "argentina":
  print("La capital de Argentina es Buenos Aires")
elif p == "bolivia":
  print("La capital de Bolivia es Sucre")
elif p == "brasil":
  print("La capital de Brasil es Brasilia")
elif p == "canada":
  print("La capital de Canadá es Ottawa")
elif p == "chile":
  print("La capital de Chile es Santiago")
elif p == "colombia":
  print("La capital de Colombia es Bogotá")
elif p == "costa rica":
  print("La capital de Costa Rica es San José")
elif p == "cuba":
  print("La capital de Cuba es La Habana")
elif p == "ecuador":
  print("La capital de Ecuador es Quito")
elif p == "el salvador":
  print("La capital de El Salvador es San Salvador")
elif p == "estados unidos":
  print("La capital de Estados Unidos es Washington D.C.")
elif p == "guatemala":
  print("La capital de Guatemala es Ciudad de Guatemala")
elif p == "haiti":
  print("La capital de Haití es Puerto Príncipe")
elif p == "honduras":
  print("La capital de Honduras es Tegucigalpa")
elif p == "jamaica":
  print("La capital de Jamaica es Kingston")
elif p == "mexico":
  print("La capital de México es Ciudad de México")
elif p == "nicaragua":
  print("La capital de Nicaragua es Managua")
elif p == "panama":
  print("La capital de Panamá es Ciudad de Panamá")
elif p == "paraguay":
  print("La capital de Paraguay es Asunción")
elif p == "peru":
  print("La capital de Perú es Lima")
elif p == "republica dominicana":
  print("La capital de República Dominicana es Santo Domingo")
elif p == "uruguay":
  print("La capital de Uruguay es Montevideo")
elif p == "venezuela":
  print("La capital de Venezuela es Caracas")
else:
  print("País no es de América")
```
10. Escriba un programa que dada una distancia calcule:
+ El tiempo que le tomaría a la luz recorrer la distancia.
+ El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
+ El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
+ El tiempo que le tomaría a Bolt recorrer la distancia.
  
  Se toma la distancia en metros y se divide en la velocidad de cada objeto/persona (una por una) en metros/segundo, luego el resultado es el tiempo en segundos.
```python
  #Se toma la distancia en metros

d=input("Distancia en metros? ")

#Se divide la distancia en la velocidad de cada elemento en metros/segundo

luz=float(d)/300000
sonido=float(d)/343
auto=float(d)/147.523
bolt=float(d)/12.3

#Se imprime el resultado de cada elemento, en segundos.

print("La luz se tardaría "+str(luz)+(" segundos"))      
print("El sonido (en el aire a temperatura normal) se tardaría "+str(sonido)+(" segundos"))
print("El Koeniggsegg Jesko Absolut a su velocidad máxima (531km/h) se tardaría "+str(auto)+(" segundos"))
print("Usain Bolt a su velocidad máxima (44km/h)se tardaría "+str(bolt)+(" segundos"))
```
