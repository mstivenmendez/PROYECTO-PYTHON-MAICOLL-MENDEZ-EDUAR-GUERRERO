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

    
