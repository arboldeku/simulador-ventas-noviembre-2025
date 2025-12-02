
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import joblib
from sklearn.ensemble import HistGradientBoostingRegressor

# =========================================
# CARGA INICIAL DEL MODELO Y DEL DATAFRAME
# =========================================
try:
    MODEL_PATH = "../models/modelo_final.joblib"
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error(f"❌ Error al cargar el modelo desde {MODEL_PATH}: {e}")
    st.stop()

try:
    DATA_PATH = "../data/processed/df_inferencia_transformado.csv"
    df_inf = pd.read_csv(DATA_PATH)
except Exception as e:
    st.error(f"❌ Error al cargar el dataframe desde {DATA_PATH}: {e}")
    st.stop()


# =========================================
# FUNCIONES CACHEADAS
# =========================================
@st.cache_resource
def cargar_modelo(ruta_modelo: str):
    try:
        return joblib.load(ruta_modelo)
    except Exception as e:
        st.error(f"❌ Error cargando modelo: {e}")
        return None


@st.cache_data
def cargar_df_inferencia(ruta_csv: str):
    try:
        return pd.read_csv(ruta_csv)
    except Exception as e:
        st.error(f"❌ Error cargando CSV: {e}")
        return None


# =========================================
# FUNCIONES DE UTILIDAD
# =========================================
def obtener_mapeo_productos(df_inferencia: pd.DataFrame):
    cols_nombre = [c for c in df_inferencia.columns if c.startswith("nombre_h_")]
    mapeo = {c.replace("nombre_h_", ""): c for c in cols_nombre}
    return mapeo


def ajustar_precios_y_competencia(df_prod, descuento_slider, escenario_comp):
    df = df_prod.copy()

    factor_desc = 1 + (descuento_slider / 100)
    df["precio_venta"] = df["precio_base"] * factor_desc
    df["descuento_porcentaje"] = ((df["precio_base"] - df["precio_venta"]) / df["precio_base"]) * 100

    if escenario_comp == "Actual (0%)":
        fc = 1.0
    elif escenario_comp == "Competencia -5%":
        fc = 0.95
    else:
        fc = 1.05

    if "precio_competencia" in df.columns:
        df["precio_competencia"] = df["precio_competencia"] * fc
        df["ratio_precio"] = df["precio_venta"] / df["precio_competencia"]

    return df


# =========================================
# PREDICCIÓN RECURSIVA
# =========================================
def simular_predicciones_recursivas(
    df_inferencia, modelo, nombre_col_dummy_producto,
    descuento_slider, escenario_comp
):
    if modelo is None:
        return None

    if nombre_col_dummy_producto not in df_inferencia.columns:
        st.error(f"❌ Columna dummy no existe: {nombre_col_dummy_producto}")
        return None

    df_prod = df_inferencia[df_inferencia[nombre_col_dummy_producto] == 1].copy()

    if df_prod.empty:
        st.error("❌ No hay datos para este producto.")
        return None

    df_prod = df_prod.sort_values("dia_mes").reset_index(drop=True)
    df_prod = ajustar_precios_y_competencia(df_prod, descuento_slider, escenario_comp)

    if hasattr(modelo, "feature_names_in_"):
        cols_modelo = list(modelo.feature_names_in_)
    else:
        cols_modelo = [c for c in df_prod.columns if c != "predicciones"]

    for col in cols_modelo:
        if col not in df_prod.columns:
            df_prod[col] = 0

    predicciones = []
    ultimas = []

    for i in range(len(df_prod)):
        X_row = df_prod.loc[[i], cols_modelo]
        y_hat = float(modelo.predict(X_row)[0])
        df_prod.loc[i, "prediccion"] = y_hat
        predicciones.append(y_hat)
        ultimas.append(y_hat)

        if i < len(df_prod) - 1:
            df_prod.loc[i+1, "lag_7"] = df_prod.loc[i, "lag_6"]
            df_prod.loc[i+1, "lag_6"] = df_prod.loc[i, "lag_5"]
            df_prod.loc[i+1, "lag_5"] = df_prod.loc[i, "lag_4"]
            df_prod.loc[i+1, "lag_4"] = df_prod.loc[i, "lag_3"]
            df_prod.loc[i+1, "lag_3"] = df_prod.loc[i, "lag_2"]
            df_prod.loc[i+1, "lag_2"] = df_prod.loc[i, "lag_1"]
            df_prod.loc[i+1, "lag_1"] = y_hat

            df_prod.loc[i+1, "media_movil_7"] = np.mean(ultimas[-7:])

    return df_prod


# =========================================
# KPIS Y TABLA DETALLE
# =========================================
def calcular_kpis(df_sim):
    if df_sim is None or df_sim.empty:
        return None

    return {
        "unidades_totales": df_sim["prediccion"].sum(),
        "ingresos_totales": (df_sim["prediccion"] * df_sim["precio_venta"]).sum(),
        "precio_medio": df_sim["precio_venta"].mean(),
        "descuento_medio": df_sim["descuento_porcentaje"].mean(),
    }


