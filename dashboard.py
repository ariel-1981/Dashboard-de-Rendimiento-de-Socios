import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Rendimiento Físico del Gimnasio", page_icon="💪", layout="wide")
st.title("💪 Dashboard de Rendimiento Físico de Socios")

# --- CARGA DE DATOS DESDE GITHUB ---
@st.cache_data
def cargar_datos():
    # URL del archivo raw en GitHub
    url = "https://raw.githubusercontent.com/ariel-1981/Dashboard-de-Rendimiento-de-Socios/refs/heads/main/datos.csv"
    
    try:
        df = pd.read_csv(url)
        
        # Debug: mostrar columnas disponibles
        st.sidebar.info(f"Columnas encontradas: {', '.join(df.columns.tolist())}")
        
        # Verificar que existan las columnas necesarias
        columnas_requeridas = ["Peso_Inicial", "Peso_Actual"]
        if not all(col in df.columns for col in columnas_requeridas):
            st.error(f"Faltan columnas requeridas. Columnas disponibles: {df.columns.tolist()}")
            return pd.DataFrame()
        
        df["Progreso_Peso (%)"] = ((df["Peso_Inicial"] - df["Peso_Actual"]) / df["Peso_Inicial"]) * 100
        return df
    except Exception as e:
        st.error(f"Error al cargar datos desde GitHub: {e}")
        st.info("Asegúrate de que la URL apunta al archivo raw correcto en GitHub")
        return pd.DataFrame()

df = cargar_datos()

# Verificar que los datos se cargaron correctamente
if df.empty:
    st.warning("⚠️ No se pudieron cargar los datos. Verifica la URL de GitHub.")
    st.stop()

# --- SIDEBAR FILTROS ---
st.sidebar.header("Filtros")
genero = st.sidebar.multiselect("Género", df["Género"].unique(), default=df["Género"].unique())
nivel = st.sidebar.multiselect("Nivel de entrenamiento", df["Nivel"].unique(), default=df["Nivel"].unique())
horario = st.sidebar.multiselect("Horario", df["Horario"].unique(), default=df["Horario"].unique())

df_filtrado = df[
    (df["Género"].isin(genero)) &
    (df["Nivel"].isin(nivel)) &
    (df["Horario"].isin(horario))
]

# --- MÉTRICAS CLAVE ---
st.subheader("📈 Indicadores de Rendimiento")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Promedio Frecuencia Semanal", f"{df_filtrado['Frecuencia_Semanal'].mean():.1f} días")
col2.metric("Duración Promedio", f"{df_filtrado['Duración_Promedio'].mean():.0f} min")
col3.metric("Promedio Progreso Peso", f"{df_filtrado['Progreso_Peso (%)'].mean():.1f}%")
col4.metric("Peso Promedio Actual", f"{df_filtrado['Peso_Actual'].mean():.1f} kg")

st.divider()

# --- VISUALIZACIONES ---
col1, col2 = st.columns(2)

# 📊 Progreso por socio
with col1:
    st.subheader("🏋️ Progreso de Peso por Socio")
    fig = px.bar(
        df_filtrado, 
        x="Socio", 
        y="Progreso_Peso (%)", 
        color="Nivel", 
        text_auto=".1f",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

# 🔥 Ejercicios más populares
with col2:
    st.subheader("🔥 Ejercicios Más Populares")
    fav = df_filtrado["Ejercicio_Favorito"].value_counts().reset_index()
    fav.columns = ["Ejercicio", "Cantidad"]
    fig2 = px.pie(fav, values="Cantidad", names="Ejercicio", hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)

# --- SEGUNDA FILA DE GRÁFICOS ---
col3, col4 = st.columns(2)

# 📆 Frecuencia vs Duración
with col3:
    st.subheader("📅 Relación entre Frecuencia y Duración de Entrenamiento")
    fig3 = px.scatter(
        df_filtrado,
        x="Frecuencia_Semanal",
        y="Duración_Promedio",
        size="Progreso_Peso (%)",
        color="Nivel",
        hover_data=["Socio"]
    )
    st.plotly_chart(fig3, use_container_width=True)

# 💪 Comparativa por nivel
with col4:
    st.subheader("💥 Promedio de Progreso por Nivel de Entrenamiento")
    nivel_prog = df_filtrado.groupby("Nivel")["Progreso_Peso (%)"].mean().reset_index()
    fig4 = px.bar(nivel_prog, x="Nivel", y="Progreso_Peso (%)", color="Nivel", text_auto=".1f")
    st.plotly_chart(fig4, use_container_width=True)

# --- TABLA DE DATOS ---
st.divider()
st.subheader("📋 Datos Filtrados")
st.dataframe(df_filtrado, use_container_width=True)

st.caption("Dashboard desarrollado por Santiago Bayaslian 🧠 | Instituto Tecnológico Beltrán")
