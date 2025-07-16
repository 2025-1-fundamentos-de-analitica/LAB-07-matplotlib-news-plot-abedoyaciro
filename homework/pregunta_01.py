"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    
    # Leer los datos
    df = pd.read_csv('files/input/news.csv', index_col=0)
    
    # Crear la figura
    plt.figure()
    
    # Definir colores para cada línea
    colors = {
        "Television": "dimgray",
        "Newspaper": "grey", 
        "Internet": "tab:red",
        "Radio": "lightgrey",
    }
    
    # Definir orden z para las líneas
    zorder = {
        'Television': 1,
        'Newspaper': 1,
        'Internet': 2,
        'Radio': 1,
    }
    
    # Definir ancho de líneas
    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Internet': 4,
        'Radio': 2,
    }
    
    # Configurar el título y ejes
    plt.title("How people get their news", fontsize=16)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    
    # Dibujar las líneas y puntos para cada columna
    for col in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x=first_year,
            y=df[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )
        
        # Dibujar la línea
        plt.plot(
            df.index,
            df[col],
            color=colors[col],
            linewidth=linewidths[col],
            zorder=zorder[col],
        )
        
        # Punto del último año
        last_year = df.index[-1]
        plt.scatter(
            x=last_year,
            y=df[col][last_year],
            color=colors[col],
        )
        
        # Etiquetas en los extremos
        plt.text(
            first_year - 0.2,
            df[col][first_year],
            f"{col} {df[col][first_year]}%",
            ha='right',
            va='center',
            color=colors[col],
            fontsize=11
        )
        
        plt.text(
            last_year + 0.2,
            df[col][last_year],
            f"{df[col][last_year]}%",
            ha='left',
            va='center',
            color=colors[col],
            fontsize=11,
            weight='bold'
        )
    
    # Añadir subtítulo
    plt.text(
        0.5, 0.93,
        "An increasing proportion cite the internet as their primary news source",
        transform=plt.gca().transAxes,
        ha='center',
        # fontsize=11,
        # color='dimgray'
    )
    
    plt.xticks(
        ticks=df.index,
        labels=df.index,
        ha='center'
    )
        
    plt.tight_layout()
    
    # Crear directorio de salida si no existe
    os.makedirs('files/plots', exist_ok=True)
    
    # Guardar la figura
    plt.savefig('files/plots/news.png', dpi=300, bbox_inches='tight')
    plt.show()
