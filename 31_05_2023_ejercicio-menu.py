import os
import time
import msvcrt

lista_rut = []
lista_nom_us = []
lista_tel = []
lista_edad = []
lista_correo = []
lista_cont = []

while True:
    print(f""" Menú Jugar

        1. Crear Jugador
        2. Eliminar Jugador
        3. Ver datos Jugador
        4. Modificar correo Jugador
        5. Ver Todos Jugadores
        6. Eliminar Todos Jugadores
        7. Salir """)
    while True:
        try:
            opcion = int(input("Ingrese la opción que desea: "))
            if opcion in (1,2,3,4,5,6,7):
                break
            else:
                print("¡¡Ingrese SOLO una opción descrita en el menú!")
        except:
            print("¡¡ERROR!! Debe ingresar solo números ENTEROS!!")
    os.system ("cls")
    if opcion == 1:
        while True:
            try:
                rut = int(input("Ingrese Rut (ingrese rut sin punto ni número verificador): "))
                if len(str(rut)) >=7 and len(str(rut)) <=8:
                    break
                else:
                    print("El rut ingresado no es valido DEBE tener entre 8 y 9 dígitos!!")
            except:
                print("¡¡ERROR!! Debe ingresar un número entero!!")
        while True:
            nombre = input("Ingrese Nombre de Usuario: ")
            if len(nombre) >=3:
                break
            else:
                print("El nombre de usuario debe tener al menos 3 caracteres!!")
        while True:
            try:
                telefono = int(input("Ingrese su número teléfono (debe ingresar 9 dígitos): "))
                if len(str(telefono)) == 9:
                    break
                else:
                    print("ERROR!! Debe ingresar 9 dígitos")
            except:
                print("¡¡ERROR! Debe ingresar números enteros!!")
        while True:
            try:
                edad = int(input("Ingrese su edad: "))
                if edad >=18:
                    break
                else:
                    print("DEBE SER MAYOR A 18 AÑOS")
            except:
                print("¡¡ERROR!! Debe ingresar solo números enteros!!")
        while True:
            correo = input("Ingrese un correo: ")
            if "@" in correo:
                break
            else:
                print("Correo incorrecto!!")
        while True:
            contrasena = input("Ingrese contraseña (al menos de 6 caracteres y máximo 18): ")
            if len(contrasena.strip()) >= 6 and len(contrasena.strip()) <=18:
                break
            else:
                print("La contraseña ingresada NO es valida, debe tener al menos 6 caracteres y máximo 18!!")        
        while True:
            val_contrasena = input("vuelva a ingresar la contraseña: ")
            if val_contrasena == contrasena:
                break
            else:
                print("La contraseña ingresada no coincide")
        
        lista_rut.append (rut)
        lista_nom_us.append (nombre)
        lista_tel.append (telefono)
        lista_edad.append (edad)
        lista_correo.append (correo)
        lista_cont.append (contrasena)

        print("Usuario nuevo a sido creado con éxito!!")
        time.sleep(3)
        os.system ("cls") 
    elif opcion == 2:
        rut = int(input("Ingrese rut: "))
        if rut in lista_rut:
            for x in range(len(lista_rut)):
                if rut == lista_rut [x]:
                    posiscion_encontrada = x
                    break
            lista_rut.pop(posiscion_encontrada)
            lista_nom_us.pop(posiscion_encontrada)
            lista_tel.pop(posiscion_encontrada)
            lista_edad.pop(posiscion_encontrada)
            lista_correo.pop(posiscion_encontrada)
            lista_cont.pop(posiscion_encontrada)

            print("El USUARIO a sido ELIMINADO!!")
        else:
            print("rut ingresado NO ENCONTRADO!!")
        time.sleep(3)
        os.system ("cls")
    elif opcion == 3:
        while True:
            try:
                rut = int(input("Ingrese rut del jugador:"))
                if rut in lista_rut:
                    for x in range(len(lista_rut)):
                        if rut == lista_rut [x]:
                            posiscion_encontrada = x
                            break
                    print("Datos del Jugador: ")
                    print(lista_rut[posiscion_encontrada])
                    print(lista_nom_us[posiscion_encontrada])
                    print(lista_tel[posiscion_encontrada])
                    print(lista_edad[posiscion_encontrada])
                    print(lista_correo[posiscion_encontrada])
                    #No ingrese la lista de contraseña por temas de seguridad
                else:
                    print("El rut ingresado no se encuentra registrado!")
            except:
                print("ERROR!! Debe ingresar solo números enteros!!!")
            time.sleep(5)
            os.system ("cls")
    elif opcion == 4:
        while True:
            try:
                rut = int(input("Ingrese rut del jugador:"))
                if rut in lista_rut:
                    for x in range(len(lista_rut)):
                        if rut == lista_rut [x]:
                            posiscion_encontrada = x
                            break
                    correo_n = input("Ingrese nuevo correo: ")
                    if "@" in correo:
                            break
                    else:
                        print("Correo incorrecto!!")
                    lista_correo[posiscion_encontrada] = correo_n
                    print("El correo a sido actualizado correctamente!!")                  
                else:
                    print("El rut ingresado no se encuentra registrado!")
            except:
                print("ERROR!! Debe ingresar solo números enteros!!!")
        time.sleep(5)
        os.system ("cls")
    elif opcion == 5:
        while True:
            try:
                opcion_vista = int(input("Desea ver la lista de usuarios (1.SI o 2.NO)?"))
                if opcion_vista in (1,2):
                    if opcion_vista == 1:
                        print ("Nombres de usuarios: ")
                        print(lista_nom_us)
                        print(lista_edad)
                        break
                    else:
                        break
                else:
                    print("¡¡Ingrese SOLO una de las opciones (1 o 2)")
            except:
                print ("¡¡ERROR!! Debe ingresar solo números ENTEROS!!")

    elif opcion == 6:
        while True:
            try:
                opcion_eliminar = int(input("Desa ELIMINAR A TODOS los usuarios (1.SI o 2.NO)??"))
                if opcion_eliminar in (1,2):
                    if opcion_eliminar == 1:
                        print ("SE ELIMINARAN TODOS LOS USUARIOS")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("..")
                        time.sleep(1)
                        print("...")
                        time.sleep(1)
                        os.system("cls")

                        lista_rut.pop(posiscion_encontrada)
                        lista_nom_us.pop(posiscion_encontrada)
                        lista_tel.pop(posiscion_encontrada)
                        lista_edad.pop(posiscion_encontrada)
                        lista_correo.pop(posiscion_encontrada)
                        lista_cont.pop(posiscion_encontrada)

                        print ("SE ELIMINARON TODOS LOS DATOS DE LOS USUARIOS")
                else:
                    print("¡¡Ingrese SOLOS una de las opciones (1 o 2)")
            except:
                print("ERROR!! Ingrese SOLO números enteros!!")
            time.sleep(3)
            os.system ("cls")

    else:
        exit
