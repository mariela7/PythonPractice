#####################################   Ejercicio 2.1
'''A continuación hemos creado unas variables "tres","tresconseis" y "hola" con unos valores almacenados en ellas. usando la función type debereis almacenar el tipo de datos que corresponde en las variables que creareis vosotros "typeTres", "typeTresConSeis" y "typeHola".'''
tres = 3
tresConSeis = 3.6
hola = "hola mundo"

# YOUR CODE HERE
typeTres = type(tres)
typeTresConSeis = type(tresConSeis)
typeHola = type(hola)

print (typeTres)
print (typeTresConSeis)
print (typeHola)


#####################################   Ejercicio 2.2
'''En el siguiente fragmento de código tenemos un input en el que le solicitamos al usuario cuantos litros de agua se ha bebido hoy y se los vamos a restar a la variable "aguaEnDeposito" de modo que tendremos un control de cuando comprar agua.

Realiza una conversión del tipo de datos del input para que sea de tipo int y asígnalo a la variable consumo de modo que podamos hacer la resta.'''
# YOUR CODE HERE
aguaEnDeposito = 50
consumo = input ('¿Cuantos litros de agua has consumido hoy?')
resultado = aguaEnDeposito - int(consumo)
print (f'Quedan {resultado} litros de agua')


#####################################   Ejercicio 2.3
'''Modifica las siguientes operaciones añadiendoles paréntesis de modo que el resultado sea el indicado en el comentario. Añade las instrucciones print necesarias para visualizar en pantalla los resultados.'''
# YOUR CODE HERE
primera = (3+2)*5 #25
print (f'Primera: {primera}')

segunda = 3+3**(2+1) #30
print (f'Segunda: {segunda}')

tercera = 3/5-2 #-1.4
print (f'Tercera: {tercera}')


#####################################   Ejercicio 2.4
'''El código a continuación tiene un input que solicitará tu nombre y un print que tratará de darte la bienvenida. Modifica la variable bienvenida de modo que concatene tu nombre dentro del mensaje de bienvenida.'''
# YOUR CODE HERE
nombre = input('¿Como te llamas? ')
bienvenida = 'Bienvenid@ : ' + str(nombre) #modifica esta línea
print(bienvenida)


#####################################   Ejercicio 3.1
'''A continuación tenemos un input en el que le pediremos un número al usuario y lo guardaremos en la variable entrada. Después, deberemos guardar en la variable mayorQueTres el valor True si ese número es mayor que tres y False en caso contrario. Nota, acordaros de realizar la conversión de tipos en el input'''
# YOUR CODE HERE
entrada = input('Introduce un número:')


#####################################   Ejercicio 5.1
'''Define la función holamundo de forma que haga una llamada al comando print con el mensaje 'Hola mundo'. En la celda siguiente haz uso de dicha función.'''
# YOUR CODE HERE
def holamundo():
    print('Hola mundo!')

# YOUR CODE HERE
holamundo()


#####################################   Ejercicio5.2
'''Define la función miconcatena la cual haga solicite dos parámetros, la función deberá hacer un print concatenando ambos parámetros como cadena.'''
# YOUR CODE HERE
def miconcatena(texto1, texto2):
    cadena = texto1 + ' ' + texto2
    return cadena
    
# YOUR CODE HERE
miconcatena('Hola a todos.', 'Soy Mariela')


#####################################   Ejercicio 5.3
'''A continuación define la función cuentapalabras la cual tendrá 2 parámetros, el primer parámetro será un texto y el segundo una palabra.

La función deberá devolver usando el comando return el número de veces que aparece la palabra dentro del texto en una variable de tipo entero.

Devolverá 0 si no aparece ninguna vez.

Ejemplo:

cuentapalabras('eran uno dos y tres los valientes', 'eran') 1 cuentapalabras('dos manzanas tres peras dos naranjas', 'dos') 2'''
# YOUR CODE HERE
def cuentapalabras(texto, palabra):
    cont = texto.count(palabra)
    print (cont)
    
# YOUR CODE HERE
cuentapalabras('Aquí voy De malas pero voy Haciendo malabares pa pagar la renta', 'voy')


#####################################   Ejercicio 5.4
'''Define un módulo constantes.py en la misma carpeta que este ejercicio, en ese módulo deberás definir las constantes:

PI = 3.1416
G = 9.8
E = 2.7183
GR = 1.618033
F = 4.669201
En el código a continuación importa el módulo que acabas de crear y muestra con el comando print los valores que has definido.'''
# YOUR CODE HERE
#constantes.py
PI = 3.1416
G = 9.8
E = 2.7183
GR = 1.618033
F = 4.669201

# YOUR CODE HERE

import constantes

print (constantes.PI)



