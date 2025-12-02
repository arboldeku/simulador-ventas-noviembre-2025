# 🛒 Simulador de Ventas Diario — Noviembre 2025

**Predicción diaria de demanda con Machine Learning + ajustes de precio y competencia**

Este proyecto construye un **simulador interactivo** para prever ventas diarias de productos durante Noviembre de 2025, combinando:

- Modelos de Machine Learning  
- Predicción recursiva día a día  
- Ajustes dinámicos de precio y competencia  
- Una app en Streamlit para equipos comerciales y directivos

---

## 🧱 1. Arquitectura del Proyecto

```bash
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
│   ├── requirements.t
```

## 🎯 2. Objetivo

El objetivo del proyecto es construir una herramienta que permita responder de forma inmediata preguntas críticas de negocio como:

- **¿Cuántas unidades voy a vender cada día?**
- **¿Qué ocurre si bajo el precio un 10%?**
- **¿Cómo afecta un cambio de precio en la competencia?**
- **¿Qué impacto tiene el Black Friday sobre las ventas?**

Esta herramienta permite a equipos de negocio simular distintos escenarios y tomar decisiones con datos reales y modelos de Machine Learning.

### 👥 ¿A quién va dirigido?

- 📦 **Demand Planners**
- 💰 **Pricing Managers**
- 📊 **Directores Comerciales**
- 🧠 **CTOs / COOs / VPs**
- 🛒 **Equipos de Retail & E-commerce**

La finalidad es acercar la ciencia de datos a la toma de decisiones diaria del negocio.

## ⚙️ 3. Metodología del Proyecto

El proyecto sigue una metodología estructurada en **4 fases**, alineada con la forma en que se ejecutan proyectos reales de Data Science en empresas.

---

### 🔍 **Fase 1 — Calidad de Datos & Exploración**
En esta fase se realiza:

- Revisión de consistencia, duplicados y valores nulos.  
- Detección de outliers.  
- Validación de rangos de precio, fechas y categorías.  
- Análisis Exploratorio (EDA) para entender patrones y estacionalidad.

**Archivos relevantes:**
- `notebooks/01_data_quality.ipynb`
- `notebooks/02_exploratory_analysis.ipynb`
- `data/raw/`

---

### 🏗️ **Fase 2 — Feature Engineering & Preparación**
Creación de variables clave para el modelo:

- Lags (`lag_1` … `lag_7`)
- Medias móviles (MA7)
- Señales de precio y competencia  
- Dummies de producto, categoría, subcategoría  
- Flags de Black Friday, Cyber Monday, fin de semana  
- Enriquecimiento temporal (día, semana, trimestre)

**Archivos relevantes:**
- `notebooks/03_feature_engineering.ipynb`
- `data/processed/df_inferencia_transformado.csv`

---

### 🤖 **Fase 3 — Entrenamiento del Modelo**
Entrenamiento del modelo final:

- Algoritmo: **HistGradientBoostingRegressor**
- Validación temporal  
- Optimización de hiperparámetros  
- Análisis de importancia de variables  
- Métricas finales del modelo

**Archivos relevantes:**
- `notebooks/04_model_training.ipynb`
- `models/modelo_final.joblib`

---

### 📈 **Fase 4 — Predicción & Simulación**
Una vez entrenado el modelo:

- Se genera la predicción diaria para noviembre.  
- Se implementa **predicción recursiva día a día**, actualizando Lags y medias móviles.  
- Se construye un simulador que permite:
  - Cambiar descuentos.
  - Modificar precios de la competencia.
  - Evaluar escenarios.

**Archivos relevantes:**
- `notebooks/05_inference.ipynb`
- `app/app.py`
- `data/processed/predicciones_noviembre_2025.csv`

---

Esta metodología permite pasar de **datos brutos → modelo → app interactiva**, replicando exactamente la forma en que Isaac estructura proyectos en el curso.

## 📊 4. Proceso Técnico del Proyecto

El proyecto sigue un flujo completo de Machine Learning aplicado a previsión de ventas, dividido en 4 fases claras. Cada fase refleja parte del proceso real que sigue un equipo de Data Science para construir un sistema predictivo listo para negocio.

### 🔍 Fase 1 — Ingesta y Calidad de Datos

En esta fase se prepararon los datos de ventas y atributos necesarios para poder entrenar modelos fiables.

Incluye:
  - Importación de datos brutos (raw/)
  - Limpieza inicial e imputación de valores faltantes
  - Detección y corrección de outliers
  - Verificación de coherencias temporales
  - Generación de dataset base para análisis

