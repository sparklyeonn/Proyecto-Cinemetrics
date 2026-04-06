# Proyecto Cinemetrics: Análisis y Modelado de Datos de Cine

Este proyecto tiene como objetivo analizar, explorar y modelar datos cinematográficos provenientes de [The Movie Database (TMDB)](https://www.themoviedb.org/). A través de un enfoque basado en ciencia de datos, buscamos entender los factores que influyen en el éxito de una película, desde su presupuesto hasta sus géneros y popularidad.

## 🚀 Estructura del Proyecto
El proyecto está organizado para seguir un flujo de trabajo profesional de Ciencia de Datos:

```text
Proyecto-Cinemetrics/
├── data/              # Datasets brutos y procesados
├── docs/              # Reportes de hallazgos y documentación técnica
├── notebooks/         # Jupyter Notebooks con el flujo de análisis (EDA y Modelado)
├── outputs/           # Gráficos y resultados generados
└── environment.yml    # Configuración del entorno virtual (Conda)
```

## 🛠️ Configuración del Entorno

Para asegurar que todos los miembros del equipo trabajen con las mismas versiones de herramientas, utilizamos **Miniconda**.

### Instalación

1. Asegúrate de tener instalado [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Clona este repositorio y navega a la carpeta del proyecto.
3. Crea y activa el entorno con los siguientes comandos:
```bash
# Crear el entorno desde el archivo de configuración
conda env create -f environment.yml

# Activar el entorno
conda activate cinemetrics

# Si necesitas actualizar el entorno después de agregar nuevas librerías:
conda env update -f environment.yml --prune
```

---

## 📊 Fases del Proyecto

| Fase | Descripción |
|------|-------------|
| **Nivel Inicial (EDA)** | Análisis exploratorio de datos, estadística descriptiva y visualización de distribuciones (presupuestos, votos, géneros). |
| **Nivel 2 (Limpieza)** | Procesamiento de datos nulos y normalización de formatos JSON. |
| **Nivel 3 (Modelado)** | Aplicación de algoritmos de Machine Learning (Scikit-Learn) para predicciones y regresiones. |

---

## 👥 Contribuciones

Este proyecto fue desarrollado bajo una metodología de trabajo colaborativo mediante **GitHub**. Cada integrante es responsable de un nivel del flujo de datos, asegurando la trazabilidad y calidad del análisis.
- Constanza Gonzalez
- Alejandra Gonzalez
- Genesis Baeza
- Jimena Galicia
