from abc import ABC
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
        if nuevo_nombre!="" and type(nuevo_nombre)!=int and type(nuevo_nombre)!=float:  #que el nombre no sea vacio ni numerico
            return nuevo_nombre
        
    def cambiar_nombre(self, nuevo_nombre):
        self.__nombre=nuevo_nombre  
        return nuevo_nombre

        