#IMPORTACION DE LIBRERIAS
import os   # Librería para operaciones del sistema operativo (limpiar pantalla)
import random  # Librería para generar números aleatorios
import json # Librería para manejar archivos JSON
from collections import Counter # Importa Counter para contar elementos en listas

#FUNCIONES PARA MANEJO DE ARCHIVOS JSON
def leerJson(path: str):
    try:
        with open(path, mode='r') as file:
            datos = json.load(file)
            return datos
    except FileNotFoundError:
        return []
    
def escribirJson(path: str, data: list):
    with open(path, mode='w') as file:
        json.dump(data, file, indent=4)

# Variables globales
Loteria = {"usuarios": []}
Usuarios = []
numeros_boletas = []
Nombre_Usuario = "MSTIVEN"
Admin = "ADMINISTRADOR"
Boleta_Ganadora = "5-12-23-34-41-48"
historial_ganadores = []

#MENU PRINCIPAL
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

#FUNCIONES DE UTILIDAD
def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/Unix

# HACEMOS UN LIMPIAR CONSOLA CADA VEZ QUE INGRESE A UNA OPCION SEA DEL USUARIO O EL ADMINISTRADOR
def rango_clear_screen(variable: int, valorminimo: int, valormaximo: int):
    if valorminimo <= variable <= valormaximo:
        clear_screen()

#FUNCION  PARA IMPRIMIT UNA LINEA EN BLANCO
def espacio():
    print("\n" * 1)
# AGREGAMOS EL LOGO DE LA EMPRESA PARA QUE APARECA CADA VEZ QUE SE DE UNA OPCION
def logos():
    print(menu)
# INTERFAZ GRAFICA DEL LAPAGINA (FUNCIONES DE MENU)
def Menu_De_Ingreso():
    logos()
    print("---------------------------------------------------------------------------------------------------")
    print("-------------------BIENVENIDOS DONDE LAS OPOTUNIDADES DE GANAR SON TAN FACILES---------------------")
    print("----------------------------------1. REGISTRATE EN LA PAGINA --------------------------------------")
    print("----------------------------------2. INGRESAR A LA  PAGINA   --------------------------------------")
    print("----------------------------------0.         SALIR ❌           --------------------------------------")
    espacio()

#FUNCIONES DE VALIDACION
def Validacion_Ingreso(mensaje: str, valorminimo: int = 0, valormaximo: int = 6): #VALIDAR QUE SOLO INGRESE LETRAS
    while True:
        try:
            valor = int(input(mensaje))
            if valorminimo <= valor <= valormaximo:
                return valor
            else:
                print(f"POR FAVOR INGRESE VALORES ENTRE {valorminimo} y {valormaximo}.")
        except:
            print("ENTRADA NO VALIDA POR FAVOR INGRESE NUMEROS")

def Validar_Texto(mensaje: str): # VALIDA QUE SOLO SEA UNA CADENA DE TEXTO Y ME LA CONVIERTE EN MAYUSCULA 
    while True:
        valor = input(mensaje)
        suplente = valor.replace(" ", "")
        if suplente.isalpha() == True:
            valor = valor.upper()
            return valor
            break
        else:
            print("ENTRADA NO VALIDAD INGRESE SOLO LETRAS")
            continue

def Validacion_Menu_Ingreso(mensaje: str, valorminimo: int = 0, valormaximo: int = 6): #CADA VEZ QUE EL USUARIO INGRESE MAL EN LA PAGINA PRINCIPAL ME PARACESA NUEVAMENTE EL MENU 
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

def Validacion_Menu_Usuario(mensaje: str, valorminimo: int = 0, valormaximo: int = 7): # CADA VEZ QUE EL USUARIO INGRESE MAL EN LA INTERFAZ DEL USUSRIO ME PARACESA NUEVAMENTE EL MENU 
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
            
def Despedida(): # CUANDO SALGA EL USUARIO  DE LA PAGINA
    clear_screen()
    print("----------------- VUELVA MUY PRONTO DONDE LAS OPOTUNIDADES DE GANAR SON TAN FACILES ---------------")
    print("----------------------------------   GRACIAS POR TU VISITA   --------------------------------------")
    espacio()

