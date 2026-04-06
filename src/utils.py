import pandas as pd
import ast
import os
import shutil
import kagglehub  

# Descargar y preparar los datos
def descargar_y_preparar_datos():
    # librería kagglehub
    path = kagglehub.dataset_download("tmdb/tmdb-movie-metadata")
    
    # destino
    destino = '../data/raw'
    os.makedirs(destino, exist_ok=True)
    
    # mover archivos
    for archivo in os.listdir(path):
        ruta_origen = os.path.join(path, archivo)
        ruta_destino = os.path.join(destino, archivo)
        if os.path.isfile(ruta_origen):
            shutil.copy(ruta_origen, ruta_destino)
            print(f"Copiado {archivo} a {destino}")

# Estructuración y unión

def cargar_y_unir_datasets(ruta_movies, ruta_credits):
    df_movies = pd.read_csv(ruta_movies)
    df_credits = pd.read_csv(ruta_credits)
    
    # se estandariza el nombre de la columna para la unión
    if 'movie_id' in df_credits.columns:
        df_credits = df_credits.rename(columns={'movie_id': 'id'})
    
    # unión (merge)
    return pd.merge(df_movies, df_credits, on='id')

def extraer_director(texto_crew):
    try:
        lista = ast.literal_eval(texto_crew)
        for miembro in lista:
            if miembro['job'] == 'Director':
                return miembro['name']
    except:
        return "Desconocido"
    return "Desconocido"


# Limpieza y auditoría

def sanear_datos(df):
    # Copia para no afectar el df original por accidente
    df_clean = df.copy()

    # 1. Tratamiento de nulos en 'runtime' 
    # Justificación: imputamos con la mediana para no sesgar por películas muy largas.
    mediana_runtime = df_clean['runtime'].median()
    df_clean['runtime'] = df_clean['runtime'].fillna(mediana_runtime)

    # 2. Limpieza de columnas de texto (Overview / Tagline)
    df_clean['overview'] = df_clean['overview'].fillna("Sin descripción")
    df_clean['tagline'] = df_clean['tagline'].fillna("Sin eslogan")

    # 3. Verificación de fechas (si no hay fecha, se elimina porque es dato crítico)
    df_clean = df_clean.dropna(subset=['release_date'])
    
    return df_clean

def auditoria_integridad(df):
    print("\n REPORTE DE AUDITORÍA")
    
    # ¿hay presupuestos negativos?
    negativos = df[df['budget'] < 0].shape[0]
    print(f"1. Presupuestos negativos encontrados: {negativos}")

    # ¿hay duplicados por id?
    duplicados = df.duplicated(subset=['id']).sum()
    print(f"2. Registros duplicados detectados: {duplicados}")

    # ¿quedaron nulos en columnas numéricas clave?
    nulos_finales = df[['budget', 'revenue', 'runtime']].isnull().sum().sum()
    print(f"3. Nulos en columnas críticas: {nulos_finales}")
    
    return negativos == 0 and duplicados == 0 and nulos_finales == 0


# Transformación avanzada 

def limpiar_generos(json_str):
    try:
        # ast.literal_eval convierte el texto en una estructura de datos real de Python
        lista = ast.literal_eval(json_str)
        return [item['name'] for item in lista]
    except (ValueError, SyntaxError):
        return []

def asignar_temporada(mes):
    if mes in [5, 6, 7, 8]:
        return 'Blockbuster Verano'
    elif mes in [10, 11, 12]:
        return 'Temporada Premios'
    elif mes in [1, 2]:
        return 'Enero Dump / Invierno'
    else:
        return 'Temporada Media'