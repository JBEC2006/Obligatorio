import datetime

class Consulta():
    def __init__ (self, especialidad, nombre_medico, fecha_consulta ,cantidad_pacientes):
        self.__especialidad = especialidad
        self.__nombre_medico = nombre_medico
        self.__fecha_consulta = fecha_consulta
        self.__cantidad_pacientes = cantidad_pacientes

    @property 
    def especialidad(self):
        return self.__especialidad

    @property 
    def nombre_medico(self):
        return self.__nombre_medico

    @property 
    def cantidad_pacientes(self):
        return self.__cantidad_pacientes
    
    @property 
    def fecha_consulta(self):
        return self.__fecha_consulta
    
    @especialidad.setter
    def especialidad(self, nueva_especialidad):
        if all(c.isalpha() or c.isspace() for c in nueva_especialidad):
            self.__especialidad = nueva_especialidad

    @nombre_medico.setter
    def nombre_medico(self, nuevo_nombre_medico):
        if all(c.isalpha() or c.isspace() for c in nuevo_nombre_medico):
            self.__nombre_medico = nuevo_nombre_medico

    @fecha_consulta.setter
    def fecha_consulta(self, nueva_fecha_consulta):
        if isinstance(nueva_fecha_consulta, (datetime)): 
            self.__fecha_consulta = nueva_fecha_consulta
        
    @cantidad_pacientes.setter
    def cantidad_pacientes(self, nueva_cantidad_de_pacientes):
        if isinstance(nueva_cantidad_de_pacientes, int)==True and nueva_cantidad_de_pacientes>=0:
            self.__cantidad_pacientes = nueva_cantidad_de_pacientes
