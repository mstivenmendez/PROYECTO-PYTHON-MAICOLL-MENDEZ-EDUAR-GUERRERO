import os
import random
import json

def leerJson(path: str):
    with open(path, mode='r') as file:
        datos = json.load(file)
        return datos
    
def escribirJson(path: str, data: list):
    with open(path,mode= 'w') as file:
        json.dump(data, file, indent= 4)

Loteria = {
    "usuarios" : []
}
Usuarios  = []






menu = """
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│     /$$       /$$                                                    /$$       /$$              │
│    | $$      |__/                                                   |__/      | $$              │
│    | $$$$$$$  /$$  /$$$$$$  /$$$$$$$  /$$    /$$  /$$$$$$  /$$$$$$$  /$$  /$$$$$$$  /$$$$$$     │
│    | $$__  $$| $$ /$$__  $$| $$__  $$|  $$  /$$/ /$$__  $$| $$__  $$| $$ /$$__  $$ /$$__  $$    │
│    | $$  \ $$| $$| $$$$$$$$| $$  \ $$ \  $$/$$/ | $$$$$$$$| $$  \ $$| $$| $$  | $$| $$  \ $$    │
│    | $$  | $$| $$| $$_____/| $$  | $$  \  $$$/  | $$_____/| $$  | $$| $$| $$  | $$| $$  | $$    │
│    | $$$$$$$/| $$|  $$$$$$$| $$  | $$   \  $/   |  $$$$$$$| $$  | $$| $$|  $$$$$$$|  $$$$$$/    │
│    |_______/ |__/ \_______/|__/  |__/    \_/     \_______/|__/  |__/|__/ \_______/ \______/     │
│                 /$$             /$$                         /$$                                 │
│                | $$            | $$                        |__/                                 │
│                | $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$  /$$  /$$$$$$                        │
│                | $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$| $$ |____  $$                       │
│                | $$| $$  \ $$  | $$    | $$$$$$$$| $$  \__/| $$  /$$$$$$$                       │
│                | $$| $$  | $$  | $$ /$$| $$_____/| $$      | $$ /$$__  $$                       │
│                | $$|  $$$$$$/  |  $$$$/|  $$$$$$$| $$      | $$|  $$$$$$$                       │
│                |__/ \______/    \___/   \_______/|__/      |__/ \_______/                       │
│                  /$$$$$$  /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$  /$$   /$$                       │
│                 /$$__  $$| $$__  $$| $$__  $$|_  $$_/ /$$__  $$| $$$ | $$                       │
│                | $$  \ $$| $$  \ $$| $$  \ $$  | $$  | $$  \ $$| $$$$| $$                       │
│                | $$$$$$$$| $$  | $$| $$$$$$$/  | $$  | $$$$$$$$| $$ $$ $$                       │
│                | $$__  $$| $$  | $$| $$__  $$  | $$  | $$__  $$| $$  $$$$                       │
│                | $$  | $$| $$  | $$| $$  \ $$  | $$  | $$  | $$| $$\  $$$                       │
│                | $$  | $$| $$$$$$$/| $$  | $$ /$$$$$$| $$  | $$| $$ \  $$                       │
│                |__/  |__/|_______/ |__/  |__/|______/|__/  |__/|__/  \__/                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
"""
def clear_screen():
    # Función para limpiar la pantalla
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/Unix

def espacio():
    print("\n" * 1)

def logos():
    print(menu)

def Menu_De_Ingreso():
    logos()
    print("---------------------------------------------------------------------------------------------------")
    print("-------------------BIENVENIDOS DONDE LAS OPOTUNIDADES DE GANAR SON TAN FACILES---------------------")
    print("----------------------------------1. REGISTRATE EN LA PAGINA --------------------------------------")
    print("----------------------------------2. INGRESAR A LA  PAGINA   --------------------------------------")
    print("----------------------------------0.         SALIR ❌           --------------------------------------")
    espacio()

def Validacion_Ingreso(mensaje: str, valorminimo: int = 0, valormaximo: int = 6):


    # Función para validar el ingreso de datos
    while True:
        try:
            valor = int(input(mensaje))
            if valorminimo <= valor <= valormaximo:
                return valor
            else:
                print(f"POR FAVOR INGRESE VALORES ENTRE {valorminimo} y {valormaximo}.")
        except:
            print("ENTRADA NO VALIDA POR FAVOR INGRESE NUMEROS")

