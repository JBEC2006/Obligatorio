from entities.persona import Persona
class Medico(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, numero_celular, especialidad):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, numero_celular)
        self.__especialidad=especialidad
   
    @property
    def especialidad(self):
        return self.__especialidad
    
    @especialidad.setter
    def especialidad(self, nueva_especialidad):
        if all(c.isalpha() or c.isspace() for c in nueva_especialidad): 
            self.__especialidad = nueva_especialidad

        
        
    
