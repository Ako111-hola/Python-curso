#variables o contenedores de DATOS

sujeto = 'Arisa'
edad = 32
altura = 1.63
txt = '''Arisa
        es la
        más hermosa'''

#datos simples

cadenas_de_texto = "Hola Arisa"     #string o str
numeros_entero= 32                  #int
numeros_reales = 1.63               #float
valores_booleanos = True            #bool

#datos compuestos

lista = ['Arisa', 32, 1.63, True] #modificable. list

tupla = ('Arisa', 32, 1.63, True) #NO modificable. tuple
#tuple(['Arisa', 32, 1.63, True])
#tupla[2] = 1.65 ERROR

conjunto = {'Arisa', 32, 1.63, True, 1.63, 32} #No datos duplicados. set
#set(['Arisa', 32, 1.63, True])
#print (conjunto[3]) ERROR

diccionario = {         #contendores de datos con valor --> <<key : valor>>
    'nombre' : 'Arisa',
    'edad' : 32,
    'altura' : 1.63}

#operadores de comparación

igual_q = 5 == 4
distinto_q = 5 != 6
mayor_q = 5 > 6
menor_q = 5 < 6
mayor_i = 5 >= 6
menor_i = 5 <= 6
pertenencia = 'Arisa' in txt #True or False
                             #in or not in

#operadores logicos

#AND
r1 = True and True #True
r2 = False and True #False
r3 = True and False #False
r4 = False and False #False

#OR
r5 = True or True #True
r6 = False or True #True
r7 = True or False #True
r8 = False or False #False

#NOT

r9 = not True #False
r10 = not False #True

#input

hola = input("Mejor miembro de Aqours es: ") #pedir info a la consola. str

#if-else

if hola == 'Arisa':
    print('eres un capo')
else:
    print('pendejo')
    
    
#BUCLES

lista = ['Arisa', 1.63, 32, 1994]
lista2 = ['yo', 1.72, 20, 2005]

#for

for x in lista: #x es una variable vacía que tomará valores de la propia lista mientras la recorre
    print(x)

for a, b in zip(lista, lista2):
    print (f'dato de Arisa: {a}, dato mio: {b}') #iterar dos listas. misma cant elem.

for x in range(11): #secuencia de numeros [0, ..., 10]
    print(x)

range(1, 10, 2) #numeros del 1 al 10 pero de dos en dos

#while

contador = 0

while contador < 5:
    print(contador) 
    contador +=1