def Validacion_Correo(mensaje: str): # VALIDA QUE EL CORREO SEA ESCRITO EN MINISCULA Y QUE NO TENGA ESPACIO Y LLEVE @
    while True:
        email = input(mensaje)
        if not "@" in email:
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
    
#FUNCIONES DE REGISTRO Y MANEJO DE USUARIOS
# Función para crear estructura de usuario
def Registro_Usuarios(Cedula: int, Nombre: str, Telefono: int, Correo: str, Usuario: str, Password: str): # CREAMOS  UN USUARIO Y LE AGREGAMOS  QUE VA TENER ESE USUARIO
    return {
        "Cedula": Cedula,
        "Nombre": Nombre,
        "Telefono": Telefono,
        "Correo": Correo,
        "Usuario": Usuario,
        "Password": Password,
        "boletos": [],
        "historial": [],
        "ganadores": [],
        "dinero_invertido": 0,
        "dinero_ganado": 0,
        "premios": {"bronce": 0, "plata": 0, "oro": 0, "gran_premio": 0}
    }


 # Función para registrar nuevos usuarios
def Guardar_Usuarios(datos: dict, guardar: list): # AQUI ES CUANDO EL USUARIO SE VA A REGISTRAR
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

def Validacion_Telefono(mensaje: str): # VALIDA QUE EL NUMERO TENGA 10 NUMERO Y QUE INICE EN 3 YA QUE S LA REFERENCIA EN COLOMBIA 
    while True: 
        try:
            telefono = int(input(mensaje))
            lista = [int(digito) for digito in str(telefono)]
            numero = len(lista)
            if lista[0] != 3:
                print("RECUERDA QUE SU NUMERO DEBE INICIAR EN 3")
            elif numero != 10:
                print("RECUERDA QUE SU NUMERO DEBE DEBE CONTENER 10 DIGITOS")
            elif numero == 10 and lista[0] == 3:
                print("TU NUMERO HA SIDO INGRESADO")
                return telefono 
                break
            else:
                print("RECUERDA QUE SU NUMERO NO DEBE TENE LETRAS ")
        except:
            print("INGRESE SOLO NUMEROS")

# INTERFAZ DE CADA OPCION O SI ES USUARIO O ADMINISTRADOR
# FUNCIONES DE MENUS ESPECIFICOS
def Menu_Usuario():
    logos()
    print("------------------------------------------------😄-------------------------------------------------")
    print("------------------BIENVENIDOS DONDE LAS OPOTUNIDADES DE GANAR SON TAN FACILES 🌟 ------------------")
    print(f"-----------------------BIENVENIDO A NUESTRA LOTERIA {Nombre_Usuario} 🌟 -------------------------")
    espacio()
    print("----------------------------1. COMPRAR BOLETOS 🎟️                      ----------------------------")
    print("----------------------------2. BOLETOS COMPRADOS 🎟️                    ----------------------------")
    print("----------------------------3. VER HOSTORIAL DE NUMEROS GANADORES 🎉   ----------------------------")
    print("----------------------------4. VER HISTORIAL DE BOLETAS JUGADOS 📜     ----------------------------")
    print("----------------------------5. VER HISTORIAL CON ACIERTOS POR BOLETO 🎯----------------------------")
    print("----------------------------6. VER DINERO INVERTIDO 💰                 ----------------------------")
    print("----------------------------7. VER DINERO GANADO 🤑                    ----------------------------")
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
    print("----------------------------1. PREMIO BRONCE 🥉 (3 ACIERTOS)     ---------------------------------")
    print("----------------------------2. PREMIO PLATA  🥈 (4 ACIERTOS)     ---------------------------------")
    print("----------------------------3. PREMIO ORO 🥇 (5 ACIERTOS)        ---------------------------------")
    print("----------------------------4. GRAN PREMIO 🏆 (6 ACIERTOS)       ---------------------------------")
    print("----------------------------5. ESTADISTICAS 📊                   ---------------------------------")
    print("----------------------------0. SALIR  ❌                         ---------------------------------")

