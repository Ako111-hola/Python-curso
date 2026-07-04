class Personaje:
    def __init__(self, tipo, vida, daño):
        self.tipo =  tipo
        self.vida = vida
        self.daño = daño
       
    def informacion(self):
        return f'El personaje es de tipo {self.tipo}\nTiene {self.vida} puntos de vida\ny tiene {self.daño} puntos de daño'

class Villano(Personaje):
    def __init__(self, tipo, vida, daño, fases):
        super().__init__(tipo, vida, daño)
        self.fases = fases
    
    def informacion(self):
        return f'El personaje es de tipo {self.tipo}\nTiene {self.vida} puntos de vida\nTiene {self.daño} puntos de daño\ny tiene {self.fases} fases'

verdugo = Villano("tanque", 1000000, 1000000, 3)

print(verdugo.informacion())

print("hola"[-1])