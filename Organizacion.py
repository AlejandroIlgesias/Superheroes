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
      else:
            raise TypeError
      def get_organizacion(self):
        return self.nombre
      def get_miembros(self):
        return str(self.miembros[0])+str(self.miembros[1])+str(self.miembros[2])
      def  is_undefeated(self):
        pass

    def surrender(self):
        pass
    def __str__(self):
        return 

      
        
          
          
              
        