#FUNCIONES DE COMPRA DE BOLETOS
def Agregar_Boletos_Usuario(usuario_nombre: str, datos: str): # AGREGA LOS BOLETOS ALEATORIAMENTE Y QUE EL ESCOJA CUALES QUIERE
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
    
    # Calcular costo y agregar boletos
    costo = len(seleccionados) * 2000  # $2000 por boleto
    
    for usuario in usuarios:
        if usuario["Usuario"] == usuario_nombre:
            if "boletos" not in usuario:
                usuario["boletos"] = []
            if "historial" not in usuario:
                usuario["historial"] = []
            if "dinero_invertido" not in usuario:
                usuario["dinero_invertido"] = 0
                
            usuario["boletos"].extend(seleccionados)
            usuario["historial"].extend(seleccionados)
            usuario["dinero_invertido"] += costo
            break
    
    escribirJson(datos, usuarios)
    
    # MOSTRAR ACIERTOS VS ULTIMO ACIERTO
    mostrar_aciertos_ultimo_sorteo(seleccionados, datos)
    
    # MOSTRAR NUEMRO MAS FRECUENTES
    mostrar_numero_mas_frecuente(datos)
    
    print(f"\n¡BOLETOS COMPRADOS EXITOSAMENTE {usuario_nombre}!")
    print(f"COSTO TOTAL: ${costo:,}")
    
    #FUNCIONES DEL ADMINISTRADOR
def Administrador_Menu():
    logos()
    print("------------------------------------------------😄-------------------------------------------------")
    print(f"----------------------------BIENVENIDO A NUESTRA LOTERIA {Admin} 🌟 ------------------------------")
    espacio()
    print("----------------------------1. VER USUARIOS 🎟️                      -------------------------------")
    print("----------------------------2. INGRESER NUMERO GANADOR 🎟️           -------------------------------")
    print("----------------------------3. VER HISTORIAL DE NUMEROS GANADORES 🎉   ----------------------------")
    print("----------------------------4. VER HISTORIAL DE LOS GANADORES   📜     ----------------------------")
    print("----------------------------0. SALIR  ❌                               ----------------------------")   

# Función para mostrar todos los usuarios registrados
def Administrador_Ver_Usuarios(datos: str, admin: str): # CAUNDO EL USUARIO QUIERA VER LOS USUARIOS
    Ver_Usuario = leerJson(datos)
    for i in Ver_Usuario:
        print(f"CEDULA: {i['Cedula']} , USUARIO: {i['Usuario']} , TELEFONO: {i['Telefono']} , CORREO: {i['Correo']}")
# Función para que el administrador ingrese número ganador
def Boletas_Ganadoras_Ad(nombre_Admin: str, datos: str): # EN ADMINISTRADOR AGREGA LA BOLETA GANADORA 
    global Boleta_Ganadora, historial_ganadores
    
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
            Boleta_Ganadora = boleto
            historial_ganadores.append(boleto)
            
            print(f"\nBOLETO GANADOR INGRESADO: {boleto}")
            
            # VEFIFICA GANADORES Y LOS ACTUALIZA
            verificar_ganadores_y_premios(datos, boleto)
            return boleto
        else:
            print("ENTRADA INVÁLIDA. ASEGÚRESE DE QUE TODOS LOS NÚMEROS ESTÉN ENTRE 1 Y 49.")
 # Función para verificar ganadores y otorgar premios
def verificar_ganadores_y_premios(datos: str, boleto_ganador: str): #VERIFICA GANADORES POR ACIERTOS
    usuarios = leerJson(datos)
    numeros_ganadores = [int(x) for x in boleto_ganador.split("-")]
    
    for usuario in usuarios:
        if "boletos" in usuario:
            for boleto in usuario["boletos"]:
                numeros_boleto = [int(x) for x in boleto.split("-")]
                aciertos = len(set(numeros_boleto) & set(numeros_ganadores))
                
                # ASIGNA LOS PREMIOS SEGUN ACIERTOS
                if aciertos == 6:
                    usuario["premios"]["gran_premio"] += 1
                    usuario["dinero_ganado"] += 100000000  # $100,000,000
                    print(f"¡GRAN PREMIO! Usuario {usuario['Usuario']} ganó $100,000,000")
                elif aciertos == 5:
                    usuario["premios"]["oro"] += 1
                    usuario["dinero_ganado"] += 5000000  # $5,000,000
                    print(f"¡PREMIO ORO! Usuario {usuario['Usuario']} ganó $5,000,000")
                elif aciertos == 4:
                    usuario["premios"]["plata"] += 1
                    usuario["dinero_ganado"] += 500000  # $500,000
                    print(f"¡PREMIO PLATA! Usuario {usuario['Usuario']} ganó $500,000")
                elif aciertos == 3:
                    usuario["premios"]["bronce"] += 1
                    usuario["dinero_ganado"] += 50000  # $50,000
                    print(f"¡PREMIO BRONCE! Usuario {usuario['Usuario']} ganó $50,000")
    
    escribirJson(datos, usuarios)

