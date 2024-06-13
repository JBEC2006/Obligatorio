from abc import ABC
from datetime import datetime
class Persona(ABC):
    def __init__(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, numero_celular ):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__fecha_nacimiento = fecha_nacimiento
        self.__fecha_ingreso = fecha_ingreso
        self.__numero_celular = numero_celular

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def cedula(self):
        return self.__cedula

    @property
    def fecha_nacimiento (self):
        return self.__fecha_nacimiento

    @property
    def fecha_ingreso(self):
        return self.__fecha_ingreso
        
    @property
    def numero_celular(self):
        return self.__numero_celular
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if all(c.isalpha() or c.isspace() for c in nuevo_nombre):
            self.__nombre = nuevo_nombre

    @apellido.setter
    def apellido(self, nuevo_apellido):
        if all(c.isalpha() or c.isspace() for c in nuevo_apellido):
            self.__apellido = nuevo_apellido
        
    @cedula.setter
    def cedula(self, nueva_cedula):
        if isinstance(nueva_cedula, int)==True and 10000000 <= nueva_cedula <= 99999999:
            self.__cedula = nueva_cedula
        
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nueva_fecha_nacimiento):
        if isinstance(nueva_fecha_nacimiento, (datetime)): 
            self.__fecha_nacimiento = nueva_fecha_nacimiento
        
    @fecha_ingreso.setter
    def fecha_ingreso(self, nueva_fecha_ingreso):
        if isinstance(nueva_fecha_ingreso, (datetime)):
            self.__fecha_ingreso = nueva_fecha_ingreso
        
    @numero_celular.setter
    def fecha_celular(self, nuevo_numero_celular):
        if isinstance(nuevo_numero_celular, int)==True and 100000000 <= nuevo_numero_celular <= 999999999:
            self.__numero_celular = nuevo_numero_celular        
        
    
    

        