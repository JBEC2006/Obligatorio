from entities.policlinica import Policlinica
from exceptions.error_tipeo import ErrorTipeo
from datetime import datetime



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

def dar_alta_socio():
    repetir1 = True
    repetir2 = True
    repetir3 = True
    repetir4 = True
    repetir5 = True
    repetir6 = True
    repetir7 = True
    while repetir1:
          try:
               nombre_socio = input("Ingrese el nombre :")
               if not all(c.isalpha() or c.isspace() for c in nombre_socio) or nombre_socio == "":       
                    raise ErrorTipeo("No es un nombre válido, ingréselo de nuevo")
               else: break
          except ErrorTipeo as e:
               print (e)
    while repetir2:
         try:
              apellido_socio = input("Ingrese el apellido :")
              if not all(c.isalpha() or c.isspace() for c in apellido_socio) or apellido_socio == "":       
                    raise ErrorTipeo("No es un apellido válido, ingréselo de nuevo")
              else: break
         except ErrorTipeo as e:
               print (e)
    while repetir3:
         try:
              cedula = int(input("Ingrese la cédula de identidad sin puntos ni guiones:")) 
              if cedula>99999999 or cedula<10000000:
                   raise ErrorTipeo("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")                              
              else: break
         except ErrorTipeo as e:
                print (e)
    while repetir4:
         try:
              fecha_nacimiento = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd :")
              fecha_nacimiento_formato = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
              break
         except ValueError as e:
              print ("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
    while repetir5:
         try:
              fecha_de_ingreso = input("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:")
              fecha_de_ingreso_formato = datetime.strptime(fecha_de_ingreso, "%Y-%m-%d")
              break
         except ValueError as e:
              print ("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
    while repetir6:
         try:
              celular_socio = int(input("Ingrese el número de celular:"))
              celular_sin_primer_digito = int(str(celular_socio)[0:]) #Se le saca el digito de la posicion 0
              if celular_sin_primer_digito>99999999 or celular_sin_primer_digito<10000000:
              #La letra no especifica que los dos primeros digitos deberan ser "09"
                   raise ErrorTipeo("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
              else:break
         except ErrorTipeo as e:
              print (e)
    while repetir7:
         try:
              tipo = int(input("Ingrese el tipo de socio: 1- Bonificado 2- No bonificado:"))
              if tipo!=1 and tipo!=2:
                   raise ValueError ("El valor ingresado no es correcto, elija la opción 1 o 2.") 
              else:break
         except ValueError as e:
              print ("El valor ingresado no es correcto, elija la opción 1 o 2.")
    policlinica.dar_alta_socio_mini(nombre_socio, apellido_socio, cedula, fecha_nacimiento_formato, fecha_de_ingreso_formato, tipo, celular_socio)
    print ("Se registró el socio con éxito")

def dar_alta_medico():
    repetir1 = True
    repetir2 = True
    repetir3 = True
    repetir4 = True
    repetir5 = True
    repetir6 = True
    repetir7 = True
    while repetir1:
          try:
               nombre_medico = input("Ingrese el nombre :")
               if not all(c.isalpha() or c.isspace() for c in nombre_medico) or nombre_medico == "":       
                    raise ErrorTipeo("No es un nombre válido, ingréselo de nuevo")
               else: break
          except ErrorTipeo as e:
               print (e)
    while repetir2:
         try:
              apellido_medico = input("Ingrese el apellido :")
              if not all(c.isalpha() or c.isspace() for c in apellido_medico) or apellido_medico == "":       
                    raise ErrorTipeo("No es un apellido válido, ingréselo de nuevo")
              else: break
         except ErrorTipeo as e:
               print (e)
    while repetir3:
         try:
              cedula = int(input("Ingrese la cédula de identidad sin puntos ni guiones:")) 
              if cedula>99999999 or cedula<10000000:
                   raise ErrorTipeo("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")                              
              else: break
         except ErrorTipeo as e:
                print (e)
    while repetir4:
         try:
              fecha_nacimiento = input("Ingrese la fecha de nacimiento en formato aaaa-mm-dd :")
              fecha_nacimiento_formato = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
              break
         except ValueError as e:
              print ("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
    while repetir5:
         try:
              fecha_de_ingreso = input("Ingrese la fecha de ingreso a la institución en formato aaaa-mm-dd:")
              fecha_de_ingreso_formato = datetime.strptime(fecha_de_ingreso, "%Y-%m-%d")
              break
         except ValueError as e:
              print ("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
    while repetir6:
         try:
              celular_medico = int(input("Ingrese el número de celular:"))
              celular_sin_primer_digito = int(str(celular_medico)[0:]) #Se le saca el digito de la posicion 0
              if celular_sin_primer_digito>99999999 or celular_sin_primer_digito<10000000:
              #La letra no especifica que los dos primeros digitos deberan ser "09"
                   raise ErrorTipeo("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
              else:break
         except ErrorTipeo as e:
              print (e)
    while repetir7:
         try:
              especialidad = input("Ingrese la especialidad :")
              if not all(c.isalpha() or c.isspace() for c in especialidad) or especialidad == "":
                    raise ErrorTipeo("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
              else:
                  for especialidad_buscar in policlinica.lista_de_especialidades: #hay que revisar que funque
                     if especialidad_buscar == especialidad:
                        especialidad=especialidad_buscar
                        policlinica.dar_alta_medico_mini(nombre_medico, apellido_medico, cedula, fecha_nacimiento, fecha_de_ingreso, celular_medico, especialidad)
                        print ("El médico se dio de alta con éxito")
                     else:
                        print("Esta especialidad no está dada de alta")
                        print ("1 - Volver a ingresar la especialidad")
                        print ("2 - Dar de alta esta especialidad")
                        opcion=int(input("Elija una opción: "))
                        if opcion == 1:
                            pass                                                        
                        elif opcion == 2:
                             dar_alta_especialidad()
                             break
                                                
         except ErrorTipeo as e:
                            print (e)
              
     
              
    
               

           
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
            dar_alta_socio()
        if pregunta_inicial == 3:
            dar_alta_medico()
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