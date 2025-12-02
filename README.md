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