# Función para mostrar historial de números ganadores (admin)
def Numero_Ganadores(datos: str, admin: str): # MUESTRA LOS NUMEROS GANADORES .................
    global historial_ganadores
    print("HISTORIAL DE NÚMEROS GANADORES:")
    for i, ganador in enumerate(historial_ganadores, start=1):
        print(f"{i}: {ganador}")

 # Función para buscar ganadores de un boleto específico
def Ganadores(datos: str, variable: str):
    usuarios = leerJson(datos)
    encontrado = False
    for usuario in usuarios:
        if "boletos" in usuario and variable in usuario["boletos"]:
            print(f"¡El usuario ganador es: {usuario['Usuario']}!")
            encontrado = True
    if not encontrado:
        print("No hay ganadores para ese boleto.")        
 # Función para normalizar formato de boletos
def Normalizar_Boletos(datos: str):
    usuarios = leerJson(datos)
    for usuario in usuarios:
        if "boletos" in usuario:
            nuevos_boletos = []
            for boleto in usuario["boletos"]:
                if isinstance(boleto, list):
                    boleto_str = '-'.join(str(x) for x in boleto)
                    nuevos_boletos.append(boleto_str)
                else:
                    nuevos_boletos.append(boleto)
            usuario["boletos"] = nuevos_boletos
    escribirJson(datos, usuarios)

# Función para verificar que las contraseñas coincidan
def Verificacion_Contraseña(mensaje: str):
    while True:
        contraseña = input(mensaje)
        contraseña2 = input("CONFIRMAR TU CONTRASEÑA ")
        if contraseña == contraseña2:
            print("CONTRASEÑA GUARDADA, EXITOSAMENTE")
            return contraseña
        else:
            print("VERIFICA QUE LAS CONTRAEÑAS SEAN IGUALES")

 # Función para iniciar sesión de usuario
def Ingreso_Usuario(mensaje: str):
    global Nombre_Usuario
    while True:
        Usuario = Validar_Texto("INGRESE SU USUARIO PARA INGRESAR A SU CUENTA: \n")
        datos = leerJson(mensaje)
        espacio()
        
        usuario_encontrado = False
        for dato in datos:
            if dato["Usuario"] == Usuario:
                usuario_encontrado = True
                while True:
                    Contraseña = input("INGRESAR CONTRASEÑA \n")
                    if dato["Password"] == Contraseña:
                        logos()
                        Nombre_Usuario = Usuario
                        print(f"BIENVENIDOS A NUESTRA LOTERIA {Nombre_Usuario}")
                        return Nombre_Usuario
                    else:
                        print("CONTRASEÑA INCORRECTA")
                        break
                break
        
        if not usuario_encontrado:
            print("USUARIO NO EXISTE")
            break


