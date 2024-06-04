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
        
        