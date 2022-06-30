Explicación de las clases:
class Organizacion
Tiene un atributo de instancia cuyo valor no cambia el cual se trata de una lista de cadenas de caracteres,dónde se encuentran cada una de las organizaciones permitidas por el juego.Está lista se utiliza para comprobar que el nombre introducido por el usuario es el de una organización permitida.En caso contrario lanza una excepción.
El atributo miembros se trata de una lista dónde se almacenan los miembros elegidos.En caso de no ser un objeto de tipo lista se lanza una excecpion.Se comprueba que el atributo escenario introducido por el usuario,es un objeto,uno de los 3 escenarios definidos,en caso de que sea un onjeto,el atributo miembros toma el valor del atributo equipo de uno de dichos escenarios.En caso contrario lanza una excepcion.
Los métodos get_organización y get_miembros obtienen respectivamente el nombre de la organizacion y los miembros del equipo.

class SanctumSantorum,StarkTower XavierSchoolForGiftedYoungster
Cada una de estas clases posee los atributos monedas,equipo,movimientos y vida fijos.

class Humano y Extraterrestre
Poseen los mismos atributos,cada uno de ellos recibe un valor aleatorio entre el rango de valores fijo asignado,a la hora de crear una instancia.

class superheroe
Define cada uno de los atrubutos de tal forma que si la condición del if es falsa lanza una excecpión.El escenario es uno de los 3 objetos definidos en la clase Escenarios.
mi repositorio:https://github.com/AlejandroIlgesias/Superheroes.git