# Función para comprar boletos ingresando números manualmente
def Agregar_Boletos_Manualmente(usuario_nombre: str, datos: str):
    usuarios = leerJson(datos)
    lista_Numeros = []
    cantidad = Validacion_Ingreso("¿CUÁNTOS BOLETOS DESEA COMPRAR? (1-5):\n", 1, 5)
    
    for i in range(cantidad):
        while True:
            entrada = input(f"INGRESE 6 NUMERO DEL 1 AL 49 PARA BOLETO {i+1} (EJEMPLO: 5,12,23,34,41,48):\n")
            numeros = [n.strip() for n in entrada.split(",")]
            
            if len(numeros) == 6 and all(n.isdigit() and 1 <= int(n) <= 49 for n in numeros):
                numeros_str = '-'.join(numeros)
                lista_Numeros.append(numeros_str)
                break
            else:
                print("ENTRADA INVALIDA INGRESE 6 NUMEROS DE DOS DIGITOS DEL 1 AL 49")
    
    print("\nBOLETOS INGRESADOS:")
    for i, boleto in enumerate(lista_Numeros, start=1):
        print(f"{i}: {boleto}")
    
    # Calcular costo
    costo = len(lista_Numeros) * 2000
    
    # Buscar usuario y agregar boletos
    for usuario in usuarios:
        if usuario["Usuario"] == usuario_nombre:
            if "boletos" not in usuario:
                usuario["boletos"] = []
            if "historial" not in usuario:
                usuario["historial"] = []
            if "dinero_invertido" not in usuario:
                usuario["dinero_invertido"] = 0
                
            usuario["boletos"].extend(lista_Numeros)
            usuario["historial"].extend(lista_Numeros)
            usuario["dinero_invertido"] += costo
            break
    
    escribirJson(datos, usuarios)
    
    # Mostrar aciertos vs último sorteo
    mostrar_aciertos_ultimo_sorteo(lista_Numeros, datos)
    
    # Mostrar número más frecuente
    mostrar_numero_mas_frecuente(datos)
    
    print(f"\n¡Boletos comprados exitosamente para {usuario_nombre}!")
    print(f"COSTO TOTAL: ${costo:,}")

 # Función para mostrar boletos comprados por usuario
def Boletos_Comprados(nombre_Usuario: str, datos: str):
    usuarios = leerJson(datos)
    boletos_encontrados = False
    
    for usuario in usuarios:
        if usuario["Usuario"] == nombre_Usuario:
            if "boletos" in usuario and len(usuario["boletos"]) > 0:
                print(f"SUS BOLETOS COMPRADOS SON {nombre_Usuario}:")
                for i, boleto in enumerate(usuario["boletos"], start=1):
                    print(f"{i}: {boleto}")
                boletos_encontrados = True
            break
    
    if not boletos_encontrados:
        print("NO TIENE BOLETOS COMPRADOS")

# Función para mostrar números ganadores al usuario
def Numeros_Ganadores_Usuario(datos: str, nombre_usuario: str):
    global historial_ganadores
    print(f"HISTORIAL DE NÚMEROS GANADORES PARA {nombre_usuario}:")
    for i, ganador in enumerate(historial_ganadores, start=1):
        print(f"{i}: {ganador}")

 # Función para mostrar historial personal de números jugados
def Personal_numerosjugadores(datos: str, nombre_usuario: str):
    usuarios = leerJson(datos)
    
    for usuario in usuarios:
        if usuario["Usuario"] == nombre_usuario:
            if "historial" in usuario and len(usuario["historial"]) > 0:
                print(f"EL HISTORIAL DE LOS NUMEROS JUGADOS DE: {nombre_usuario}")
                for i, boleto in enumerate(usuario["historial"], start=1):
                    print(f"{i}: {boleto}")
            else:
                print("NO HAY HISTORIAL DE BOLETOS JUGADOS")
            break

 # Función para mostrar premios ganados por usuario
def premios_personales(datos: str, nombre_usuario: str):
    usuarios = leerJson(datos)
    
    for usuario in usuarios:
        if usuario["Usuario"] == nombre_usuario:
            premios = usuario.get("premios", {"bronce": 0, "plata": 0, "oro": 0, "gran_premio": 0})
            print(f"PREMIOS PERSONALES DE {nombre_usuario}:")
            print(f"🥉 PREMIO BRONCE (3 aciertos): {premios['bronce']} veces")
            print(f"🥈 PREMIO PLATA (4 aciertos): {premios['plata']} veces")
            print(f"🥇 PREMIO ORO (5 aciertos): {premios['oro']} veces")
            print(f"🏆 GRAN PREMIO (6 aciertos): {premios['gran_premio']} veces")
            break

 # Función para mostrar dinero invertido por usuario
