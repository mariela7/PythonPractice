#########################################################################   PRINT   ##
print ("Hola", 2, "mundo", 5)
nombre = input('Cual es tu nombre? ')
'''********************************************************'''
print ('Hola',nombre)
print("siguiente instrucción")
print(f'Primera: {primera}')
print(1, 3, 5, 7, 8) # 1 3 5 7 8
print(1, 3, 5, 7, 8, sep="*") # 1*3*5*7*8
print(1, 3, 5, 7, 8, sep="#", end="&") # 1#3#5#7#8&
print("The value of x is {} and the value of y is {}".format(x,y))
print("I like {0} and also {1}".format("Tea", "Milk")) #I like Tea and also Milk
print("I like {1} and also {0}".format("Tea", "Milk")) #I like Milk and also Tea

#########################################################################   ARITHMETIC OPERATORS   ##
+
5 + 5 = 10
-
5 - 5 = 0
*
5 * 5 = 25
/
5 / 5 = 1
%
23 % 5 = 3 #23/5 = 4 y sobran 3
//
23 // 5 = 4 #23/5 = 4
**
5 ** 2 = 25 #5 a la segunda potencia

#########################################################################   IDENTITY OPERATORS   ##
'''is'''
'''is not'''
x = 5
y = 10
print(x is y) #False
print(x is not y) #True

#########################################################################   MEMBERSHIP OPERATIONS   ##
x = "Hi there"
y = [1, 2, 3, 4]
print("H" in x) #True
print(1 in y) #True
print("t" not in x) #False
print(2 not in y) #False

#########################################################################   INPUT   ##
edadDelUsuario = input("dime tu edad")
f'la variable C vale: {c}'

#########################################################################   WHILE   ##
a=10
while a>0:
    print (a)
    a= a-1
print("siguiente instrucción")

#########################################################################   FOR ##
palabra="patatas"
for letra in palabra:
    print(letra)
print('siguiente instrucción')
'''********************************************************'''
frutas = ['manzana', 'pera', 'platano']

print('comienza el bloque')
for fruta in frutas:
  print(fruta)
  print("-")
print('finaliza el bloque')
'''********************************************************'''
for x in range(2, 30, 3): #Inicia en 2, hasta el 30, con saltos de 3
    print(x)
else:
    print("Finally completed!")

#########################################################################   IF  ##
a=True
if(a):
    print(a)
else:
    print("no")
print('Siguiente Instrucción')
'''********************************************************'''
a=3
if a==4:
    print("cuatro")
elif a>2:
    print("grt2")
print("siguiente instrucción")
'''********************************************************'''
edad = 21
if edad > 18:
  print('puede beber en España')
print ('eso es todo')

#########################################################################   RANGE   ##
list(range(5))
'''********************************************************'''
range(2,7)
'''********************************************************'''
a="patatas"
for i in range(0,len(a)):
    print(a[i])
print('siguiente instrucción')

#########################################################################   BREAK   ##
palabra="patatas"
for letra in palabra:
    print (letra)
    if letra == 't':
      break
print('siguiente instrucción')

#########################################################################   CONTINUE    ##
a="patatas"
for letra in a:
    if letra=='a':
        continue
    print (letra)
print('siguiente instrucción')

#########################################################################   FUNCIONES   ##
def funcionSuma():
  a = 5
  b = 3
  print (a+b)

funcionSuma()

valor = input('Escribe el número:') #pero el usuario lo pone con letras
valor_numerico = int(valor)
resultado = valor_numerico + 3
print(resultado)

#########################################################################   TRY   ##
try:
  valor = "siete"
  valorNumerico = int(valor)
  resultado = valorNumerico + 3 #esto no se ejecutará porque falla en la linea anterior
  print(resultado)
except ValueError:
    valorNumerico = 0
finally:
  print(valorNumerico + 3)
'''********************************************************'''
num = input('Introduce un número:')
#TU CÓDIGO AQUÍ
numInt = int(num)
if(numInt%2 == 0):
    print("PAR")
else:
    print ("IMPAR")
'''********************************************************'''
num=18
intNum=int(num)
if (intNum%3==0):
    print(num/3)
'''********************************************************'''
num = input('Introduce un número:')
#TU CÓDIGO AQUÍ
try:
    numInt = int(num)
    if(numInt > 0):
        #El numero es positivo
        print("Seguimos")
        numero = 1
        while (numero <= numInt):
            if(numero%5 == 0 or numero%7 == 0):
                print ("Número divisibe: ", numero)
            numero = numero + 1
    else:
        print("El número es negativo")