🎯 Objetivo: Garantizar que los datos son consistentes, completos y utilizables para el modelado.

### 📈 Fase 2 — Análisis Exploratorio (EDA)

Aquí se estudió cómo se comportan las ventas, los precios y la competencia, así como su impacto temporal.

Incluye:

  - Análisis de estacionalidad (día, semana, mes)
  - Visualización de tendencias y patrones
  - Distribución de precios y descuentos
  - Comparativa de ventas por categoría y producto
  - Identificación de drivers principales de demanda

🎯 Objetivo: Entender qué mueve las ventas antes de modelar.

### 🧪 Fase 3 — Feature Engineering & Preparación para ML

El paso más crítico del proyecto. Aquí se crearon las variables que el modelo necesita para predecir correctamente.

Incluye:

  -  de ventas (lag_1…lag_7)
  - Media móvil de 7 días (media_movil_7)
  - Variables de calendario: festivos, fin de semana, Black Friday, Cyber Monday
  - Codificación one-hot (dummies) de: producto, categoría, subcategoría
  - Variables de precio:
  - descuento (%)
  - precio competencia
  - ratio precio vs competencia

🎯 Objetivo: Construir un dataset rico y modelizable para capturar patrones reales de demanda.

### 🤖 Fase 4 — Modelización y Predicción Recursiva

El modelo final utilizado es un HistGradientBoostingRegressor, optimizado para series temporales con regresión tabular.

Incluye:

- División entrenamiento / validación
- Entrenamiento de varios modelos base
- Selección del modelo final según MAE, RMSE y error relativo por producto
- Implementación de predicción recursiva:
- Día 1 se predice desde los lags reales
- Día 2 usa el resultado del día 1
- Día 3 usa resultados de día 1 y día 2
- …y así hasta el día 30

Exportación del modelo final en modelo_final.joblib

🎯 Objetivo: Predecir ventas día a día usando las predicciones previas, igual que en un entorno real.

🧩 5. App Interactiva en Streamlit

La última fase del proyecto consiste en transformar el modelo creado en una aplicación interactiva que permita a equipos comerciales, de pricing y dirección simular escenarios reales de negocio en segundos.

La app está diseñada para ser intuitiva, rápida y orientada a toma de decisiones.

### 🖥️ ¿Qué permite hacer la app?

  - Seleccionar el producto a simular
  - Ajustar el descuento del precio base
  - Cambiar el escenario de competencia (+5%, −5%, actual)
  - Predecir las ventas día a día para Noviembre 2025
  - Visualizar resultados en un gráfico claro y accesible
  - Mostrar tabla de datos final exportable

🎯 Objetivo: Permitir al usuario evaluar decisiones de pricing y competencia de manera inmediata.

### ⚙️ ¿Cómo funciona por dentro?

  - La app usa el modelo entrenado (modelo_final.joblib) y reconstruye las condiciones del usuario:
  - Carga el dataset base de inferencia
  - Aplica el ajuste de precio seleccionado
  - Aplica el escenario de competencia elegido
  - Ejecuta la predicción recursiva día a día
  - Genera la serie completa de ventas simuladas

Renderiza:

- gráfico de ventas
- tabla
- métricas clave

```bash
Forecasting Ventas/
│
└── app/
    └── app.py
```

### 🚀 Experiencia de usuario (UX)

La app está diseñada siguiendo principios de claridad y velocidad:

- Sidebar con todos los controles
- Botón claro: “Simular ventas”
- Gráficos visibles de inmediato
- Mensajes de ayuda contextual
- Código optimizado para cargar en segundos

## 🏁 6. Conclusiones

Este proyecto demuestra cómo un flujo completo de Machine Learning aplicado al negocio puede resolver preguntas clave de ventas, pricing y competencia con rapidez y precisión.

# Integra:

  - Procesamiento y preparación profesional de datos
  - Modelización predictiva robusta
  - Predicción diaria y recursiva
  - Una app interactiva para convertir el modelo en decisiones reales

El resultado es una herramienta capaz de simular escenarios comerciales en segundos, pensada para equipos de demanda, pricing y dirección.

# Este proyecto es totalmente extensible a:

- Nuevos productos
- Otros periodos temporales
- Nuevos modelos
- Integraciones reales en sistemas internos o dashboards ejecutivos

Una base sólida para construir soluciones de analítica avanzada orientadas al negocio.