def ver_dinero_invertido(datos: str, nombre_usuario: str):
    usuarios = leerJson(datos)
    
    for usuario in usuarios:
        if usuario["Usuario"] == nombre_usuario:
            dinero = usuario.get("dinero_invertido", 0)
            print(f"DINERO INVERTIDO POR {nombre_usuario}: ${dinero:,}")
            break

 # Función para mostrar dinero ganado por usuario
def ver_dinero_ganado(datos: str, nombre_usuario: str):
    usuarios = leerJson(datos)
    
    for usuario in usuarios:
        if usuario["Usuario"] == nombre_usuario:
            dinero = usuario.get("dinero_ganado", 0)
            print(f"DINERO GANADO POR {nombre_usuario}: ${dinero:,}")
            break


 # Función para mostrar aciertos contra último sorteo
def mostrar_aciertos_ultimo_sorteo(boletos: list, datos: str):
    global Boleta_Ganadora
    
    if Boleta_Ganadora:
        numeros_ganadores = [int(x) for x in Boleta_Ganadora.split("-")]
        print(f"\nACIERTOS VS ÚLTIMO SORTEO ({Boleta_Ganadora}):")
        
        for i, boleto in enumerate(boletos, start=1):
            numeros_boleto = [int(x) for x in boleto.split("-")]
            aciertos = len(set(numeros_boleto) & set(numeros_ganadores))
            print(f"Boleto {i} ({boleto}): {aciertos} aciertos")


 # Función para mostrar número más frecuente en sorteos
def mostrar_numero_mas_frecuente(datos: str):
    global historial_ganadores
    
    if len(historial_ganadores) > 0:
        todos_numeros = []
        # Tomar los últimos 20 sorteos
        ultimos_sorteos = historial_ganadores[-20:]
        
        for sorteo in ultimos_sorteos:
            numeros = [int(x) for x in sorteo.split("-")]
            todos_numeros.extend(numeros)
        
        if todos_numeros:
            contador = Counter(todos_numeros)
            mas_frecuente = contador.most_common(1)[0]
            print(f"\nNÚMERO MÁS FRECUENTE EN ÚLTIMOS {len(ultimos_sorteos)} SORTEOS:")
            print(f"Número {mas_frecuente[0]} apareció {mas_frecuente[1]} veces")
    else:
        print("\nNO HAY HISTORIAL DE SORTEOS DISPONIBLE")

 # Función para convertir string de boleto a lista de enteros
def convertido(nombre: str):
    numero = [int(x) for x in nombre.split("-")]
    return numero

# Función para convertir lista de strings de boletos a listas de enteros
def convertido_lista(nombre: list):
    numeros = [[int(x) for x in s.split("-")] for s in nombre]
    return numeros

 # Función para comparar boletos con número ganador
def comparacion(dato: list, datos2: list):
    for i, boleto in enumerate(dato, start=1):
        aciertos = len(set(boleto) & set(datos2))
        print(f"Boleto {i}: {boleto} - Aciertos: {aciertos}")

 # Función para mostrar historial con aciertos detallados
def mostrar_historial_con_aciertos(datos: str, nombre_usuario: str):
    global Boleta_Ganadora
    usuarios = leerJson(datos)
    
    for usuario in usuarios:
        if usuario["Usuario"] == nombre_usuario:
            if "historial" in usuario and len(usuario["historial"]) > 0:
                print(f"HISTORIAL CON ACIERTOS DE {nombre_usuario}:")
                numeros_ganadores = [int(x) for x in Boleta_Ganadora.split("-")]
                
                for i, boleto in enumerate(usuario["historial"], start=1):
                    numeros_boleto = [int(x) for x in boleto.split("-")]
                    aciertos = len(set(numeros_boleto) & set(numeros_ganadores))
                    premio = ""
                    
                    if aciertos == 6:
                        premio = "🏆 GRAN PREMIO"
                    elif aciertos == 5:
                        premio = "🥇 PREMIO ORO"
                    elif aciertos == 4:
                        premio = "🥈 PREMIO PLATA"
                    elif aciertos == 3:
                        premio = "🥉 PREMIO BRONCE"
                    
                    print(f"{i}: {boleto} - {aciertos} aciertos {premio}")
            else:
                print("NO HAY HISTORIAL DE BOLETOS")
            break

 # Función principal del menú de usuario