except:
    print ("El número no es entero")

#########################################################################   TIPOS DE ARREGLOS   ##
cadena ="hola caracola"
lista =["pera","manzana","piña"]
tupla = ("pera","manzana","piña")
set = {1, 2, 3, 4}
diccionario = {"nombre":"Leonardo", "apellidos": "Salom Muñoz"}

#########################################################################   LISTAS  ##
lista = [9,13,2,7,124,-5]
print(len(lista))
'''********************************************************'''
lista = [9,13,2,7,124,-5]
print(sum(lista))
'''********************************************************'''
lista = [9,13,2,7,124,-5]
print(sum(lista)/len(lista))
'''********************************************************'''
lista = [9,13,2,7,124,-5]
print(7 in lista)
'''********************************************************'''
lista = [9,13,2,7,124,-5,0]
print(max(lista))
print(min(lista))
'''********************************************************'''
fruit_list = ["banana", "cherry", "lemon"]
if "banana" in fruit_list:
    print("banana is in the fruit_list!")#banana is in the fruit_list!
'''********************************************************'''
fruit_list[1] = "Apple"
print(fruit_list)#["banana", "Apple", "lemon"]
'''********************************************************'''
fruit_list[0] = ["fig", "watermelon"]
print(fruit_list) #[["fig", "watermelon"], "Apple", "lemon"]
'''********************************************************'''
fruit_list.insert(1, "banana")
print(fruit_list) #[["fig", "watermelon"], "banana", "Apple", "lemon"]
'''********************************************************'''
fruits = ["fig", "apple", "watermelon"]
fruits.append("orange")
print(fruits)#["fig", "apple", "watermelon", "orange"]
'''********************************************************'''
fruits2 = ["lemon", "cherry"]
fruits.extend(fruits2)
print(fruits)#["fig", "apple", "watermelon", "orange","lemon", "cherry"]
'''********************************************************'''
fruits.remove("watermelon")
print(fruits)#["fig", "apple", "orange","lemon", "cherry"]
'''********************************************************'''
fruits.pop(1)
print(fruits)#["fig", "orange","lemon", "cherry"]
'''********************************************************'''
fruits.pop()#"cherry"
'''********************************************************'''
print(fruits)#["fig", "orange","lemon"]
'''********************************************************'''
del fruits[0]#Si no establece el indice, se borra la lista entera
print(fruits)#["orange","lemon"]
'''********************************************************'''
fruits.clear()
print(fruits)#[]

#########################################################################   TUPLAS  ##
newfruits = ("fig", "banana", "lemon")
print(newfruits) #("fig", "banana", "lemon")
'''********************************************************'''
newfruits = ("fig", "banana", "lemon", "banana")
print(newfruits) #("fig", "banana", "lemon", "banana")
'''********************************************************'''
len(newfruits) #4
'''********************************************************'''
new_f =  tuple(("Banana", "Apple", "Fig"))
print(new_f) #('Banana', 'Apple', 'Fig')
print(type(new_f)) #<class 'tuple'>
'''********************************************************'''
print(new_f[0]) #Banana
print(new_f[1]) #Apple
'''********************************************************'''
print(new_f[-1]) #Fig
print(new_f[-2]) #Apple
'''********************************************************'''
print(new_f[0:2]) #('Banana', 'Apple')
'''********************************************************'''
fruits_t = ("apple", "banana", "fig", "cherry")
if "banana" in fruits_t:
    print ("Yes, banana is in fruits!") #Yes, banana is in fruits!")
'''********************************************************'''
fruits_l = list(fruits_t)
fruits_l[1] = "watermelon"
fruits_t = tuple(fruits_l)
print(fruits_t) #("apple", "watermelon", "fig", "cherry")
'''********************************************************'''
aTuple = "Yellow", 20, "Red"
a, b, c = aTuple
print(a) #'Yellow
'''********************************************************'''
#########################################################################   SETS ##
fruits_set = {"apple", "fig", "lemon"}
print(fruits_set) #{'fig', 'lemon', 'apple'} ##DESORDENADOS
'''********************************************************'''
len(fruits_set) #3
'''********************************************************'''
fruits_set.add("orange")
print(fruits_set)#{'apple', 'fig', 'orange', 'lemon'}
'''********************************************************'''
fruits_set.update(["banana", "cherry"])
print(fruits_set)#{'apple', 'banana', 'fig', 'lemon', 'cherry', 'orange'}
'''********************************************************'''
fruits_set.remove("orange")
print(fruits_set)#{'apple', 'banana', 'fig', 'lemon', 'cherry'}
'''********************************************************'''
fruits_set.discard("cherry")
print(fruits_set)#{'apple', 'banana', 'fig', 'lemon'}
'''********************************************************'''
set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}
set1.difference_update(set2)
print(set1) #{'Black', 'Yellow'}
'''********************************************************'''
sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.add("Blue")
sampleSet.add("Orange")
print(sampleSet) #{'Orange', 'Black', 'Yellow', 'Blue'} ##SIN DUPLICADOS
'''********************************************************'''
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}
print(set1.issubset(set2)) #True
print(set2.issuperset(set1)) #True
'''********************************************************'''
set1 = {10, 20, 30, 40}
set2 = {50, 20, "10", 60}
set3 = set1.union(set2)
print(set3) #{40, 10, 50, 20, '10', 60, 30} ##SIN DUPLICADOS