def Validar_Texto(mensaje: str):
    while True:
        valor = input(mensaje)
        suplente = valor.replace(" ", "")
        if suplente.isalpha() == True :
            valor = valor.upper()
            return valor
            break
        else:
            print("ENTRADA NO VALIDAD INGRESE SOLO LETRAS")
            continue

def Validacion_Menu_Ingreso(mensaje: str, valorminimo: int = 0, valormaximo: int = 6):
     while True:
        try:
            valor = int(input(mensaje))
            if valorminimo <= valor <= valormaximo:
                return valor
            else:
                print(f"POR FAVOR INGRESE VALORES ENTRE {valorminimo} y {valormaximo}.")
                Menu_De_Ingreso()
        except:
            print("ENTRADA NO VALIDA POR FAVOR INGRESE NUMEROS")
            Menu_De_Ingreso()

def Validacion_Menu_Usuario(mensaje: str, valorminimo: int = 0, valormaximo: int = 6):
     while True:
        try:
            valor = int(input(mensaje))
            if valorminimo <= valor <= valormaximo:
                return valor
            else:
                print(f"POR FAVOR INGRESE VALORES ENTRE {valorminimo} y {valormaximo}.")
                Menu_Usuario()
        except:
            print("ENTRADA NO VALIDA POR FAVOR INGRESE NUMEROS")
            Menu_Usuario()
            
def Despedida():
    clear_screen()
    print("----------------- VUELVA MUY PRONTO DONDE LAS OPOTUNIDADES DE GANAR SON TAN FACILES ---------------")
    print("----------------------------------   GRACIAS POR TU VISITA   --------------------------------------")
    espacio()

def Validacion_Correo(mensaje:str):
    while True :
        email = input(mensaje)
        if not "@" in email :
            print("RECUERDA QUE TU CORREO DEBE CONTENER @")
            continue
        elif not email.islower():
            print("CORREO TIENEN LETRAS EN MAYUSCULA")
            continue
        elif any(c.isspace() for c in email):
            print("CORREO TIENE ESPACIOS")
            continue
        print("CORREO INGRESADO CORRECTAMENTE")
        return email

def Registro_Usuarios(Cedula: int, Nombre: str, Telefono:  int, Correo: str, Usuario: str, Password: str):
    return {
        "Cedula" : Cedula,
        "Nombre" : Nombre,
        "Telefono" : Telefono,
        "Correo" : Correo,
        "Usuario" : Usuario,
        "Password" :  Password
    }

def Guardar_Usuarios(datos: dict, guardar: list):
    Nombre = Validar_Texto("INGRESE SU NOMBRE: \n")
    Cedula = Validacion_Ingreso(f"INGRESE SU CEDULA, {Nombre} :\n", 10000000, 100000000000)
    Telefono = Validacion_Telefono(f"INGRESE SU NUMERO, {Nombre} :\n")
    Correo = Validacion_Correo(f"INGRESE SU CORREO, {Nombre} :\n")
    Usuario = Validar_Texto(f"INGRESE SU USUARIO : {Nombre} \n")
    Password = Verificacion_Contraseña(f"INGRESE SU CONTRASEÑA {Nombre} \n")
    datos = Registro_Usuarios(
        Cedula=Cedula,
        Nombre=Nombre,
        Telefono=Telefono,
        Correo=Correo,
        Usuario=Usuario,
        Password=Password
    )

    guardar.append(datos)  

def Validacion_Telefono(mensaje: str):
    while True: 
        try:
            telefono = int(input(mensaje))
            lista = [int(digito) for digito in str(telefono)]
            numero = len(lista)
            if lista[0] != 3:
                print("RECUERDA QUE SU NUMERO DEBE INICIAR EN 3")
            elif numero != 10  :
                print("RECUERDA QUE SU NUMERO DEBE DEBE CONTENER 10 DIGITOS")
            elif numero  == 10 and lista[0] == 3:
                print("TU NUMERO HA SIDO INGRESADO")
                return telefono 
                break
            else:
                print("RECUERDA QUE SU NUMERO NO DEBE TENE LETRAS ")
        except:
            print("INGRESE SOLO NUMEROS")