def Proceso_Inicial():
    while True:
        Menu_Usuario()
        Opcion_Usuario = Validacion_Menu_Usuario("INGRESE SU OPCION\n", 0, 7)
        rango_clear_screen(Opcion_Usuario,0,7)
        
        if Opcion_Usuario == 1:  # COMPRAR BOLETOS
            Menu_Sub_Menu_Boletas()
            Opcion_Boleto = Validacion_Ingreso("INGRESE SU OPCION\n", 0, 2)
            rango_clear_screen(Opcion_Boleto,0,2)
            
            if Opcion_Boleto == 1:  # Compra aleatoria
                logos()
                Agregar_Boletos_Usuario(Nombre_Usuario, "Loteria.json")
            elif Opcion_Boleto == 2:  # Compra manual
                logos()
                Agregar_Boletos_Manualmente(Nombre_Usuario, "Loteria.json")
            elif Opcion_Boleto == 0:  # Salir
                continue
                
        elif Opcion_Usuario == 2:  # VER BOLETOS COMPRADOS
            logos()
            Boletos_Comprados(Nombre_Usuario, "Loteria.json")
            input("\nPresione ENTER para continuar...")
            
        elif Opcion_Usuario == 3:  # VER HISTORIAL DE NÚMEROS GANADORES
            logos()
            Numeros_Ganadores_Usuario("Loteria.json", Nombre_Usuario)
            input("\nPresione ENTER para continuar...")
            
        elif Opcion_Usuario == 4:  # VER HISTORIAL PERSONAL
            logos()
            Personal_numerosjugadores("Loteria.json", Nombre_Usuario)
            input("\nPresione ENTER para continuar...")
            
        elif Opcion_Usuario == 5:  # VER HISTORIAL CON ACIERTOS
            Menu_Sub_Menu_Aciertos()
            opcion_aciertos = Validacion_Ingreso("INGRESE SU OPCION\n", 0, 5)
            rango_clear_screen(opcion_aciertos,0,5)
            
            if opcion_aciertos == 1:  # Premio Bronce
                logos()
                mostrar_premios_especificos("Loteria.json", Nombre_Usuario, "bronce")
            elif opcion_aciertos == 2:  # Premio Plata
                logos()
                mostrar_premios_especificos("Loteria.json", Nombre_Usuario, "plata")
            elif opcion_aciertos == 3:  # Premio Oro
                logos()
                mostrar_premios_especificos("Loteria.json", Nombre_Usuario, "oro")
            elif opcion_aciertos == 4:  # Gran Premio
                logos()
                mostrar_premios_especificos("Loteria.json", Nombre_Usuario, "gran_premio")
            elif opcion_aciertos == 5:  # Estadísticas
                logos()
                premios_personales("Loteria.json", Nombre_Usuario)
                mostrar_historial_con_aciertos("Loteria.json", Nombre_Usuario)
            
            input("\nPresione ENTER para continuar...")
            
        elif Opcion_Usuario == 6:  # VER DINERO INVERTIDO
            logos()
            ver_dinero_invertido("Loteria.json", Nombre_Usuario)
            input("\nPresione ENTER para continuar...")
            
        elif Opcion_Usuario == 7:  # VER DINERO GANADO
            logos()
            ver_dinero_ganado("Loteria.json", Nombre_Usuario)
            input("\nPresione ENTER para continuar...")
            
        elif Opcion_Usuario == 0:  # SALIR
            break

# Función para mostrar premios específicos
def mostrar_premios_especificos(datos: str, nombre_usuario: str, tipo_premio: str):
    usuarios = leerJson(datos)
    
    for usuario in usuarios:
        if usuario["Usuario"] == nombre_usuario:
            premios = usuario.get("premios", {"bronce": 0, "plata": 0, "oro": 0, "gran_premio": 0})
            cantidad = premios.get(tipo_premio, 0)
            
            nombres_premios = {
                "bronce": "🥉 PREMIO BRONCE (3 aciertos)",
                "plata": "🥈 PREMIO PLATA (4 aciertos)", 
                "oro": "🥇 PREMIO ORO (5 aciertos)",
                "gran_premio": "🏆 GRAN PREMIO (6 aciertos)"
            }
            
            print(f"{nombres_premios[tipo_premio]}: {cantidad} veces ganado")
            
            if cantidad > 0:
                dinero_por_premio = {
                    "bronce": 50000,
                    "plata": 500000,
                    "oro": 5000000,
                    "gran_premio": 100000000
                }
                total_ganado = cantidad * dinero_por_premio[tipo_premio]
                print(f"Total ganado en este premio: ${total_ganado:,}")
            break

 # Función principal del menú de administrador
