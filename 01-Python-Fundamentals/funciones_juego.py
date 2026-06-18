import random
import getpass
import pandas as pd
from pathlib import Path

# Resolve the Excel path relative to this module's folder
DATA_FILE = str(Path(__file__).parent / 'TAREA.xlsx')

##Save data:
def guardar_datos(excel_document, nombre, resultado, intentos, dificultad, rango, opcion):
    hoja = excel_document['Estadisticas']
    fila_nueva = [nombre,'Ganador' if resultado else 'Perdedor',intentos,dificultad,rango,'Solitario' if opcion == '1' else 'Dos jugadores']
    hoja.append(fila_nueva)
    excel_document.save(DATA_FILE)
    ### Update the DataFrame
    global df_estadisticas
    df_estadisticas = pd.read_excel(DATA_FILE)

##Modalidades de juego
def modo_solitario(excel_document, dificultad, rango):
    nombre = input('Ingrese su nombre: ').capitalize()
    intentos_permitidos = dificultad
    numero_a_adivinar = random.randint(1, rango)
    intentos_realizados = 0
    print(f'Intenta adivinar el numero secreto!! Puede estar entre 1 y {rango}. Tienes {intentos_permitidos} intentos')
    while intentos_realizados < intentos_permitidos:
        intento = int(input('Introduce tu intento: '))
        if intento == numero_a_adivinar:    
            print(f'Felicidades {nombre}!! Adivinista el numero en tu {intentos_realizados}° intento')
            guardar_datos(excel_document, nombre, True, intentos_realizados, dificultad, rango, '1')
            return
        elif intento < numero_a_adivinar:
            print('El numero que buscas es mayor')
        else:
            print('El numero que buscas es menor')
        intentos_realizados += 1
        print(f'Te quedan {(intentos_permitidos-intentos_realizados)} intentos')
    print(f'Lo siento {nombre}, ya no tienes mas intentos. El número era: {numero_a_adivinar}')
    guardar_datos(excel_document, nombre, False, intentos_permitidos, dificultad, rango, '1')
    
def dos_jugadores(excel_document, dificultad, rango):
    intentos_permitidos = dificultad
    numero_a_adivinar = validacion_numero_a_adivinar(1, rango)
    nombre = input('Jugador 2, ingrese su nombre: ').capitalize()
    intentos_realizados = 0
    while intentos_realizados < intentos_permitidos:
        intento = int(input(f'{nombre}, intente adivinar el numero: '))
        intentos_realizados += 1
        if intento == numero_a_adivinar:
            print(f'Felicidades {nombre}!! Adivinista el numero en tu {intentos_realizados}° intento')
            guardar_datos(excel_document, nombre, True, intentos_realizados, dificultad, rango, '2')
            return
        elif intento < numero_a_adivinar:
            print('El número buscado es mayor.')
        else:
            print('El número buscado es menor.')
        print(f'Te quedan {(intentos_permitidos-intentos_realizados)} intentos')
    print(f'Lo siento {nombre}, ya no tienes mas intentos. El número era: {numero_a_adivinar}')
    guardar_datos(excel_document, nombre, False, intentos_permitidos, dificultad, rango, '2')

def validacion_numero_a_adivinar(minimo, maximo):
    eleccion = 0
    jugador1 = input('Jugador 1, ingrese su nombre: ').capitalize()
    while (eleccion<minimo or eleccion>maximo):
        eleccion = int(getpass.getpass(f'{jugador1}, Ingrese el numero a adivinar(entre {minimo} y {maximo}): '))
    return eleccion