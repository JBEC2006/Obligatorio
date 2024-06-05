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
    
    @tipo.setter
    def tipo(self, nuevo_tipo):
        if isinstance(nuevo_tipo, int)==True and (nuevo_tipo==1 or nuevo_tipo==2):
            return nuevo_tipo
    
    @deuda.setter
    def deuda(self, nueva_deuda):
        if isinstance(nueva_deuda, int)==True and nueva_deuda>=0:
            return nueva_deuda
