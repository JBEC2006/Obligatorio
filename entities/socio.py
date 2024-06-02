from entities.persona import Persona
class Socio(Persona):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, numero_celular, tipo, deuda=0):
        super().__init__(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, numero_celular)
        self.__tipo = tipo
        self.__deuda = deuda

    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def deuda(self):
        return self.__deuda