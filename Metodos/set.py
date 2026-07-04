#meter un conjunto dentro de otro
conj1 = frozenset(['dat1'])
conj2 = {'dat2', 'dat3', conj1} #--> conj2 = {frozenset({'dat1'}), 'dat2', 'dat3'}

conj2.add('5') #añade un elemento
conj2.update([6, 7, 5, 7]) #añade varios elementos. list, tuple & set

conj2.remove('dat2') #remueve un elemento. Si no existe --> ERROR
conj2.discard('dat2') #lo mismo, pero si no existe --> no pasa nada xd

c1 = {1, 2, 3}
c2 = {1, 2}

c2.issuperset(c1) #bool
#c2 >= c1
c2.issubset(c1) #bool
#c2 <= c1
c2.isdisjoint(c1) #verifica si hay elementos en común. bool

c2.union(c1) #--> {1, 2, 3} une
c1.intersection(c2)#--> {2} lo que está en ambos
c1.difference(c2) #--> {3} lo que está en el primero pero no en el otro
c1.symmetric_difference(c2) #lo que no está en ambos