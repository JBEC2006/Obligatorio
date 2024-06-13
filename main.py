from entities.policlinica import Policlinica
from exceptions.error_tipeo import ErrorTipeo
from exceptions.entidad_ya_existe import EntidadYaExiste
from exceptions.entidad_no_existe import EntidadNoExiste
from datetime import datetime



def dar_alta_especialidad():
        repetir1 = True
        repetir2 = True
        while repetir1:
            try:
                nombre_especialidad = input("Ingrese el nombre de la especialidad :")
                if not all(c.isalpha() or c.isspace() for c in nombre_especialidad) or nombre_especialidad == "":       #si no hay escrito texto, con o sin espacio
                    raise ErrorTipeo("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
                else:
                     for especialidad_buscar in policlinica.lista_de_especialidades:
                          if especialidad_buscar.nombre_especialidad == nombre_especialidad:
                               raise EntidadYaExiste ("Esta especialidad ya está ingresada")
                     break     
            except ErrorTipeo as e:
                 print (e)
            except EntidadYaExiste as e:
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
              else: 
                   for socio_buscar in policlinica.lista_de_socios:
                          if socio_buscar.cedula == cedula:
                               raise EntidadYaExiste ("Este socio ya está ingresado")
                   break
         except ErrorTipeo as e:
                print (e)
         except EntidadYaExiste as e:
              print(e)
         except ValueError as e :
              print ("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
              
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
              tipo = int(input("Ingrese el tipo de socio: 1- bonificado 2- no bonificado:"))
              if tipo!=1 and tipo!=2:
                   raise ValueError ("El valor ingresado no es correcto, elija la opción 1 o 2.") 
              else:break
         except ValueError as e:
              print ("El valor ingresado no es correcto, elija la opción 1 o 2.")
    policlinica.dar_alta_socio_mini(nombre_socio, apellido_socio, cedula, fecha_nacimiento_formato, fecha_de_ingreso_formato, celular_socio, tipo)
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
              else: 
                    for buscar_medico in policlinica.lista_de_medicos:
                        if buscar_medico.cedula == cedula:
                             raise EntidadYaExiste ("Este médico ya está ingresado")
                    break
          except EntidadYaExiste as e:
               print (e)
          except ErrorTipeo as e:
               print (e)
          except ValueError as e:
               print("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")
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
         except ValueError as e:
              print ("No es un número de celular válido, ingrese un número con el formato 09XXXXXXX")
    while repetir7:
         try:
              especialidad = input("Ingrese la especialidad :")
              if not all(c.isalpha() or c.isspace() for c in especialidad) or especialidad == "":
                    raise ErrorTipeo("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
              else:
                encontrado = False
                for especialidad_buscar in policlinica.lista_de_especialidades:
                    if especialidad_buscar.nombre_especialidad == especialidad:  #para comparar el nombre de cada uno, y no un objeto con el nombre
                        encontrado = True
                        policlinica.dar_alta_medico_mini(nombre_medico, apellido_medico, cedula, fecha_nacimiento, fecha_de_ingreso, celular_medico, especialidad)
                        print ("El médico se dio de alta con éxito.")
                        repetir7 = False
                        break
                    
                if not encontrado:
                    repetir7_mini=True
                    while repetir7_mini:
                         try:
                              print("Esta especialidad no está dada de alta.")
                              print ("1 - Volver a ingresar la especialidad")
                              print ("2 - Dar de alta esta especialidad")
                              opcion=(input("Elija una opción: "))
                              if opcion == "1":
                                   repetir7_mini = False                                                        
                              elif opcion == "2":
                                   dar_alta_especialidad()
                                   repetir7_mini = False
                              else:
                                   raise ErrorTipeo ("El valor ingresado no es correcto, ingrese 1 o 2")
                         except ErrorTipeo as e:
                              print (e)                       
         except ErrorTipeo as e:
                            print (e)
         except ValueError as e:
              print(e)


def dar_alta_consulta():
     repetir1 = True
     repetir2 = True
     repetir3 = True
     repetir4 = True
              

     while repetir1:
         try:
              especialidad = input("Ingrese la especialidad :")
              if not all(c.isalpha() or c.isspace() for c in especialidad) or especialidad == "":
                    raise ErrorTipeo("El nombre de la especialidad es incorrecto, ingréselo nuevamente")
              else:
                encontrado = False
                for especialidad_buscar in policlinica.lista_de_especialidades: 
                    if especialidad_buscar.nombre_especialidad == especialidad:  #para comparar el nombre de cada uno, y no un objeto con el nombre
                        encontrado = True
                        repetir1 = False
                        break
                if not encontrado:
                    repetir1_mini = True
                    while repetir1_mini:
                         try:
                              print("Esta especialidad no está dada de alta")
                              print ("1 - Volver a ingresar la especialidad")
                              print ("2 - Dar de alta esta especialidad")
                              opcion=(input("Elija una opción: "))
                              if opcion == "1":
                                   repetir1_mini = False                                                       
                              elif opcion == "2":
                                   dar_alta_especialidad()
                                   repetir1_mini = False
                              else:
                                   raise ErrorTipeo ("El valor ingresado no es correcto, ingrese 1 o 2.")
                         except ErrorTipeo as e:
                              print (e)
                                                
         except ErrorTipeo as e:
               print (e)

     while repetir2:
          try:
               nombre_medico = input("Ingrese el nombre completo del médico :")
               if not all(c.isalpha() or c.isspace() for c in nombre_medico) or nombre_medico == "":
                         raise ErrorTipeo("El nombre del medico es incorrecto, ingréselo nuevamente")
               else:
                    encontrado = False
                    for medico_a_buscar in policlinica.lista_de_medicos: 
                         if medico_a_buscar.nombre +" "+ medico_a_buscar.apellido == nombre_medico:  #para comparar el nombre de cada uno, y no un objeto con el nombre
                              encontrado = True                       #se pone.nombre para que sepa que tiene que comparar eso de la lista
                              repetir2 = False
                              break                    
                    if not encontrado:
                         repetir2_mini = True
                         while repetir2_mini:
                              try:
                                   print("Este medico no está dado de alta")
                                   print ("1 - Volver a ingresar el nombre del medico")
                                   print ("2 - Dar de alta el medico")
                                   opcion=(input("Elija una opción: "))
                                   if opcion == "1":
                                        repetir2_mini = False                                                        
                                   elif opcion == "2":
                                        dar_alta_medico()
                                        repetir2_mini = False
                                   else:
                                        raise ErrorTipeo ("El valor ingresado no es correcto, vuelva a elegir una opción.")
                              except ErrorTipeo as e:
                                   print (e)
          except ErrorTipeo as e:
               print(e)
     
     while repetir3:
          try:
              fecha_consulta = input("Ingrese la fecha de la consulta en en formato aaaa-mm-dd:")
              fecha_consulta_formato = datetime.strptime(fecha_consulta, "%Y-%m-%d")
              break
          except ValueError as e:
              print ("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
              
     while repetir4:
          try:
               cantidad_pacientes = int(input("Ingrese la cantidad de pacientes que se atenderán :"))
               turno = []
               for i in range (cantidad_pacientes):
                    turno.append(i+1)
               policlinica.dar_alta_consulta_mini(especialidad, nombre_medico, fecha_consulta, turno)
               repetir4 = False
          except ValueError as e:
               print ("La cantidad de los pacientes no es válida, ingrese un número.")          
              
def emitir_ticket():
     repetir1 = True
     repetir2 = True
     repetir3 = True
     repetir2_mini = True
     
     while repetir1:
          try: 
               encontrado = []          #matriz donde se guarda la posicion de las consultas en la lista real"
               tuco_numero = 0
               tuco = False
               lista_consultas_especialidad = []
               especialidad = input("Ingrese la especialidad :")
               if not all(c.isalpha() or c.isspace() for c in especialidad) or especialidad== "":
                              raise ErrorTipeo("La especialidad debe ser un string")
               else:
                    for especialidad_a_buscar in policlinica.lista_de_especialidades:
                         if especialidad_a_buscar.nombre_especialidad == especialidad :
                              for posicion,especialidad_variable in enumerate(policlinica.lista_de_consultas): #en posicion se guarda la posicion por el enumerate, y en esp_variable el objeto
                                   if especialidad_variable.especialidad == especialidad:
                                        tuco_numero += 1
                                        lista_consultas_especialidad.append([f"{tuco_numero} - Doctor: {especialidad_variable.nombre_medico}", f"Día de la consulta: {especialidad_variable.fecha_consulta} "])                
                                        encontrado.append(posicion)                    
                                        tuco = True
                              if lista_consultas_especialidad==[]:
                                   print("No hay consultas para esa especialidad, te enviaremos al menú.")
                                   repetir1 = False
                                   tuco = True
                                   repetir2 = False
                                   repetir2_mini = False
                                   repetir3 = False
                              else:
                                   print(lista_consultas_especialidad)          
                                   repetir1 = False
                    if tuco == False:
                         repetir1_mini = True
                         while repetir1_mini:
                              try:
                                   print("Esta especialidad no está dada de alta.")
                                   print ("1 - Volver a ingresar la especialidad")
                                   print ("2 - Dar de alta la especialidad")
                                   opcion=(input("Elija una opción: "))
                                   if opcion == "1":           
                                        repetir1_mini=False                                             
                                   elif opcion == "2":
                                        dar_alta_especialidad()
                                        repetir1_mini=False
                                   else:
                                        raise ErrorTipeo ("El valor ingresado no es correcto, ingrese 1 o 2.")
                              except ErrorTipeo as e:
                                   print (e)
          except ErrorTipeo as e:
               print (e)
     
     turno = None
     while repetir2:
          try: 
               opcion = int(input("Seleccione la opción deseada: "))
               if  0<opcion<=tuco_numero:
                    consulta = (policlinica.lista_de_consultas[encontrado[opcion-1]]) #accedo a la posicion-1 de encontrado, que tambien es un numero y se refiere a la consulta que me sirve
                    print(consulta.cantidad_pacientes)
                    repetir2 = False
               else:
                    raise (ValueError, TypeError) ("Esa opción no es válida, ingrésela de nuevo.")
          except (ValueError, TypeError) as e:
               print ("Esa opción no es válida, ingrésela de nuevo.")
   
     while repetir2_mini:
          try:
               opcion2 = int(input("Seleccione el numero de atención deseado :"))
               if opcion2 not in consulta.cantidad_pacientes:
                    raise (ValueError, TypeError) ("Esta opción no está disponible, elija un turno de los que aparecen en pantalla.")
               else:
                    turno = opcion2
                    repetir2_mini = False
          except (ValueError, TypeError) as e:
               print ("Esta opción no está disponible, elija un turno de los que aparecen en pantalla.")

     while repetir3:
          try:
               cedula = int(input("Ingrese la cédula de identidad del socio sin puntos ni guiones:")) 
               if cedula>99999999 or cedula<10000000:
                   raise ErrorTipeo("No es una cédula válida, ingrese nuevamente una cédula de 8 dígitos.")                              
               else: 
                   x = False
                   for socio_buscar in policlinica.lista_de_socios:
                          if socio_buscar.cedula == cedula:
                              x = True
                              precio_socio = None
                              for especialidad_buscar in policlinica.lista_de_especialidades:
                                   if consulta.especialidad == especialidad_buscar.nombre_especialidad:
                                        if socio_buscar.tipo == 1:    
                                             precio_socio = (especialidad_buscar.precio)*0.8
                                             socio_buscar.deuda += precio_socio
                                        if socio_buscar.tipo == 2:
                                             precio_socio = especialidad_buscar.precio     
                                             socio_buscar.deuda += precio_socio                              
                                   break
                              print (socio_buscar.deuda)
                              print (precio_socio)    
                              policlinica.lista_de_tickets.append([cedula, consulta.nombre_medico, turno, precio_socio])
                              consulta.cantidad_pacientes.remove(turno)             #para que saque el numero de turnos del array de la lista de pacientes
                              repetir3 = False
                   if x == False:
                        repetir3_mini = True
                        while repetir3_mini:
                              try:
                                   print("Este socio no está dada de alta")
                                   print ("1 - Volver a ingresar el socio")
                                   print ("2 - Dar de alta el socio")
                                   opcion=(input("Elija una opción: "))
                                   if opcion == "1":           
                                        repetir3_mini=False                                             
                                   elif opcion == "2":
                                        dar_alta_socio()
                                        repetir3_mini=False
                                   else:
                                        raise ErrorTipeo ("El valor ingresado no es correcto, ingrese 1 o 2.")
                              except ErrorTipeo as e:
                                   print (e)
                                  
          except ErrorTipeo as e:
               print (e)
               
               



def realizar_consulta():
     repetir_menu = True
     repetir1 = True
     repetir2 = True
     repetir2_mini = True
     repetir4 = True
     repetir4_1 = True
     repetir4_2 = True
     repetir5_1 = True
     repetir5_2 = True
     while repetir_menu:
          try:
               print("1. Obtener todos los médicos asociados a una especialidad específica.")
               print("2. Obtener el precio de una consulta de una especialidad especifico")
               print("3. Listar todos los socios con sus deudas asociadas en orden ascendente")
               print("4. Realizar consultas respecto a cantidad de consultas entre dos fechas.")
               print("5. Realizar consultas respecto a las ganancias obtenidas  entre dos fechas.")
               print("6. Salir.")
               pregunta_inicial = int(input("selecciones una opcion :"))
               if pregunta_inicial != 1 and pregunta_inicial != 2 and pregunta_inicial != 3 and pregunta_inicial != 4 and pregunta_inicial != 5 and pregunta_inicial !=6:
                    raise (ValueError, TypeError)("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")
               if pregunta_inicial==1:
                    while repetir1:
                         try:
                              encontrado=False
                              medicos_de_la_especialidad_a_mostar=[]
                              especialidad=input("Ingrese la especialidad :")
                              if not all(c.isalpha() or c.isspace() for c in especialidad):
                                   raise ErrorTipeo("La especialidad no puede ser un numero o un string vacio, vuelva a ingresarla")
                              for especialidad_a_buscar in policlinica.lista_de_medicos:
                                   if especialidad_a_buscar.especialidad==especialidad:
                                        encontrado=True
                                        medicos_de_la_especialidad_a_mostar.append([especialidad_a_buscar.nombre +" "+ especialidad_a_buscar.apellido])
                              if encontrado==True:
                                   repetir1=False
                                   print (medicos_de_la_especialidad_a_mostar)
                              if encontrado==False:
                                   print("la especialidad ingresada no esta dada de alta")
                                   repetir1=False    
                         except ErrorTipeo as e:
                              print(e)
               if pregunta_inicial ==2:
                         while repetir2:
                              try:
                                   especialidad=input("Ingrese la especialidad:")
                                   if not all(c.isalpha() or c.isspace() for c in especialidad):
                                        raise ErrorTipeo ("La especialidad no puede ser un numero o un string vacio, vuelva a ingresarla.")
                                   for especialidad_a_buscar in policlinica.lista_de_especialidades:
                                        if especialidad_a_buscar.nombre_especialidad==especialidad:
                                             encontrado=True
                                             precio_incial=especialidad_a_buscar.precio
                                   if encontrado==True:
                                        while repetir2_mini:
                                             try:
                                                  repetir2 = False
                                                  tipo_de_socio=int(input("Ingrese tipo de socio; 1- bonificado , 2- no bonificado: "))                                                      
                                                  if tipo_de_socio==1:
                                                       precio_final=precio_incial*0.8
                                                       print (f"El precio para una consulta de {especialidad} es {precio_final}.")
                                                       repetir2_mini=False
                                                  if tipo_de_socio==2:
                                                       print (f"El precio para una consulta de {especialidad} es {precio_incial}.")
                                                       repetir2_mini=False
                                                  else:
                                                       raise ErrorTipeo ("El tipo de socio solo puede ser 1- bonificado, 2- no bonificado, por favor ingrese 1 o 2")
                                             except ErrorTipeo as e:
                                                  print (e)                                  
                                   if encontrado==False:
                                             print("Esta especialidad no esta dada de alta")
                                             repetir2=False
                              except ErrorTipeo as e:
                                   print(e)

               if pregunta_inicial ==3:
                    lista_deudas = []
                    for socio_buscar in policlinica.lista_de_socios:
                         lista_deudas.append([socio_buscar.nombre +" "+ socio_buscar.apellido, socio_buscar.deuda])
                    lista_ordenada = sorted(lista_deudas, key=lambda x: x[1])   #x[1] se refiere a las deudas, lambda toma una tupla ej:(Juan, 200) y devuelve el segundo valor     
                    print (lista_ordenada)
              
               if pregunta_inicial ==4:
                    while repetir4_1:
                         try:
                              fecha_inicial= input("Ingrese la fecha inicial en formato aaaa-mm-dd :")
                              fecha_inicial_formato = datetime.strptime(fecha_inicial, "%Y-%m-%d")
                              repetir4_1=False
                         except ValueError as e:
                              print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                    while repetir4_2:
                         try:    
                              fecha_final=input("Ingrese la fecha inicial en formato aaaa-mm-dd :")
                              fecha_final_formato = datetime.strptime(fecha_final, "%Y-%m-%d")
                              repetir4_2=False
                         except ValueError as e:
                              print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                    cantidad = 0
                    for consulta in policlinica.lista_de_consultas:
                         if fecha_inicial<=consulta.fecha_consulta<=fecha_final:
                              cantidad =+ 1
                    print(f"La cantidad de consultas entre {fecha_inicial} y {fecha_final} es {cantidad}")
                                        
                                        
               if pregunta_inicial ==5:
                    while repetir5_1:
                         try:
                              fecha_inicial= input("Ingrese la fecha inicial en formato aaaa-mm-dd :")
                              fecha_inicial_formato = datetime.strptime(fecha_inicial, "%Y-%m-%d")
                              repetir4_1=False
                         except ValueError as e:
                              print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                    while repetir5_2:
                         try:    
                              fecha_final=input("Ingrese la fecha inicial en formato aaaa-mm-dd :")
                              fecha_final_formato = datetime.strptime(fecha_final, "%Y-%m-%d")
                              repetir4_2=False
                         except ValueError as e:
                              print("No es una fecha válida, vuelva a ingresarla en el formato aaaa-mm-dd.")
                    ganancias=0
                    for ganancias_u in policlinica.lista_de_tickets:
                         ganancias+=ganancias_u.precio
                    print (f"las ganancias obtenidas dentro de {fecha_inicial} y {fecha_final} fueron {ganancias}")
               #5. Realizar consultas respecto a las ganancias obtenidas entre dos fechas

                    pass
               if pregunta_inicial ==6:
                    repetir_menu=False
          except ValueError as e:
               print (e)    
          except TypeError as e:
               print (e)    
              

               

           
def menu():
    repetir=True
    while repetir:
        try:
          print("1. Dar de alta una especialidad")
          print("2. Dar de alta un socio")
          print("3. Dar de alta un médico")
          print("4. Dar de alta una consulta médica")
          print("5. Emitir un ticket de consulta")
          print("6. Realizar consultas")
          print("7. Salir del programa")
          pregunta_inicial=int(input("Seleccione una opción del menú (1/2/3/4/5/6/7): "))
          if pregunta_inicial != 1 and pregunta_inicial != 2 and pregunta_inicial != 3 and pregunta_inicial != 4 and pregunta_inicial != 5 and pregunta_inicial != 6 and pregunta_inicial != 7:
               raise (ValueError, TypeError) ("La opción ingresada no es correcta, vuelva a intentar con otra opción.")
          
          if pregunta_inicial == 1:
               dar_alta_especialidad()
          if pregunta_inicial == 2:
               dar_alta_socio()
          if pregunta_inicial == 3:
               dar_alta_medico()
          if pregunta_inicial == 4:
               dar_alta_consulta()
          if pregunta_inicial == 5:
               emitir_ticket()
          if pregunta_inicial == 6:
               realizar_consulta()
          if pregunta_inicial == 7:
               repetir=False
               print("Fin")
        except ValueError:
             print ("La opción seleccionada no es correcta, vuelva a intentar con otra opción.")
        except TypeError:
             print ("La opción seleccionada no es correcta, vuelva a intentar con otra opción.") 
if __name__ == "__main__":
    policlinica = Policlinica()
    menu()
