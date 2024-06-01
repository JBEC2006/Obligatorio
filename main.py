from entities.policlinica import Policlinica
from entities.socio import Socio
from exceptions.error_tipeo import ErrorTipeo



def dar_alta_especialidad():
        repetir1 = True
        repetir2 = True
        while repetir1:
            try:
                nombre_especialidad = input("Ingrese el nombre de la especialidad :")
                if not all(c.isalpha() or c.isspace() for c in nombre_especialidad) or nombre_especialidad == "":       #si no hay escrito texto, con o sin espacio
                    raise ErrorTipeo("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                else: break
                    
            except ErrorTipeo as e:
                            print (e)

        while repetir2:
            try:                                                                              
                precio = int(input("Ingrese el precio asociado :"))                               
                repetir2 = False
                print("la especialidad se ha creado con exito")
                policlinica.dar_alta_especialidad_mini(nombre_especialidad, precio)
            except ValueError as e:
                print ("El precio de la especialidad es incorrecto, ingréselo nuevamente")

def alta_socio():
     pass

           
def menu():
    repetir=True
    while repetir:
        print("1. Dar de alta una especialidad")
        print("2. Dar de alta un socio")
        print("3. Dar de alta un médico")
        print("4. Dar de alta una consulta médica")
        print("5. Emitir un ticket de consulta")
        print("6. Realizar consultas")
        print("7. Salir del programa")
        pregunta_inicial= int(input("Seleccione una opción del menú (1/2/3/4/5/6/7): "))
        if pregunta_inicial != 1 and pregunta_inicial != 2 and pregunta_inicial != 3 and pregunta_inicial != 4 and pregunta_inicial != 5 and pregunta_inicial != 6 and pregunta_inicial != 7:
            print("------------------")
            print("La opción seleccionada no es correcta, vuelva a intentar con otra opción")
            print("------------------")
        if pregunta_inicial == 1:
            dar_alta_especialidad()
        if pregunta_inicial == 2:
            alta_socio()
        if pregunta_inicial == 3:
            pass
        if pregunta_inicial == 4:
            pass
        if pregunta_inicial == 5:
            pass
        if pregunta_inicial == 6:
            pass
        if pregunta_inicial == 7:
            repetir=False
            print("Fin")
            
if __name__ == "__main__":
    policlinica = Policlinica()
    menu()