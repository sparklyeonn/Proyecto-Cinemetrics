El presente reporte detalla las primeras impresiones sobre la calidad y estructura del dataset de TMDB. Se realizó una inspección de 4,803 registros cinematográficos para evaluar su integridad y distribuciones estadísticas básicas antes de proceder a fases de limpieza y modelado.

Análisis de Calidad de Datos

A. Columnas con Valores Nulos (NaN)
- Homepage (64.3%): 3,091 registros faltantes. Esta columna no posee valor estadístico, por ende si se descarta o elimina no tiene efecto en los procesos.

- Tagline (17.5%): 844 registros faltantes. Información que no afecta cálculos numéricos.

- Datos críticos casi completos: release_date (1 nulo) y runtime (2 nulos). Estos casos aislados pueden corregirse mediante una limpieza simple.

B. Hallazgo Crítico: Nulos disfrazados de Ceros
Aunque la función de detección de nulos marca 0 para las columnas financieras, el análisis de valores específicos reveló una inconsistencia mayor:
    - Presupuesto ($0): 1,037 películas (21.6% del total) registran un presupuesto de cero.
    - Ingresos ($0): 1,441 películas (30.0% del total) registran ingresos de cero.

Impacto: Estos valores actúan como ruido. Cualquier cálculo de promedio o rentabilidad (ROI) que incluya estos ceros resultará en conclusiones sesgadas y erróneas.

C. Estadísticas Descriptivas
De las columnas con datos válidos (mayores a cero), se extrajeron las siguientes tendencias:
- Calificaciones (vote_average): La mayoría de las películas se concentran en un rango de 6.0 a 7.0. Existe una distribución normal con pocos casos extremos, lo que indica un sistema de votación equilibrado.
- Duración (runtime): El promedio se sitúa cerca de los 106 minutos, lo cual es el estándar de la industria.
- Predominancia de idioma: Más del 90% del dataset corresponde al idioma inglés (en), indicando que las conclusiones del proyecto estarán centradas principalmente en el mercado anglosajón.

D. Distribución de Géneros 
Se identificó que la columna genres venía en formato anidado (JSON). Tras un proceso de extracción y limpieza, se determinaron los géneros líderes:
    1. Drama: El género con mayor volumen de producción.
    2. Comedia: En segundo lugar de frecuencia.
    3. Thriller/Action: Géneros recurrentes en el top 5.

Estado de la fase: Finalizada y lista para preprocesamiento.