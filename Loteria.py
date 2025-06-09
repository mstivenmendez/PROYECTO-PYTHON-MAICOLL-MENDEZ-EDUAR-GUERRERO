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
numeros_boletas = []
Nombre_Usuario ="MSTIVEN"
global Admin 
Admin = "ADMINISTRADOR"
Boleta_Ganadora ="5-12-23-34-41-48"






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
        "Password" :  Password,
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
    print(f"-----------------------BIENVENIDO A NUESTRA LOTERIA {Nombre_Usuario} 🌟 -------------------------")
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

def Agregar_Boletos_Usuario(usuario_nombre: str, datos: str):
    usuarios = leerJson(datos)
    lista_Numeros = []
    numero = Validacion_Ingreso("¿CUÁNTOS BOLETOS ALEATORIOS DESEA GENERAR? (1-20):\n", 1, 20)
    for _ in range(numero):
        numeros = random.sample(range(1, 49), 6)
        numeros_str = '-'.join(str(x) for x in numeros)
        lista_Numeros.append(numeros_str)
    print("\nBOLETOS GENERADOS:")
    
    for index, boleto in enumerate(lista_Numeros, start=1):
        print(f"{index}. {boleto}")
    seleccion = input("\nINGRESE LOS NUMERO QUE QUIERE COMPRAR SEPARADOS POR COMAS POR (EJEMPLO: 1,3,5):\n")
    seleccionados = []
    try:
        indices = [int(x.strip())-1 for x in seleccion.split(",") if x.strip().isdigit()]
        for idx in indices:
            if 0 <= idx < len(lista_Numeros):
                seleccionados.append(lista_Numeros[idx])
    except:
        print("SECCION INVALIDA")
        return
    if not seleccionados:
        print("NO SE SELECIONO NINGUN BOLETO")
        return
    for usuario in usuarios:
        if usuario["Usuario"] == usuario_nombre:
            if "boletos" not in usuario:
                usuario["boletos"] = []
            usuario["boletos"].extend(seleccionados)
            break
    escribirJson(datos, usuarios)
    Normalizar_Boletos(datos)
    print(f"\n¡BOLETOS COMPRADOS EXITOSAMENTE {usuario_nombre}!")

def Administrador_Menu():
    logos()
    print("------------------------------------------------😄-------------------------------------------------")
    print(f"----------------------------BIENVENIDO A NUESTRA LOTERIA {admin} 🌟 ------------------------------")
    espacio()
    print("----------------------------1. VER USUARIOS 🎟️                      -------------------------------")
    print("----------------------------2. INGRESER NUMERO GANADOR 🎟️           -------------------------------")
    print("----------------------------3. VER HISTORIAL DE NUMEROS GANADORES 🎉   ----------------------------")
    print("----------------------------4. VER HISTORIAL DE LOS GANADORES   📜     ----------------------------")
    print("----------------------------0. SALIR  ❌                               ----------------------------")   

def Administrador_Ver_Usuarios(datos: str,admin:str):
    Ver_Usuario = leerJson(datos)
    for i in Ver_Usuario:
        print(f"CEDULA: {i["Cedula"]} , USUARIO: {i["Usuario"]} , TELEFONO: {i["Telefono"]} , CORREO: {i["Correo"]}")

def Boletas_Ganadoras_Ad(nombre_Admin:str, datos:str):
    global Boleta_Ganadora
    ganador = leerJson(datos)
    while True:
        entrada = input("INGRESE 6 NÚMEROS ENTRE 1 Y 49, SEPARADOS POR COMAS (EJ: 5,12,23,34,41,48):\n")
        partes = entrada.split(",")
        if len(partes) != 6:
            print("DEBE INGRESAR EXACTAMENTE 6 NÚMEROS.")
            continue
        numeros = []
        es_valido = True
        for p in partes:
            p = p.strip()  
            if not p.isdigit():
                es_valido = False
                break
            numero = int(p)
            if numero < 1 or numero > 49:
                es_valido = False
                break
            numeros.append(numero)
        if es_valido:
            boleto = "-".join(str(n) for n in numeros)
            print("\nBOLETO GANADOR INGRESADO:")
            for i in ganador:
                if i["Usuario"] == nombre_Admin :
                    i["ganadores"].append(boleto)
                    Boleta_Ganadora = boleta 
                    escribirJson(datos,ganador)
            print(boleto)
            return boleto
        else:
            print("ENTRADA INVÁLIDA. ASEGÚRESE DE QUE TODOS LOS NÚMEROS ESTÉN ENTRE 1 Y 49.")
            
    for Indice, Ganador in enumerate(Numero_Ganador, start=1):
        print(f"{Indice}. {Ganador}")

def Numero_Ganadores(datos:str, admin: str):
    numero = leerJson(datos)
    for i in numero:
        if i["Usuario"] == admin:
            for i, index in enumerate(i["ganadores"], start = 1):
                print(f"{i}: {index}")

def Ganadores(datos: str, variable: str):
    Numero = leerJson(datos)
    encontrado = False
    for i in Numero:
        if "boletos" in i and variable in i["boletos"]:
            print(f"¡El usuario ganador es: {i['Usuario']}!")
            encontrado = True
    if not encontrado:
        print("No hay ganadores para ese boleto.")        