def Menu_Usuario():
    print("------------------------------------------------😄-------------------------------------------------")
    print("------------------BIENVENIDOS DONDE LAS OPOTUNIDADES DE GANAR SON TAN FACILES 🌟 ------------------")
    espacio()
    print("----------------------------1. COMPRAR BOLETOS 🎟️                      ----------------------------")
    print("----------------------------2. BOLETOS COMPRADOS 🎟️                    ----------------------------")
    print("----------------------------3. VER HOSTORIAL DE NUMEROS GANADORES 🎉   ----------------------------")
    print("----------------------------4. VER HISTORIAL DE BOLETAS JUGADOS 📜     ----------------------------")
    print("----------------------------5. VER HISTORIAL CON ACIERTOS POR BOLETO 🎯----------------------------")
    print("----------------------------0. SALIR  ❌                               ----------------------------")   

def Menu_Sub_Menu_Boletas():
    logos()
    print("--------------------------------------------------😄-----------------------------------------------")
    print("------------------BIENVENIDOS DONDE LAS OPOTUNIDADES DE GANAR SON TAN FACILES 🌟-------------------")
    print("----------------------------   COMPRADO BOLETOS 🎟️                     ----------------------------")
    espacio()
    print("----------------------------- 1. COMPRAR NUMEROS ALEATORIAMENTE🎲 ---------------------------------")
    print("------------------------------2. COMPRAR INGRESANDO EL NUMERO 🎟️  ---------------------------------")
    print("------------------------------0. SALIR ❌                         ---------------------------------")

def Menu_Sub_Menu_Aciertos():
    logos() 
    print("------------------------------------------------😄------------------------------------------------")
    print("-----------------BIENVENIDOS DONDE LAS OPOTUNIDADES DE GANAR SON TAN FACILES 🌟-------------------")
    espacio()
    print("----------------------------1. PREMIO BRONCE 🥉          -----------------------------------------")
    print("----------------------------2. PREMIO PLATA  🥈          -----------------------------------------")
    print("----------------------------3. PREMIO ORO 🥇             -----------------------------------------")
    print("----------------------------4. GRAN PREMIO 🏆            -----------------------------------------")
    print("----------------------------5. ESTADISTICAS 📊           -----------------------------------------")
    print("----------------------------0. SALIR  ❌                 -----------------------------------------")

def Numero_Aleatorios(lista_Numeros: list):
    lista_Numeros = []
    numero = Validacion_Ingreso(f"INGRESE LOS NUMEROS QUE DESEA GENERAR :\n ",1,20) 
    for i in range(numero) :
        numeros = random.sample(range(1,49),6)
        lista_Numeros.append(numeros)

    for index, i in enumerate(lista_Numeros, start =1):
        print(f"{index}. {i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]} ")

        
    
def Verificacion_Contraseña(mensaje: str):
    while True:
        contraseña = input(mensaje)
        contraseña2 = input("CONFIRMAR TU CONTRASEÑA ")
        if contraseña == contraseña2:
            print("CONTRASEÑA GUARDADA, EXITOSAMENTE")
            return contraseña
        else:
            print("VERIFICA QUE LAS CONTRAEÑAS SEAN IGUALES")

def Ingreso_Usuario(mensaje: str):
    while True:
        Usuario = Validar_Texto(f"INGRESE SU USUARIO PARA INGRESAR A SU CUENTA : \n" )
        datos = leerJson(mensaje)
        espacio()
        for dato in datos :
            if dato["Usuario"] == Usuario:
                while True:
                    Contraseña = input("INGRESAR CONTRASEÑA \n")
                    if dato["Password"] == Contraseña :
                        logos()
                        break
                    else:
                        print("CONTRASEÑA INCORRECTA")
            else:
                print("USUARIO NO EXISTE")                  
        break






while True:
    Menu_De_Ingreso()
    Opcion_Menu = Validacion_Menu_Ingreso("INGRESE  SU OPCION\n",0,2)

    if Opcion_Menu == 1:
        Guardar_Usuarios(Loteria,Usuarios)
        escribirJson("Loteria.json",Usuarios)
    elif  Opcion_Menu == 2:
        Ingreso_Usuario("Loteria.json")
        def Proceso_Inicial():
            Menu_Usuario()
            Opcion_Usuario = Validacion_Menu_Usuario("INGRESE  SU OPCION\n",0,5)

            if  Opcion_Usuario == 1:
                Menu_Sub_Menu_Boletas()
                Opcion_Boleto = Validacion_Ingreso("INGRESE  SU OPCION\n",0,2)





    elif  Opcion_Menu == 0:
        Numero_Aleatorios()
        



