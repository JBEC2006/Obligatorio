from entities.especialidad import Especialidad
from entities.socio import Socio

class Policlinica:
    def __init__(self):
        self.__lista_de_medicos = []
        self.__lista_de_socios = []
        self.__lista_de_especialidades = []

    @property
    def lista_de_especialidades(self):
        return self.__lista_de_especialidades

    @property
    def lista_de_socios(self):
        return self.__lista_de_socios
    
    @property
    def lista_de_medicos(self):
        return self.__lista_de_medicos
    
    
    
    def dar_alta_especialidad_mini(self, nombre_especialidad, precio):
        especialidad = Especialidad(nombre_especialidad, precio)        #crea un objeto esp parea agregarlo a la lista
        self.__lista_de_especialidades.append(especialidad)
        
    def dar_alta_socio_mini(self, nombre_socio, apellido, cedula, fecha_nacimiento, fecha_ingreso, tipo, celular):
        socio = Socio(nombre_socio, apellido, cedula, fecha_nacimiento, fecha_ingreso, tipo, celular)
        self.__lista_de_socios.append(socio)
