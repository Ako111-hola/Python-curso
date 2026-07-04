lista = ['Arisa', 32, 1.63, True]

lista.index('Arisa') #buscar elemento

lista.append('HERMOSA') #agrega un elemento
lista.insert(2, 'BELLA') #agrega un elemento en un indice especifico
lista.extend(['preciosa', 1994]) #agrega varios elementos.
                                 #if (list = False & str = True) -> itera str
                                 #if (str = False) -> ERROR

lista.pop(-1) #elimina un elemento por su indice
lista.remove('HERMOSA') #elimina un elemento por su valor
#lista.clear() elimina todos los elementos

#lista.sort() ordena los elementos de menor a mayor. NO str
#lista.reverse() mayor a menor