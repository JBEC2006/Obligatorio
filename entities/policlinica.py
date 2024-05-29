
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
        self.__lista_de_especialidades.append(nombre_especialidad, precio)
        