def Normalizar_Boletos(datos: str):
    usuarios = leerJson(datos)
    for usuario in usuarios:
        if "boletos" in usuario:
            nuevos_boletos = []
            for boleto in usuario["boletos"]:
                if isinstance(boleto, list):
                    # Convierte la lista de números a string con guiones
                    boleto_str = '-'.join(str(x) for x in boleto)
                    nuevos_boletos.append(boleto_str)
                else:
                    nuevos_boletos.append(boleto)
            usuario["boletos"] = nuevos_boletos
            escribirJson(datos, usuarios)
  
    
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
    global Nombre_Usuario
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
                        Nombre_Usuario = Usuario  # Guardar el usuario autenticado en la variable global
                        print(f"BIENVENIDOS A NUESTRA LOTERIA {Nombre_Usuario}")
                        return Nombre_Usuario
                    else:
                        print("CONTRASEÑA INCORRECTA")
            else:
                print("USUARIO NO EXISTE")                  
        break
 
def Agregar_Boletos_Manualmente(usuario_nombre: str, datos: str):
    usuarios = leerJson(datos)
    lista_Numeros = []
    cantidad = Validacion_Ingreso("¿CUÁNTOS BOLETOS DESEA COMPRAR? (1-5):\n", 1, 5)
    for i in range(cantidad):
        while True:
            entrada = input(f"INGRESE 6 NUMERO DEL 1 AL 49 POR {i+1} (EJEMPLO: 5,12,23,34,41,48):\n")
            numeros = [n.strip() for n in entrada.split(",")]
            if len(numeros) == 6 and all(n.isdigit() and 1 <= int(n) <= 49 for n in numeros):
                numeros_str = '-'.join(numeros)
                lista_Numeros.append(numeros_str)
                break
            else:
                print("ENTRADA INVALIDA INGRESE 6 NUMEROS DE DOS DIGITOS DEL 1 AL 49")
    print("\nBOLETOS INGRESADOS:")
    lista = convertido(Boleta_Ganadora)
    lista2 = convertido_lista(lista_Numeros)
    comparacion(lista2,lista)
        
    # Buscar usuario y agregar boletos
    for usuario in usuarios:
        if usuario["Usuario"] == usuario_nombre:
            if "boletos" not in usuario:
                usuario["boletos"] = []
            usuario["boletos"].extend(lista_Numeros)
            break
    escribirJson(datos, usuarios)
    Normalizar_Boletos(datos)
    print(f"\n¡Boletos comprados exitosamente para {usuario_nombre}!")

def Boletos_Comprados(nombre_Usuario: str, datos: str,):
    Boletos_Comprado = leerJson(datos)
    for indice in Boletos_Comprado:
        if indice["Usuario"] == nombre_Usuario:
            print(f"SUS BOLETOS COMPRADOS SON {nombre_Usuario}:")
            for i, index in enumerate(indice["boletos"], start = 1):
                print(f"{i}: {index}")
        else:
            print("USUARIO NO TIENE BOLETOS") 
             
    
        
def Numeros_Ganadores_Usuario(datos: str,  nombre_usario: str):
    historial_ganadores = leerJson(datos)
    for i in historial_ganadores:
        if i["Usuario"] == nombre_usario:
            for i, index in enumerate(i["ganadores"], start = 1):
                print(f"{i}: {index}")
                  

def Personal_numerosjugadores(datos:str, nombre_usuario:str):
    historial_personal = leerJson(datos)
    for i in historial_personal:
        if i["Usuario"] == nombre_usuario:
            for i, index in enumerate(i["historial"], start = 1):
                print(F"EL HISTORIAL DE LOS NUMEROS JUGADOS DE: {Nombre_Usuario}")
                print(f"{i}: {index}")

def premios_personales(datos:str, premios:str):
    Premios_personales = leerJson(datos)
    numero = []
    for x in Premios_personales:
        if x["Usuario"] == premios:
            for i, index in enumerate(x["boletos"], start = 1):
                numero.append(index)
    boletos_numeros = []
    for boleto in numero:
        numeros = [int(x) for x in boleto.split("-")]
        boletos_numeros.append(numeros)
    
    
        
def convertido(nombre: str):
    numero = [int(x) for x in nombre.split("-")]
    print(numero)
    return numero

def convertido_lista(nombre:list):
    numeros = [[int(x) for x in s.split("-")] for s in nombre]
    return numeros

          
        
def comparacion(dato:list, datos2: list):
    for i, boleto in enumerate(dato, start=1):
        aciertos = len(set(boleto) & set(datos2))
        print(f"Boleto {i}: {boleto} - Aciertos: {aciertos}")
              
def Proceso_Inicial():
    Menu_Usuario()
    Opcion_Usuario = Validacion_Menu_Usuario("INGRESE  SU OPCION\n",0,5)
    if  Opcion_Usuario == 1:
        Menu_Sub_Menu_Boletas()
        Opcion_Boleto = Validacion_Ingreso("INGRESE  SU OPCION\n",0,2)
        if Opcion_Boleto == 1:
            Agregar_Boletos_Usuario(Nombre_Usuario,"Loteria.json")             
        if Opcion_Boleto == 2:
            Agregar_Boletos_Manualmente(Nombre_Usuario,"Loteria.json")
        if Opcion_Boleto == 0:
            pass
    if Opcion_Usuario == 2:
        Boletos_Comprados(Nombre_Usuario,"Loteria.json")
        
            
while True:
    Menu_De_Ingreso()
    Opcion_Menu = Validacion_Menu_Ingreso("INGRESE  SU OPCION\n",0,2)

    if Opcion_Menu == 1:
        Guardar_Usuarios(Loteria,Usuarios)
        escribirJson("Loteria.json",Usuarios)
    elif  Opcion_Menu == 2:
        Ingreso_Usuario("Loteria.json")
        Proceso_Inicial()
    elif  Opcion_Menu == 0:
        Agregar_Boletos_Manualmente(Nombre_Usuario,"Loteria.json" )
        
        