def preparar_tabla_detalle(df_sim):
    df = df_sim.copy()
    df["fecha_str"] = df.apply(lambda r: f"{int(r['anio'])}-11-{int(r['dia_mes']):02d}", axis=1)
    df["ingresos_dia"] = df["prediccion"] * df["precio_venta"]

    columnas = ["fecha_str", "precio_venta", "precio_competencia",
                "descuento_porcentaje", "prediccion", "ingresos_dia", "es_black_friday"]
    columnas = [c for c in columnas if c in df.columns]

    df_tabla = df[columnas].copy()
    df_tabla = df_tabla.rename(columns={
        "fecha_str": "Fecha",
        "precio_venta": "Precio venta (€)",
        "precio_competencia": "Precio competencia (€)",
        "descuento_porcentaje": "Descuento (%)",
        "prediccion": "Unidades predichas",
        "ingresos_dia": "Ingresos día (€)",
    })

    return df_tabla


# =========================================
# STREAMLIT - MAIN
# =========================================
def main():

    st.set_page_config(page_title="Simulador de Ventas", page_icon="📈", layout="wide")

    st.title("📈 Simulador de Ventas - Noviembre 2025")

    ruta_modelo = "../models/modelo_final.joblib"
    ruta_inferencia = "../data/processed/df_inferencia_transformado.csv"

    modelo = cargar_modelo(ruta_modelo)
    df_inferencia = cargar_df_inferencia(ruta_inferencia)

    if modelo is None or df_inferencia is None:
        st.stop()

    # ------------------------------
    # SIDEBAR
    # ------------------------------
    st.sidebar.header("🛠️ Controles de simulación")

    mapeo = obtener_mapeo_productos(df_inferencia)
    lista_prod = sorted(list(mapeo.keys()))

    producto = st.sidebar.selectbox("Producto:", options=lista_prod)
    nombre_dummy = mapeo[producto]     # 🔥 AHORA SÍ ESTÁ DEFINIDO AQUÍ

    descuento = st.sidebar.slider("Ajuste de descuento (%)", -50, 50, 0, step=5)

    escenario = st.sidebar.radio(
        "Escenario de competencia:",
        ["Actual (0%)", "Competencia -5%", "Competencia +5%"]
    )

    simular = st.sidebar.button("🚀 Simular ventas", type="primary")

    # ------------------------------
    # INFO DEL PRODUCTO (ESTILO ISAAC)
    # ------------------------------
    st.markdown("---")
    st.subheader(f"📊 Información del producto: **{producto}**")

    df_base = df_inferencia[df_inferencia[nombre_dummy] == 1].copy()

    if df_base.empty:
        st.warning("⚠️ No hay datos base del producto.")
    else:
        fila = df_base.iloc[0]

        # reconstrucción categoría
        cat_cols = [c for c in df_inferencia.columns if c.startswith("categoria_h_")]
        categoria = next((c.replace("categoria_h_", "") for c in cat_cols if fila[c] == 1), "N/A")

        # reconstrucción subcategoría
        sub_cols = [c for c in df_inferencia.columns if c.startswith("subcategoria_h_")]
        subcategoria = next((c.replace("subcategoria_h_", "") for c in sub_cols if fila[c] == 1), "N/A")

        precio_base = fila["precio_base"]

        c1, c2, c3 = st.columns(3)
        c1.info(f"**Categoría**\n\n### {categoria}")
        c2.info(f"**Subcategoría**\n\n### {subcategoria}")
        c3.info(f"**Precio Base**\n\n### €{precio_base:.2f}")

    if not simular:
        st.info("👈 Ajusta los controles y pulsa **Simular ventas**.")
        st.stop()

    # ------------------------------
    # PREDICCIÓN
    # ------------------------------
    with st.spinner("Calculando predicciones..."):
        df_sim = simular_predicciones_recursivas(
            df_inferencia, modelo, nombre_dummy, descuento, escenario
        )

    if df_sim is None:
        st.stop()

    kpis = calcular_kpis(df_sim)

    # ------------------------------
    # KPIs
    # ------------------------------
    st.markdown("### 🔢 KPIs del escenario seleccionado")

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Unidades totales", f"{kpis['unidades_totales']:.0f}")
    k2.metric("Ingresos totales", f"{kpis['ingresos_totales']:.2f} €")
    k3.metric("Precio medio", f"{kpis['precio_medio']:.2f} €")
    k4.metric("Descuento medio", f"{kpis['descuento_medio']:.1f} %")

    # ------------------------------
    # GRÁFICO
    # ------------------------------
    st.markdown("### 📉 Predicción diaria")

    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(data=df_sim, x="dia_mes", y="prediccion", marker="o", ax=ax)

    st.pyplot(fig)

    # ------------------------------
    # TABLA DETALLADA
    # ------------------------------
    st.markdown("### 📋 Tabla Detallada")

    tabla = preparar_tabla_detalle(df_sim)

    st.dataframe(tabla, use_container_width=True)

    st.success("✅ Simulación completada.")


if __name__ == "__main__":
    main()
