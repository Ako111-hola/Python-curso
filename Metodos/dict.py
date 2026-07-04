diccionario = {
    'nombre' : 'Arisa',
    'edad' : 32,
    'altura' : 1.63,
    ('primer letra', 'ultima letra') : 'a'} #tupla as key. frozenset too

#dic = {key : valor}

diccionario.get('nombre') #valor del key. any
diccionario.keys() #clave. dict_keys

diccionario.items()

diccionario.update({'altura' : 1.64, 'nacionalidad': 'japonesa'}) #añade y actualiza valores

#diccionario.pop('altura') #elimina keys. x --> valor
#diccionario.clear()

dict.fromkeys('nombre', 'Arisa') #itera el primer elemento --> keys para Arisa
dict.fromkeys(['nombre', 'non'], 'Arisa') #la lista son las keys para Arisa