#########################################################################   DICCIONARIOS ##
newcars = {
    "brand" : "BMW",
    "model" : "X5",
    "year" : 2017
}
print(newcars) #{'brand': 'BMW', 'model': 'X5', 'year': 2017}
'''********************************************************'''
len(newcars) #3
'''********************************************************'''
print(newcars["brand"]) #BMW
'''********************************************************'''
x = newcars.get("brand")
print(x) #BMW
'''********************************************************'''
x = newcars.keys()
print(x) #dict_keys(['brand', 'model', 'year'])
'''********************************************************'''
x = newcars.values()
print(x) #dict_values(['BMW', 'X5', 2017, 'black'])
'''********************************************************'''
newcars["color"] = "black"
print(newcars) #{'brand': 'BMW', 'model': 'X5', 'year': 2017, 'color': 'black'}
'''********************************************************'''
newcars["year"] = 2019
print(newcars) #{'brand': 'BMW', 'model': 'X5', 'year': 2019, 'color': 'black'}
'''********************************************************'''
x = newcars.items()
print(x) #dict_items([('brand', 'BMW'), ('model', 'X5'), ('year', 2019), ('color', 'black')])
'''********************************************************'''
newcars.update({"color" : "white"})
print(newcars) #{'brand': 'BMW', 'model': 'X5', 'year': 2019, 'color': 'white'}
'''********************************************************'''
newcars.pop("year")
print(newcars) #{'brand': 'BMW', 'model': 'X5', 'color': 'white'}
'''********************************************************'''
newcars.popitem() #('color', 'white')
print(newcars) #{'brand': 'BMW', 'model': 'X5'}

#########################################################################   CADENAS ##
refran = "el perro de san roque no tiene rabo \n"\
        "porque ramón rodriguez se lo ha robado,\n"\
        " esto es un refrán típico en España."
'''********************************************************'''
len(refran)
##El perro de San Roque no tiene rabo ...
refran[0] ##Obtiene el caracter de la posicion 0
refran[0:10] ##De la posicion 0 a la 10
refran[:20] ##De la posicion 0 a la 20. Se asume el 0
refran[20:] ##De la posicion 20 al final. Se asume el final
refran[:-10] ##Desde el principio al final, sin los ultimos 10
refran[-10:] ##ultimos 10 caracteres
refran.lower() ##Todo en minusculas
refran.upper() ##Todo en mayusculas
refran.capitalize() ##Primera letra en mayusculas
refran.replace('no','si') ##reemplazar texto
refran.find('Roque') ##Primera posición donde esta ubicada la palabra
refran[refran.find('Roque'):refran.find('Roque') + len('Roque')] ##cortar una palabra hallada
refran.find('roque') ##Si no la encuentra, porque es sensible a mayusculas
refran.lower().find('roque'.lower()) ##poner todo en minusculas para buscar
refran.strip() ##Quita los espacios al principio y al final
refran.split() ##Divide la cadena en palabras y las coloca en una lista
refran.split('no') ##Busca lo que esta entre parentesis, y lo usa para partir la cadena en ese punto. Borrando esos caracteres

letra="@"
ord(letra) ##Devuelve el código ASCII de la letra
'''********************************************************'''
chr(64) ##DEvuelve el caracter al correponde el codigo

#Codificacion de cadenas
cadena="El perro de Roque"
cadenacodificada=""
desplazamiento=7
for letra in cadena:
    cadenacodificada=cadenacodificada+chr(ord(letra)+desplazamiento)
cadenadecodificada=''
for letra in cadenacodificada:
    cadenadecodificada=cadenadecodificada+chr(ord(letra)-desplazamiento)

