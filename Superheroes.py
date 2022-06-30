from random import randint
from Escenarios import*
class Humano():
  def __init__(self):
    self.inteligencia=randint(3,7)
    self.fuerza=randint(1,6)
    self.velocidad=randint(2,5)
    self.resistencia=randint(2,5)
    self.proyeccionenergia=randint(1,6)
    self.habilidadeslucha=randint(1,7)
    self.total=self.inteligencia+self.fuerza+self.velocidad+self.resistencia+self.proyeccionenergia+self.habilidadeslucha
    
class Extraterrestre():
  def __init__(self):
     self.inteligencia=randint(4,6)
        self.fuerza=randint(1,7)
        self.velocidad=randint(1,7)
        self.resistencia=randint(3,7)
        self.proyeccionenergia=randint(1,7)
        self.habilidadeslucha=randint(3,6)
        self.total=self.inteligencia+self.fuerza+self.velocidad+self.resistencia+self.proyeccionenergia+self.habilidadeslucha
 class Superheroe():
  def __init__(self,identificador,alias,identidadsecreta,conjuntodemovimientos,tipo,escenario):
        if type(identificador)==int:
           self.identificador=identificador
        else:
            raise TypeError
 
 if type(alias)==str:
            self.alias=alias
        else:
            raise TypeError
         
if type(identidadsecreta)==str:
            self.identidadsecreta=identidadsecreta
        else:
            raise TypeError
        

  if type(conjuntodemovimientos)==dict:
            self.conjuntodemovimientos=conjuntodemovimientos
        else:
            raise TypeError
            
 if type(tipo)==object:
            self.tipo=tipo
        else:
            raise TypeError
        if type(escenario)==object:
            self.coste=(escenario.monedas/escenario.equipo)*(self.tipo.total/30)
        else:
            raise TypeError  
