#Definiendo una clase
class Personaje:
    #Definiendo los atributos de esta clase
    def __init__(self, tipo, vida, daño):
        self.tipo =  tipo
        self.vida = vida
        self.daño = daño
    
    #Metodo exclusivo de esta clase
    def informacion(self):
        return f'El personaje es de tipo {self.tipo}\nTiene {self.vida} puntos de vida\ny tiene {self.daño} puntos de daño'

    #GEETER metodo para mostrar el atributo del objeto
    def get_vida(self):
        return self.vida
    
    #SETTER metodo para actualizar o cambiar el atributo del objeto
    def set_vida(self, nueva_vida):
        self.vida = nueva_vida

class NPC:
    def __init__(self, dialogo):
        self.dialogo = dialogo
    
    def hablar(self):
        return self.dialogo

#Heredando la clase Personaje en la nueva clase Villano
class Villano(Personaje):
    #Colocamos los atributos de la clase padre y finalmente de la clase hijo 
    def __init__(self, tipo, vida, daño, fases):
        #Heredamos los atributos de la clase padre con la función super()
        super().__init__(tipo, vida, daño)
        #Definimos los atributos de la clase hijo
        self.fases = fases
    
    def informacionVillano(self):
        return f'El personaje es de tipo {self.tipo}\nTiene {self.vida} puntos de vida\nTiene {self.daño} puntos de daño\ny tiene {self.fases} fases'

#Herencia multiple de las clases Personaje y NPC
class NPC_Jugable(Personaje, NPC):
    def __init__(self, tipo, vida, daño, dialogo, importancia):
        #Heredamos los atrubutos de las clases padre. Similar a usar la función super()
        Personaje.__init__(self, tipo, vida, daño)
        NPC.__init__(self, dialogo)
        
        self.importancia = importancia
    
    def informacion(self):
        return f'Hola, soy un NPC de importancia {self.importancia}'
    
    #self. para usar metodo de clase hijo
    def presentacion(self):
        return self.informacion()
    
    #super() para usar metodo de clase padre 
    def presentacion1(self):
        return super().informacion()