print(cadena)
print(cadenacodificada)
print(cadenadecodificada)


#########################################################################   ARCHIVOS ##
r -> Read
a -> Append
w -> Write
x -> Create
'''read : Lee el archivo completo'''
archivo = open('ejercicio.csv', 'r')
contenido = archivo.read() ## ojo con los \n
print(contenido)
archivo.close()

'''read : Lee número especifico de caracteres(10) desde la posicion cero'''
archivo = open('ejercicio.csv', 'r')
contenido = archivo.read(10) ## ojo con los \n
print(contenido)

'''readline : Lee el archivo linea a linea'''
archivo = open('ejercicio.csv', 'r')
linea0 = archivo.readline()
linea1 = archivo.readline()
print (linea0)
print (linea1)
archivo.close()

'''readlines : Lee todas las lineas, por separado'''
archivo = open("ejercicio.csv", "r")
for linea in archivo.readlines():
    print(linea)
archivo.close()

'''tell : Devuelve la posicion del archivo donde esta ubicado el puntero'''
archivo = open('ejercicio.csv', 'r')
print (archivo.tell())
linea0 = archivo.readline()
print (archivo.tell())
archivo.close()

'''seek : Sirve para moverse entre las ubicaciones del archivo'''
archivo = open('ejercicio.csv', 'r')
archivo.read()
print archivo.tell()
archivo.seek(0)
print archivo.tell()
archivo.close()

'''write : escribe sobre un archivo, si no existe lo crea, si existe sobre escribe'''
archivo = open("prueba_escritura.extension",'w+')
archivo.write('B; vbdjksbvsabvibfbskcbzxvjbzxjk')
archivo.close()

'''flush : Permite añadir texto al final de un archivo'''
archivo = open("prueba_escritura.extension",'a+')
archivo.write('cadena para flushear\n')
archivo.flush()
archivo.close()

'''with open : Para controlar que el archivo se cierre'''
with open("prueba_escritura.extension",'r') as archivo:
    print(archivo.read())
print(archivo.read())


def parrafo(numerodeparrafo):
    #primero cargamos el fichero
    fichero = open('quijote.txt', 'r', encoding='utf-8')
    #lo leemos
    texto = fichero.read()
    #y seleccionamos el párrafo indicado en el parámetro
    parrafos = texto.split('\n')
    while '' in parrafos:
        parrafos.remove('')
    parrafoseleccionado=parrafos[numerodeparrafo]

    #acordaos de cerrar el fichero si no lo habéis abierto con un with
    fichero.close()
    return(parrafoseleccionado)

parrafo(8)

#########################################################################   FUNCIONES ##
def mifuncion():
    a= 3 + 4
    print(a)
mifuncion()
'''********************************************************'''
def suma(sumandoA,sumandoB):
  total = sumandoA + sumandoB
  return total, 'mensaje'
numero, texto = suma(5,7)
print(numero)
print(texto)
'''********************************************************'''
def fruits(*name):
    print("The fruit is " + name[2])

fruits("Apple", "Fig", "Cherry")#The fruit is Cherry
'''********************************************************'''
def numbers(n):
    if(n>0):
        result = n + numbers(n-1)
        print(result)
    else:
        result = 0
    return result

numbers(6)'''1
3
6
10
15
21'''

#########################################################################   LAMBDA ##
x = lambda i:i +10
print(x(5))#15
'''********************************************************'''
calculate = lambda x, y : x * y
print(calculate(5,7))#35
'''********************************************************'''
math_op = lambda x, y, z : x * y + z
print(math_op(2, 3, 4))#10
'''********************************************************'''
def multiply(n):
    return lambda x:x*n

double = multiply(2)
triple = multiply(3)

print(double(10))#20
print(triple(10))#30

#########################################################################   CLASES Y OBJETOS ##
class NewClass:
    num = 10

print (NewClass)#<class '__main__.NewClass'>
'''********************************************************'''
class NewClass:
    num = 10

p1 = NewClass()
print (p1.num)#10
'''********************************************************'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

ob1 = Person("Dony", 40)

print(ob1.name) #Dony
print(ob1.age) #40
'''********************************************************'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hi(self):
        print("Hi my name is " + self.name)

ob1 = Person("Dony", 40)
ob1.hi() #Hi my name is Dony
'''********************************************************'''
 class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hi(self):
        print("Hi my name is " + self.name)

ob1 = Person("Dony", 40)

#Modify ob1
ob1.age = 50
print(ob1.age) #50

#########################################################################   MODULOS ##
'''constantes.py'''
PI = 3.1416
G = 9.8
E = 2.7183
GR = 1.618033
F = 4.669201

