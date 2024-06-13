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
    
    @nombre_especialidad.setter
    def nombre_especialidad(self, nuevo_nombre_especialidad):
        if all(c.isalpha() or c.isspace() for c in nuevo_nombre_especialidad):
            self.__nombre_especialidad = nuevo_nombre_especialidad 

    @precio.setter
    def precio(self, nuevo_precio):
        if isinstance(nuevo_precio, int)==True:
            self.__precio = nuevo_precio