#####################################   Ejercicio 6.1
'''Escribe una función **cambiaprimera** que dada una cadena nos devuelva la misma cadena pero reemplazando todas las veces que aparezca la primera letra por el símbolo &#36;, excepto en esa primera letra.

Ejemplo:

- cambiaprimera('casco')
- -> 'cas&#36;o'
- cambiaprimera('rocodromo')
- -> 'rocod&#36;omo' '''
# YOUR CODE HERE
def cambiaprimera(cadena):
    indice = 0
    retorno=""
    for letra in cadena:
        #print (f'Indice: ',indice, ' Letra: ', letra, ' Cadena indice: ', cadena[indice])
        if ((letra == cadena[0]) and (indice > 0)):
            retorno = retorno + "$"
            #print (f'SI -- Vuelta: ', indice, ' - retorno', retorno)
        else:
            retorno = retorno + letra
            #print (f'NO -- Vuelta: ', indice, ' - retorno', retorno)
        indice = indice + 1
    return (retorno)
    
# YOUR CODE HERE
print(cambiaprimera("casco"))


#####################################   Ejercicio 6.2
'''Escribe una función concatenamal que, dadas dos cadenas nos devuelva una sola cadena combinando ambas unidas por un espacio, pero cambiando las dos primeras letras de cada palabra.

Ejemplo:

concatenamal('casco','polipo')
-> 'posco calipo'
concatenamal('rocodromo','encrucijada')
-> 'encodromo rocrucijada' '''
# YOUR CODE HERE
def concatenamal(palabra1, palabra2):
    inicio1 = palabra1[0:2]
    inicio2 = palabra2[0:2]
    
    fin1 = palabra1[2:]
    fin2 = palabra2[2:]
    
    '''print(palabra1)
    print(palabra2)
    print(inicio1)
    print(inicio2)
    print(fin1)
    print(fin2)'''
    
    resultado = inicio2 + fin1 + ' ' + inicio1 + fin2
    
    return resultado
    
# YOUR CODE HERE
print (concatenamal('casco','polipo'))


#####################################   Ejercicio 6.3
'''Escribe una función enelmedio que dadas dos cadenas nos devuelva una sola cadena de modo que la segunda quede en el medio de la primera tal y como se muestra en los ejemplos.

Ejemplo:

enelmedio('[::]','polipo')
-> '[:polipo:]'
enelmedio('rocodromo','XXX')
-> 'rocoXXXdromo'
enelmedio('-:..:-','Título')
-> '-:.Título.:-' '''
# YOUR CODE HERE
def enelmedio(palabra1, palabra2):
    largo1 = len(palabra1)
    
    mitad = largo1 / 2
        
    parte1 = palabra1[:int(mitad)]
    
    parte2 = palabra1[int(mitad):]
    
    resultado = parte1 + palabra2 + parte2
    return resultado
    
# YOUR CODE HERE
print(enelmedio('-:..:-','Título'))


#####################################   Ejercicio 6.4
'''Escribe una función cambiamayus que dadas una cadena nos devuelva la misma cadena cambiando las mayusculas por minúsculas y viceversa.

Ejemplo:

cambiamayus('Castilla')
-> 'cASTILLA'
cambiamayus('ENTretenido')
-> 'entRETENIDO'
cambiamayus('PaliNdrOmo')
-> 'pALInDRoMO' '''
# YOUR CODE HERE
def cambiamayus(palabra):
    nuevapal = ''
    for letra in palabra:
        ind = ord(letra)
        #print(f'Cod: ', ind, 'LEtra: ', letra)
        if ind >= 65 and ind <= 90:
            #Mayus
            nuevapal = nuevapal + letra.lower()
        else:
            nuevapal = nuevapal + letra.upper()
    return nuevapal
    
# YOUR CODE HERE
print(cambiamayus('PaliNdrOmo'))


#####################################   Ejercicio 7.1
'''En el archivo adjunto 'quijote.txt' hemos dejado los primeros párrafos del libro que comparte nombre con el archivo.

La función primerafrase(numerodeparrafo) deberá abrir el archivo y devolver el contenido de la primera frase del párrafo indicado (siendo 0 el primer párrafo). La primera frase estará definida por los caracteres que se encuentran en el párrafo hasta llegar al primer símbolo de puntuación (cualquiera del grupo ,.:;), tal y como se muestra en el ejemplo a continuación.

primerafrase(0)
-> 'En un lugar de la Mancha'
primerafrase(2)
-> 'Con estas razones perdía el pobre caballero el juicio' '''
# YOUR CODE HERE
def primerafrase(numerodeparrafo):
    fichero = open('quijote.txt', 'r', encoding='utf-8')
    texto = fichero.read()
    parrafos = texto.split('\n')
    while '' in parrafos: 
        parrafos.remove('')    
    parrafoseleccionado=parrafos[numerodeparrafo]
    pos = 0
    lafra = ''
    for letra in parrafoseleccionado:
        if letra == ',' or letra == '.' or letra == ':' or letra == ';':
            #print(parrafoseleccionado[:pos])
            lafra = (f'La primera frase del parrafo {numerodeparrafo} es: '+ str(parrafoseleccionado[:pos]))
            break
        pos = pos + 1
    fichero.close()    
    return(lafra)

primerafrase(7)