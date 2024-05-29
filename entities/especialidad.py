class Especialidad():
    def __init__(self, nombre_especialidad, precio):
        self.__nombre_especialidad = nombre_especialidad
        self.__precio = precio

    @property
    def nombre_especialidad(self):
        return self.__nombre_especialidad

    @property
    def precio(self):
        return self.__precio
    
    