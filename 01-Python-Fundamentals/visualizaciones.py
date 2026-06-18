import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from pathlib import Path

DATA_FILE = str(Path(__file__).parent / 'TAREA.xlsx')
df_estadisticas = pd.read_excel(DATA_FILE)

# Etiquetas utiles para los graficos
etiquetas_rangos = {500: 'Facil: 1 a 500',1000: 'Medio: 1 a 1.000',5000: 'Dificil: 1 a 5.000'}
etiquetas_dificultad = {20: 'Facil: 20 intentos',12: 'Medio: 12 intentos',5: 'Dificil: 5 intentos'}

# Funcion para reemplazar los valores por las etiquetas
def mapeo_etiquetas(df):
    df['Rango'] = df['Rango'].map(etiquetas_rangos)
    df['Dificultad'] = df['Dificultad'].map(etiquetas_dificultad)
    return df

# Funcion de estadisticas generales
def fig1(df_estadisticas):
    df_mapped = mapeo_etiquetas(df_estadisticas.copy())
    plt.figure(figsize=(12, 4))
    
    ### Gráfico 1: Torta cantidad de juegos por dificultad
    plt.subplot(1, 3, 1)
    dificultad_counts = df_mapped['Dificultad'].value_counts()
    dificultad_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.ylabel('')
    plt.title('Cantidad de juegos por dificultad')
        
    ### Gráfico 2: Torta cantidad de juegos por rango
    plt.subplot(1, 3, 2)
    rango_counts = df_mapped['Rango'].value_counts()
    rango_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.ylabel('')
    plt.title('Cantidad de juegos por rango')

    ### Gráfico 3: Barras de modalidades de juego
    plt.subplot(1, 3, 3)
    modalidades_counts = df_mapped['Modalidad'].value_counts()
    modalidades_counts.plot(kind='bar')
    plt.title('Modalidad')

    ### Ajusto el espaciado entre subplots y muestro la visualizacion
    plt.tight_layout()
    plt.show()

# Funcion de historial de partidas
def fig2(df_estadisticas):
    df_mapped = mapeo_etiquetas(df_estadisticas.copy())
    fig2 = go.Figure(data=[go.Table(
        header=dict(values=list(df_mapped.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[df_mapped[col] for col in df_mapped.columns],
                fill_color='lavender',
                align='left'))])
    fig2.show()

#Funcion de ranking de ganadores
def fig3(df_estadisticas):
    df_mapped = mapeo_etiquetas(df_estadisticas.copy())
    ganadores = df_mapped[df_mapped['Resultado'] == 'Ganador']
    ranking_ganadores = ganadores['Nombre'].value_counts().reset_index()# Cuento la cantidad de partidas ganadas por cada jugador
    ranking_ganadores.columns = ['Nombre', 'Partidas Ganadas']
    ranking_ganadores = ranking_ganadores.sort_values(by='Partidas Ganadas', ascending=False) # Ordeno el ranking por cantidad de partidas ganadas
    fig3 = go.Figure([go.Bar(x=ranking_ganadores['Nombre'], y=ranking_ganadores['Partidas Ganadas'])])
    fig3.update_layout(title='Ranking de Ganadores', xaxis_title='Jugador', yaxis_title='Partidas Ganadas')
    fig3.show()

# Funcion auxiliar para calcular las estadisticas necesarias para las figuras 4 y 5
def calcular_estadisticas(df):
    partidas_jugadas = df.groupby('Nombre').size()    
    tasa_victoria = round(df.groupby('Nombre')['Resultado']
                       .apply(lambda x: (x == 'Ganador').sum() / len(x)).mul(100), 2)
    intentos_promedio = round(df.groupby('Nombre')['Intentos_realizados'].mean(),2) 
    dificultad_preferida = df.groupby('Nombre')['Dificultad'].agg(lambda x: x.value_counts().index[0])
    rango_preferido = df.groupby('Nombre')['Rango'].agg(lambda x: x.value_counts().index[0])
    modalidad_preferida = df.groupby('Nombre')['Modalidad'].agg(lambda x: x.value_counts().index[0])

    resumen = pd.DataFrame({
        'Partidas Jugadas': partidas_jugadas,
        'Tasa de Victoria (%)': tasa_victoria,
        'Intentos Promedio': intentos_promedio,
        'Dificultad Preferida': dificultad_preferida,
        'Rango Preferido': rango_preferido,
        'Modalidad Preferida': modalidad_preferida
    }).reset_index()

    return resumen

#Funcion de tabla estadisticas avanzadas por jugador
def fig4(df_estadisticas): 
    df_mapped = mapeo_etiquetas(df_estadisticas.copy())
    resumen = calcular_estadisticas(df_mapped)
    fig4 = go.Figure(data=[go.Table(
         header=dict(values=list(resumen.columns),
                     fill_color='paleturquoise',
                     align='left'),
         cells=dict(values=[resumen[col] for col in resumen.columns],
                    fill_color='lavender',
                    align='left'))])
    fig4.update_layout(title='Estadísticas por Jugador')
    fig4.show()

#Funcion de tabla estadisticas avanzadas por jugador en especifico
def estadisticas_por_jugador(df_estadisticas, jugador):
    df_mapped = mapeo_etiquetas(df_estadisticas.copy())
    estadisticas_jugador = calcular_estadisticas(df_mapped[df_mapped['Nombre'] == jugador])
    fig5 = go.Figure(data=[go.Table(
         header=dict(values=list(estadisticas_jugador.columns),
                     fill_color='paleturquoise',
                     align='left'),
         cells=dict(values=[estadisticas_jugador[col] for col in estadisticas_jugador.columns],
                    fill_color='lavender',
                    align='left'))])
    fig5.update_layout(title=f'Estadísticas de {jugador}')
    fig5.show()