cad1 = '  Arisa es la más hermosa            '

cad1[5:17] #str desde el caracter x hasta el y

cad1.upper() #MAYUSCULAS. str
cad1.lower() #minusculas. str
cad1.capitalize() #solo la primer letra en Mayuscula. str
cad1.strip() #elimina caracteres especiales a los extremos. str

cad1.find('Arisá es') #busca la primera coincidencia. -1 si no. int
cad1.index('a') #lo mismo, pero con EXCEPCION. int
cad1.rfind('s') #lo mismo pero buscando desde el final. Tambien rindex. int 

cad1.isnumeric() #verifica si es un numerico True or False. bool
cad1.isalpha() #alfanumerico, sin caracteres especiales. bool

cad1.count('a') #numero de coincidencias. int

cad1.startswith('A') #verifica si str empieza con... bool
cad1.endswith('h') #verifica si str termina con... bool

cad1.replace('Arisa', 'Rikako') #reemplaza un str por otro. str

cad1.split(' ') #crea una lista con los caracteres separados por la cadena ingresada. list

len(cad1) #numero de caracteres. FUNCION. int

dir(cad1) #muestra metodos y atributos de un objeto. FUNCION. list