def Proceso_Administrador():
    while True:
        Administrador_Menu()
        opcion_admin = Validacion_Ingreso("INGRESE SU OPCION\n", 0, 4)
        rango_clear_screen(opcion_admin,0,4)
        
        if opcion_admin == 1:  # VER USUARIOS
            logos()
            Administrador_Ver_Usuarios("Loteria.json", Admin)
            input("\nPresione ENTER para continuar...")
            
        elif opcion_admin == 2:  # INGRESAR NÚMERO GANADOR
            logos()
            Boletas_Ganadoras_Ad(Admin, "Loteria.json")
            input("\nPresione ENTER para continuar...")
            
        elif opcion_admin == 3:  # VER HISTORIAL DE NÚMEROS GANADORES
            logos()
            Numero_Ganadores("Loteria.json", Admin)
            input("\nPresione ENTER para continuar...")
            
        elif opcion_admin == 4:  # VER HISTORIAL DE GANADORES
            logos()
            mostrar_todos_los_ganadores("Loteria.json")
            input("\nPresione ENTER para continuar...")
            
        elif opcion_admin == 0:  # SALIR
            break

 # Función para mostrar todos los ganadores del sistema
def mostrar_todos_los_ganadores(datos: str):
    usuarios = leerJson(datos)
    print("HISTORIAL DE TODOS LOS GANADORES:")
    logos()
    
    hay_ganadores = False
    for usuario in usuarios:
        premios = usuario.get("premios", {"bronce": 0, "plata": 0, "oro": 0, "gran_premio": 0})
        total_premios = sum(premios.values())
        
        if total_premios > 0:
            hay_ganadores = True
            print(f"\nUSUARIO: {usuario['Usuario']}")
            print(f"🥉 Premios Bronce: {premios['bronce']}")
            print(f"🥈 Premios Plata: {premios['plata']}")
            print(f"🥇 Premios Oro: {premios['oro']}")
            print(f"🏆 Gran Premios: {premios['gran_premio']}")
            print(f"💰 Total ganado: ${usuario.get('dinero_ganado', 0):,}")
    
    if not hay_ganadores:
        print("NO HAY GANADORES REGISTRADOS")

# PROGRAMA PRINCIPAL
def main(): # Función principal del programa
    global Nombre_Usuario
    
    while True:
        Menu_De_Ingreso()
        Opcion_Menu = Validacion_Menu_Ingreso("INGRESE SU OPCION\n", 0, 2)
        rango_clear_screen(Opcion_Menu,0,2)

        if Opcion_Menu == 1:  # REGISTRARSE
            logos()
            Guardar_Usuarios(Loteria, Usuarios)
            escribirJson("Loteria.json", Usuarios)
            print("USUARIO REGISTRADO EXITOSAMENTE")
            input("Presione ENTER para continuar...")
            
        elif Opcion_Menu == 2:  # INICIAR SESIÓN
            # Verificar si es administrador
            logos()
            usuario_ingresado = input("INGRESE SU USUARIO: ").upper()
            
            if usuario_ingresado == "ADMINISTRADOR":
                contraseña = input("INGRESE CONTRASEÑA DE ADMINISTRADOR: ")
                if contraseña == "admin123":  # Contraseña del administrador
                    print("BIENVENIDO ADMINISTRADOR")
                    Proceso_Administrador()
                else:
                    print("CONTRASEÑA INCORRECTA")
            else:
                # Proceso normal de usuario
                resultado = Ingreso_Usuario("Loteria.json")
                if resultado:
                    Proceso_Inicial()
                    
        elif Opcion_Menu == 0:  # SALIR
            Despedida()
            break

if __name__ == "__main__":
    main()
