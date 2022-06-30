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

    
  
