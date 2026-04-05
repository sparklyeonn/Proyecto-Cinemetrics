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


# --- JIME (Limpieza y Auditoria) ---

def sanear_datos(df):
    """
    FASE 3: Limpieza y Tratamiento de Nulos.
    Mantiene la integridad del dataset procesado por Gene.
    """
    # Copia para no afectar el df original por accidente
    df_clean = df.copy()

    # 1. Tratamiento de Nulos en 'runtime' (Duración)
    # Justificación: Imputamos con la mediana para no sesgar por películas muy largas.
    mediana_runtime = df_clean['runtime'].median()
    df_clean['runtime'] = df_clean['runtime'].fillna(mediana_runtime)

    # 2. Limpieza de columnas de texto (Overview / Tagline)
    df_clean['overview'] = df_clean['overview'].fillna("Sin descripción")
    df_clean['tagline'] = df_clean['tagline'].fillna("Sin eslogan")

    # 3. Verificación de fechas (Si no hay fecha, se elimina porque es dato crítico)
    df_clean = df_clean.dropna(subset=['release_date'])
    
    return df_clean

def auditoria_integridad(df):
    """
    FASE 3: Validación de Calidad.
    Asegura que los datos sean lógicos post-limpieza.
    """
    print("\n--- 🔍 REPORTE DE AUDITORÍA (JIME) ---")
    
    # Check 1: ¿Hay presupuestos negativos?
    negativos = df[df['budget'] < 0].shape[0]
    print(f"1. Presupuestos negativos encontrados: {negativos}")

    # Check 2: ¿Hay duplicados por ID?
    duplicados = df.duplicated(subset=['id']).sum()
    print(f"2. Registros duplicados detectados: {duplicados}")

    # Check 3: ¿Quedaron nulos en columnas numéricas clave?
    nulos_finales = df[['budget', 'revenue', 'runtime']].isnull().sum().sum()
    print(f"3. Nulos en columnas críticas: {nulos_finales}")
    
    return negativos == 0 and duplicados == 0 and nulos_finales == 0


# --- ALE (Transformación Avanzada e Ingeniería de Atributos) ---

def limpiar_generos(json_str):
    """
    Transforma el string JSON anidado de géneros en una lista simple de nombres.
    Utiliza list comprehension para optimizar la velocidad de procesamiento.
    """
    try:
        # ast.literal_eval convierte el texto en una estructura de datos real de Python
        lista = ast.literal_eval(json_str)
        return [item['name'] for item in lista]
    except (ValueError, SyntaxError):
        return []

def asignar_temporada(mes):
    """
    Clasifica un mes numérico (1-12) en una temporada cinematográfica clave
    para analizar el impacto del 'Timing' de estreno en los ingresos.
    """
    if mes in [5, 6, 7, 8]:
        return 'Blockbuster Verano'
    elif mes in [10, 11, 12]:
        return 'Temporada Premios'
    elif mes in [1, 2]:
        return 'Enero Dump / Invierno'
    else:
        return 'Temporada Media'