'''llamada.py'''
import constantes

print (PI)
'''********************************************************'''
'''mymodule.py'''
def greeting(name):
    print("Hi " + name + " nice to meet you.")
 
 '''main.py'''
import mymodule

mymodule.greeting("Ronaldo")

'''********************************************************'''
'''mymodule.py'''
person = {
    "name" : "Dany",
    "age" : 40,
    "country" : "Finland"
    }
    
 '''main.py'''
x = mymodule.person["name"]
print(x)

from mymodule import person

print(person["country"])

#########################################################################   NumPy ##
import numpy as np

new_arr = np.array([1, 2, 3, 4, 5])
print(new_arr) #[1 2 3 4 5]
'''********************************************************'''
print(type(new_arr)) #<class 'numpy.ndarray'>
'''********************************************************'''
another_arr = np.array((1,2,3,4))
print(another_arr) #[1 2 3 4]
'''********************************************************'''
#0-D Array
arr = np.array(30)
print(arr) #30

# 1-D Array
new_arr = np.array([1, 2, 3, 4, 5])
print(new_arr) #[1 2 3 4 5]

# 2-D Array
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1) #[[1 2 3]
            #[4 5 6]]

# 3-D Array
arr2 = np.array([[[1, 3, 4], [6, 7, 8]], [[1, 2, 3], [6, 7, 8]]])
print (arr2)    #[[[1 3 4]
                #[6 7 8]]

                #[[1 2 3]
                #[6 7 8]]]
'''********************************************************'''
# Check number of dimensions
a = np.array(30)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 3, 4], [6, 7, 8]], [[1, 2, 3], [6, 7, 8]]])

print(a.ndim) #0
print(b.ndim) #1
print(c.ndim) #2
print(d.ndim) #3
'''********************************************************'''
# Higher dim arr
new_arr = np.array([1, 2, 3, 4], ndmin=5)
print(new_arr)#[[[[[1 2 3 4]]]]]
print("The number of dimensions: ", new_arr.ndim) #The number of dimensions:  5
'''********************************************************'''
arr1 = np.array([10, 20, 30, 40])
print(arr1[0]) #10
print(arr1[1]) #20
print(arr1[2]) #30
'''********************************************************'''
# Access 2-D Arr
newArr = np.array([[10, 20, 30], [40, 50, 60]])

print("The second element in 1st dim is: ", newArr[0, 1])#The second element in 1st dim is:  20

'''********************************************************'''
# Access 3-D Arr
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#the third element in the second array of the first array
print(arr3[0, 1, 2])#6
'''********************************************************'''
new_arr = np.array([1, 2, 3, 4, 5, 6])
print(new_arr[1:4]) #[2 3 4]
print(new_arr[3:]) #[4 5 6]
print(new_arr[:3]) #[1 2 3]
print(new_arr[-4:-1]) #[3 4 5] 
print(new_arr[1:6:2]) #[2 4 6] --- [indice inicial: indice final: salto]
'''********************************************************'''
#Slice 2-d
new_arr = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]])
print(new_arr[1, 1:4]) #[20 30 40] --- [indica la dimension, inicio del rango:fin del rango]

print(new_arr[0:2, 3]) #[ 4 40] --- [inicio de la dimension:fin de la dimension, indice]

print(new_arr[0:2, 1:4])    #[[ 2  3  4]
                            #[20 30 40]]
'''********************************************************'''
'''********************************************************'''
new_arr1 = np.array([1, 2, 3])
print(new_arr1.dtype) #int32

new_arr2 = np.array(["banana", "fig", "watermelon"])
print(new_arr2.dtype) #<U10

new_arr2 = np.array(["banana", "fig", "watermelon"], dtype = "S")
print(new_arr2.dtype)#|S10
'''********************************************************'''
a = np.array([1, 2, 3, 4])
b = a + 2
print(b) #[3 4 5 6]
'''********************************************************'''
c = np.array([1, 2, 3, 4])
d = np.array([10, 20, 30, 40])
e = c + d
print(e) #[11 22 33 44]
'''********************************************************'''
c = np.array([1, 2, 3, 4])
d = np.array([10, 20, 30, 40])
np.dot(c, d) #300 --- ((1*10)+(2*20)+(3*30)+(4*40))
'''********************************************************'''
c = np.array([1, 2, 3, 4])
np.exp(c) #array([ 2.71828183,  7.3890561 , 20.08553692, 54.59815003])

#########################################################################   MATPLOTLIB ##














