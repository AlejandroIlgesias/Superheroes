class Organizacion():
  def __init__(self,nombre,miembros,escenario):
     organizaciones=["A-Force", "Avengers", "Mercs for Money","League of Realms", "Strange Academy" ,"X-Men"]
      if type(nombre)==str:
            if nombre in organizaciones:
              self.nombre=nombre
           else:
              raise ValueError
      else:
            raise TypeError
      if type(miembros)==list:
        if type(escenario)==object:
          self.miembros=escenario.equipo
        else:
                raise TypeError
          
              
        

