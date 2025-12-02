# Forecasting Ventas

Este proyecto contiene un modelo de Machine Learning para el pronóstico de ventas implementado con una aplicación Streamlit.

## Estructura del Proyecto

```
├── data/
│   ├── raw/          # Datos sin procesar
│   └── processed/    # Datos procesados
├── notebooks/        # Jupyter notebooks para análisis y desarrollo
├── models/          # Modelos entrenados
├── app/            # Aplicación Streamlit
├── docs/           # Documentación
├── requirements.txt # Dependencias del proyecto
└── .gitignore     # Archivos y carpetas ignoradas por git
```

## Configuración del Entorno

1. Crear un entorno virtual:
```bash
python -m venv venv
```

2. Activar el entorno virtual:
```bash
# Windows
venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Para desarrollo y análisis, usar los notebooks en la carpeta `notebooks/`
2. Los modelos entrenados se guardarán en `models/`
3. La aplicación Streamlit se encuentra en `app/`

Para ejecutar la aplicación Streamlit:
```bash
streamlit run app/main.py
```