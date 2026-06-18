import openpyxl
import pandas as pd

def cargar_datos(ruta):
    return openpyxl.load_workbook(ruta)

def cargar_estadisticas(ruta):
    return pd.read_excel(ruta)

#Funciones menu
def menu_principal(): 
    print('''Bienvenido al mejor juego de adivinanza!! ¿Que modalidad desea jugar?: 
          1. Partida modo solitario
          2. Partida dos jugadores
          3. Estadística
          4. Salir''')

def menu_dificultad_intentos(): 
    print('''Elija la cantidad de intentos:
            1. Facil(20 intentos)
            2. Medio(12 intentos)
            3. Dificil(5 intentos)''')

def menu_dificultad_rango(): 
    print('''Elija el rango de numeros:
            1. Facil(entre 1 y 500)
            2. Medio(entre 1 y 1.000)
            3. Dificil(entre 1 y 5.000)''')
    
def menu_estadistica():
    print('''Elija una opcion:
            1. Estadisticas generales
            2. Estadisticas avanzadas por jugador
            3. Estadisticas de un jugador en especifico
            4. Ranking de ganadores
            5. Historial de partidas''')

#Validacion opciones del menu
def validacion(minimo,maximo):
    eleccion = 0
    while (eleccion<minimo or eleccion>maximo):
        eleccion = int(input('Ingrese una opcion valida: '))
    return eleccion