🛒 Simulador de Ventas Diario — Noviembre 2025

Predicción diaria de demanda con Machine Learning + ajustes de precio y competencia

Este proyecto construye un simulador interactivo para prever ventas diarias de productos durante Noviembre de 2025, combinando:

Modelos de Machine Learning

Predicción recursiva día a día

Ajustes dinámicos de precio y escenarios competitivos

Una app en Streamlit para uso por equipos comerciales y directivos

🧱 1. Arquitectura del Proyecto
simulador-ventas-noviembre-2025/
│
├── Datos/                       
│   ├── entrenamiento/
│   └── inferencia/
│
├── Forecasting Ventas/
│   ├── app/
│   │   └── app.py
│   ├── data/
│   │   ├── raw/
│   │   ├── processed/
│   │   └── external/
│   ├── docs/
│   ├── models/
│   │   └── modelo_final.joblib
│   ├── notebooks/
│   ├── README.md
│   ├── requirements.txt
│   └── .gitignore
│
└── copilot-instructions/

🎯 2. Objetivo

El objetivo es crear una herramienta que permita responder en segundos:

¿Cuántas unidades voy a vender cada día?

¿Qué pasa si bajo el precio un 10%?

¿Qué ocurre si la competencia sube o baja su precio?

¿Cómo afecta el Black Friday a las ventas?

Esto es útil para:

📦 Demand Planners

💰 Pricing Managers

📊 Directores Comerciales

🧠 VPs / CTOs que requieren escenarios rápidos para tomar decisiones

⚙️ 3. Metodología (4 Fases Técnicas)
Fase 1 — Data & Calidad de Datos

Se realizan:

Importación de datos brutos

Limpieza y formateo

Revisión de valores NA

Validación de columnas clave

Alineación entre datasets de entrenamiento e inferencia

📁 notebooks/01_data_quality.ipynb
📁 data/processed/

Fase 2 — Feature Engineering

Se crean variables críticas para series temporales:

Variables temporales:
anio, mes, dia_mes, dia_semana, semana_anio, trimestre

Variables de precio:
precio_base, precio_venta, descuento_porcentaje

Competencia:
precio_competencia, ratio_precio

Lags:
lag_1 a lag_7

Media móvil:
media_movil_7

Eventos especiales:
es_black_friday, es_festivo, es_fin_de_semana

📁 notebooks/02_feature_engineering.ipynb

Fase 3 — Modelado (Machine Learning)

Modelo final: HistGradientBoostingRegressor

Incluye:

División Train/Test

Evaluación MAE, RMSE, R²

Exportación del modelo en .joblib

📁 notebooks/03_modelo_ml.ipynb
📁 models/modelo_final.joblib

Fase 4 — Predicción Recursiva + Simulador

La app ejecuta:

Predicción día a día

Actualización de lags con predicciones generadas

Ajuste de escenarios:

Precio

Descuento

Competencia

Comparativa automática de escenarios

📁 app/app.py

🖥️ 4. Aplicación Streamlit

La app incluye:

✔ Selección de producto

✔ Ajuste de descuento
✔ Escenarios de competencia
✔ KPIs principales
✔ Gráfico diario de predicciones
✔ Tabla detallada con Black Friday marcado
✔ Comparativa entre escenarios (0%, -5%, +5%)

Listo para usuarios no técnicos (dirección, ventas, pricing).

🚀 5. Deployment

Preparado para deploy en:

Streamlit Cloud

Railway

Render

HuggingFace Spaces

Archivos necesarios:

app/app.py

requirements.txt

📄 6. Disclaimer

Este proyecto está construido bajo un enfoque business-first:
convertir Machine Learning en herramientas reales que permiten tomar decisiones comerciales.

Cualquier VP, CTO, COO, Director Comercial o Pricing Manager puede utilizar esta app sin conocer Python.

👤 Autor

Albert Bañeres
Data Analytics & Machine Learning — Decision Intelligence Systems
