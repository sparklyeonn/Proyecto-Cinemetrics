import pandas as pd
import ast
import os
import shutil
import kagglehub  

# --- CONI (Descarga y Preparación) ---
def descargar_y_preparar_datos():
    """
    Función de Coni: Descarga el dataset desde Kaggle y lo mueve a la carpeta data/raw.
    """
    # Descargar usando la librería kagglehub
    path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")
    
    # Definir destino
    destino = '../data/raw'
    os.makedirs(destino, exist_ok=True)
    
    # Mover archivos
    for archivo in os.listdir(path):
        ruta_origen = os.path.join(path, archivo)
        ruta_destino = os.path.join(destino, archivo)
        if os.path.isfile(ruta_origen):
            shutil.copy(ruta_origen, ruta_destino)
            print(f"✅ Copiado {archivo} a {destino}")

# --- GENE (Estructuración y Unión) ---

def cargar_y_unir_datasets(ruta_movies, ruta_credits):
    """
    Tu función: Carga los dos CSV y los une en un solo DataFrame usando el ID.
    """
    df_movies = pd.read_csv(ruta_movies)
    df_credits = pd.read_csv(ruta_credits)
    
    # Estandarizamos el nombre de la columna para la unión
    if 'movie_id' in df_credits.columns:
        df_credits = df_credits.rename(columns={'movie_id': 'id'})
    
    # Realizamos la unión (Merge)
    return pd.merge(df_movies, df_credits, on='id')

def extraer_director(texto_crew):
    """
    Tu función: Extrae el nombre del Director desde la columna 'crew'.
    """
    try:
        lista = ast.literal_eval(texto_crew)
        for miembro in lista:
            if miembro['job'] == 'Director':
                return miembro['name']
    except:
        return "Desconocido"
    return "Desconocido"