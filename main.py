# Menú principal:
# El menú principal deberá continuar en loop hasta que el usuario ingrese una opción válida o la
# opción salir del programa.
# Seleccione una opción del menú:
# 1. Dar de alta una especialidad
# 2. Dar de alta un socio
# 3. Dar de alta un médico
# 4. Dar de alta una consulta médica
# 5. Emitir un ticket de consulta
# 6. Realizar consultas
# 7. Salir del programa

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
        
        

    
        if pregunta_inicial==7:
            repetir=False
            print("Fin")
            
if __name__ == "__main__":
    menu()