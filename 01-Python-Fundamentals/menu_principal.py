### Welcome to the main menu of GUESS THE NUMBER.
# Make sure the modules "funciones_juego", "visualizaciones" and "utilidades" are
# in the same folder as this file, together with TAREA.xlsx. Enjoy the game!

import funciones_juego as fg
import visualizaciones as vz
import utilidades as ut
from pathlib import Path

# Resolve the Excel path relative to this script's folder — works anywhere.
DATA_FILE = str(Path(__file__).parent / 'TAREA.xlsx')

excel_document = ut.cargar_datos(DATA_FILE)
df_estadisticas = ut.cargar_estadisticas(DATA_FILE)

#Menu principal
while True:
    ut.menu_principal()
    eleccion = ut.validacion(1,4)
    opcion = str(eleccion)
    
    if opcion == '1':
        ut.menu_dificultad_intentos()
        dificultad = ut.validacion(1,3)
        ut.menu_dificultad_rango()
        rango = ut.validacion(1,3)
        if dificultad == 1 and rango == 1: 
            fg.modo_solitario(excel_document, 20, 500)
        elif dificultad == 2 and rango == 1:
            fg.modo_solitario(excel_document, 12, 500)
        elif dificultad == 3 and rango == 1:
            fg.modo_solitario(excel_document, 5, 500)
        elif dificultad == 1 and rango == 2: 
            fg.modo_solitario(excel_document, 20, 1000)
        elif dificultad == 2 and rango == 2:
            fg.modo_solitario(excel_document, 12, 1000)
        elif dificultad == 3 and rango == 2:
            fg.modo_solitario(excel_document, 5, 1000)
        elif dificultad == 1 and rango == 3: 
            fg.modo_solitario(excel_document, 20, 5000)
        elif dificultad == 2 and rango == 3:
            fg.modo_solitario(excel_document, 12, 5000)
        elif dificultad == 3 and rango == 3:
            fg.modo_solitario(excel_document, 5, 5000)
            
    elif opcion == '2':
        ut.menu_dificultad_intentos()
        dificultad = ut.validacion(1,3)
        ut.menu_dificultad_rango()
        rango = ut.validacion(1,3)
        if dificultad == 1 and rango == 1: 
            fg.dos_jugadores(excel_document, 20, 500)
        elif dificultad == 2 and rango == 1:
            fg.dos_jugadores(excel_document, 12, 500)
        elif dificultad == 3 and rango == 1:
            fg.dos_jugadores(excel_document, 5, 500)
        elif dificultad == 1 and rango == 2: 
            fg.dos_jugadores(excel_document, 20, 1000)
        elif dificultad == 2 and rango == 2:
            fg.dos_jugadores(excel_document, 12, 1000)
        elif dificultad == 3 and rango == 2:
            fg.dos_jugadores(excel_document, 5, 1000)
        elif dificultad == 1 and rango == 3: 
            fg.dos_jugadores(excel_document, 20, 5000)
        elif dificultad == 2 and rango == 3:
            fg.dos_jugadores(excel_document, 12, 5000)
        elif dificultad == 3 and rango == 3:
            fg.dos_jugadores(excel_document, 5, 5000)
            
    elif opcion == '3':
        df_estadisticas = ut.cargar_estadisticas(DATA_FILE)
        ut.menu_estadistica()
        eleccion = ut.validacion(1,5)
        if eleccion == 1:
            vz.fig1(df_estadisticas)
        elif eleccion == 2:
            vz.fig4(df_estadisticas)
        elif eleccion == 3:
            nombre_jugador = input('Ingrese el nombre del jugador para ver sus estadísticas: ').capitalize()
            vz.estadisticas_por_jugador(df_estadisticas, nombre_jugador)
        elif eleccion == 4:
            vz.fig3(df_estadisticas)
        else:
            vz.fig2(df_estadisticas)

    elif opcion == '4':
        print('Muchas gracias por jugar a ADIVINA EL NUMERO, Nos vemos pronto!')
        break
    
    # Save the data
excel_document.save(DATA_FILE)