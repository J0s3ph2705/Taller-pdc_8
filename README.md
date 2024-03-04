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


2. Realice un programa que lea tres números reales y determine cuál es el mayor.

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
5. Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.

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
```python
  #Se pide los números

n1=input("Número 1? ")
n2=input("Número 2? ")
n3=input("Número 3? ")
n4=input("Número 4? ")
n5=input("Número 5? ")

#Se calcula el promedio, la mediana, el promedio multiplicativo...

promedio=(float(n1)+float(n2)+float(n3)+float(n4)+float(n5))/5
mediana=(float(n1)+float(n2)+float(n3)+float(n4)+float(n5))//5
promedio_multiplicativo=(float(n1)*float(n2)*float(n3)*float(n4)*float(n5))**(1/5)

#Se hace una lista con los números

lista=n1,n2,n3,n4,n5

#Se usa la función "sort" para oorganizarla ascendente y descendentemente, y se hacen 2 listas

ascendente=sorted(lista)
descendente=sorted(lista, reverse=True)

#Se toman los primeros valores de cada lista (el número más pequeño y el más grande) y se les asigna variables 

menor=float(ascendente[0])
mayor=float(descendente[0])

#Se realiza la potencia y la raíz que se pide

potencia=mayor**menor
raiz=menor**(1/3)

#Se imprimen los resultados

print("El promedio es igual a "+str(promedio))
print("La mediana es igual a "+str(mediana))
print("El promedio multiplicativo es igual a "+str(promedio_multiplicativo))
print("El orden ascendente es "+str(ascendente))
print("El orden descendente es "+str(descendente))
print("La potencia de el número mayor ("+str(mayor)+") a la de el número menor ("+str(menor)+") es "+str(potencia))
print("La raíz cúbica del número menor ("+str(menor)+") es igual a "+str(raiz))
```
8. Escriba un programa al que se le ingrese la frecuencia de una onda en *hz* y como salida arroje en que parte del <a href="https://es.wikipedia.org/wiki/Espectro_electromagn%C3%A9tico">espectro electromagnético se encuentra</a>.

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
9. Escriba un programa que reciba el nombre en minúsculas de un país de **America** y retorne la ciudad capital, si el país no pertenece al continente debe arrojar *país no identificado*.

```python
  #Se pide el país en minúsculas

p=input("País? ")

#Se hace una lista con los países y una con las capitales, de manera que cada país tenge el mismo index de su capital

paises=("canadá","estados unidos","méxico","belice","costa rica","el salvador","guatemala","honduras","nicaragua","panama","argentina","bolivia","brasil","chile","colombia","ecuador","paraguay","perú","surinam","trinidad y tobago","uruguay","venezuela","antigua y barbuda","bahamas","barbados","cuba","dominica" ,"granada","guyana","haití" ,"jamaica","república dominicana","san cristóbal y nieves","san vicente y las granadinas","santa Lucía")

capitales=["Otawwa.","Washington DC.","México DF.","Belmopán.","San José.","San Salvador.","Ciudad de Guatemala.","Tegucigalpa.","Managua.","Panamá.","Buenos Aires.","Sucre.","Brasilia.","Santiago de Chile.","Bogotá.","Quito.","Asunción.","Lima.","Parabarimo.","Puerto España.","Montevideo.","Caracas.","Saint John.","Nasáu.","Bridgetown.","La Habana.","Roseau.","Saint George.","Georgetown.","Puerto Príncipe.","Kingston.","Santo Domingo.","Basseterre.","Kingstown.","Castries."]

#Se verifica si el país está en la lista, si esta, se encuentra el index para poder hallar su capital y se imprime el país con su capital; si no, se imprime un texto que dice que el país no está en América.

if p in paises:
    numero=paises.index(p)
    print("la capital de "+p+" es "+capitales[numero])
else:
    print("El pais no pertenece a América.")
```
10. Escriba un programa que dada una distancia calcule:
+ El tiempo que le tomaría a la luz recorrer la distancia.
+ El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
+ El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
+ El tiempo que le tomaría a Bolt recorrer la distancia.

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
