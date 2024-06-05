from entities.especialidad import Especialidad
from entities.socio import Socio
from entities.medico import Medico
from entities.consulta import Consulta

class Policlinica:
    def __init__(self):
        self.__lista_de_medicos = []
        self.__lista_de_socios = []
        self.__lista_de_especialidades = []
        self.__lista_de_consultas = []

    @property
    def lista_de_especialidades(self):
        return self.__lista_de_especialidades

    @property
    def lista_de_socios(self):
        return self.__lista_de_socios
    
    @property
    def lista_de_medicos(self):
        return self.__lista_de_medicos
    
    @property
    def lista_de_consultas(self):
        return self.__lista_de_consultas
    
    
    
    def dar_alta_especialidad_mini(self, nombre_especialidad, precio):
        especialidad = Especialidad(nombre_especialidad, precio)        #crea un objeto especialidad parea agregarlo a la lista
        self.__lista_de_especialidades.append(especialidad)
        
    def dar_alta_socio_mini(self, nombre_socio, apellido, cedula, fecha_nacimiento, fecha_ingreso, tipo, celular):
        socio = Socio(nombre_socio, apellido, cedula, fecha_nacimiento, fecha_ingreso, tipo, celular)
        self.__lista_de_socios.append(socio)

    def dar_alta_medico_mini(self, nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, numero_celular, especialidad):
        medico = Medico(nombre, apellido, cedula, fecha_nacimiento, fecha_ingreso, numero_celular, especialidad)
        self.__lista_de_medicos.append(medico)
    
    def dar_alta_consulta_mini(self, especialidad, nombre_medico, fecha_consulta, cantidad_pacientes):
        consulta = Consulta(especialidad, nombre_medico, fecha_consulta, cantidad_pacientes)
        self.__lista_de_consultas.append(consulta)