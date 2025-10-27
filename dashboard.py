import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Rendimiento Físico del Gimnasio", page_icon="💪", layout="wide")
st.title("💪 Dashboard de Rendimiento Físico de Socios")

# --- DATOS DIRECTAMENTE EN EL CÓDIGO ---
@st.cache_data
def cargar_datos():
    datos = {
        'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
               41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
               61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
        'Socio': ['Ana', 'Carlos', 'Lucía', 'Marcos', 'Sofía', 'Julián', 'Paula', 'Tomás', 'Martina', 'Diego',
                  'Valentina', 'Federico', 'Camila', 'Sebastián', 'Florencia', 'Matías', 'Daniela', 'Facundo', 'Agustina', 'Nicolás',
                  'Jimena', 'Gonzalo', 'Victoria', 'Ignacio', 'Carolina', 'Ezequiel', 'Aldana', 'Lucas', 'Romina', 'Maximiliano',
                  'Micaela', 'Rodrigo', 'Brenda', 'Gastón', 'Natalia', 'Leandro', 'Melina', 'Pablo', 'Celeste', 'Mariano',
                  'Julieta', 'Emiliano', 'Sabrina', 'Adrián', 'Eugenia', 'Claudio', 'Lorena', 'Damián', 'Gabriela', 'Hernán',
                  'Yanina', 'Cristian', 'Marina', 'Javier', 'Andrea', 'Rubén', 'Valeria', 'Gustavo', 'Silvina', 'Oscar',
                  'Carla', 'Ramiro', 'Noelia', 'Marcelo', 'Mónica', 'Jorge', 'Roxana', 'Alberto', 'Fernanda', 'Sergio',
                  'Karina', 'Martín', 'Claudia', 'Ricardo', 'Soledad', 'Daniel', 'Verónica', 'Alejandro', 'Laura', 'Fernando'],
        'Edad': [25, 32, 28, 40, 22, 35, 30, 27, 26, 31,
                 24, 29, 33, 38, 23, 34, 27, 26, 31, 36,
                 25, 39, 28, 30, 32, 27, 24, 35, 29, 41,
                 26, 33, 23, 37, 30, 28, 25, 34, 27, 40,
                 24, 31, 29, 36, 26, 38, 32, 27, 25, 35,
                 28, 39, 30, 33, 24, 37, 26, 41, 29, 34,
                 27, 31, 23, 36, 32, 28, 25, 38, 30, 35,
                 26, 40, 29, 33, 24, 37, 31, 28, 25, 34],
        'Género': ['Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino',
                   'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino',
                   'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino',
                   'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino',
                   'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino',
                   'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino',
                   'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino',
                   'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino'],
        'Nivel': ['Intermedio', 'Avanzado', 'Principiante', 'Intermedio', 'Intermedio', 'Avanzado', 'Intermedio', 'Principiante', 'Avanzado', 'Intermedio',
                  'Principiante', 'Intermedio', 'Avanzado', 'Intermedio', 'Principiante', 'Avanzado', 'Intermedio', 'Principiante', 'Avanzado', 'Intermedio',
                  'Intermedio', 'Avanzado', 'Principiante', 'Intermedio', 'Avanzado', 'Principiante', 'Intermedio', 'Avanzado', 'Intermedio', 'Principiante',
                  'Avanzado', 'Intermedio', 'Principiante', 'Avanzado', 'Intermedio', 'Principiante', 'Avanzado', 'Intermedio', 'Intermedio', 'Avanzado',
                  'Principiante', 'Intermedio', 'Avanzado', 'Principiante', 'Intermedio', 'Avanzado', 'Intermedio', 'Principiante', 'Avanzado', 'Intermedio',
                  'Principiante', 'Avanzado', 'Intermedio', 'Principiante', 'Avanzado', 'Intermedio', 'Intermedio', 'Avanzado', 'Principiante', 'Intermedio',
                  'Avanzado', 'Principiante', 'Intermedio', 'Avanzado', 'Intermedio', 'Principiante', 'Avanzado', 'Intermedio', 'Principiante', 'Avanzado',
                  'Intermedio', 'Principiante', 'Avanzado', 'Intermedio', 'Principiante', 'Avanzado', 'Intermedio', 'Principiante', 'Avanzado', 'Intermedio'],
        'Frecuencia_Semanal': [5, 4, 6, 2, 6, 3, 5, 3, 6, 3,
                               4, 5, 5, 3, 5, 4, 6, 4, 5, 3,
                               5, 4, 6, 4, 5, 3, 6, 4, 5, 2,
                               6, 4, 5, 3, 5, 4, 6, 3, 5, 4,
                               6, 3, 5, 4, 6, 4, 5, 3, 6, 4,
                               5, 3, 5, 4, 6, 3, 5, 4, 6, 3,
                               5, 4, 6, 4, 5, 3, 6, 4, 5, 3,
                               5, 2, 6, 4, 5, 4, 5, 3, 6, 4],
        'Duración_Promedio': [65, 70, 50, 55, 60, 80, 65, 45, 70, 50,
                              55, 60, 75, 65, 50, 85, 60, 45, 70, 55,
                              65, 80, 50, 60, 75, 45, 55, 85, 65, 50,
                              70, 60, 50, 80, 65, 45, 75, 55, 60, 85,
                              50, 60, 70, 45, 55, 80, 65, 50, 75, 60,
                              50, 85, 65, 45, 70, 55, 60, 80, 50, 60,
                              75, 45, 55, 85, 65, 50, 70, 60, 50, 80,
                              65, 45, 75, 60, 50, 85, 65, 50, 70, 55],
        'Peso_Inicial': [64, 85, 60, 92, 58, 88, 70, 76, 62, 81,
                        68, 78, 65, 90, 55, 95, 63, 72, 67, 84,
                        61, 93, 59, 80, 66, 74, 62, 89, 64, 95,
                        60, 82, 57, 91, 69, 77, 63, 85, 65, 94,
                        58, 83, 66, 79, 62, 90, 68, 75, 61, 86,
                        64, 92, 67, 81, 59, 87, 63, 96, 66, 84,
                        62, 78, 60, 91, 70, 76, 61, 88, 65, 93,
                        64, 94, 63, 85, 58, 90, 68, 77, 60, 86],
        'Peso_Actual': [62, 83, 59, 91, 56, 86, 68, 75, 60, 80,
                       66, 76, 63, 88, 54, 92, 61, 71, 65, 82,
                       59, 90, 58, 78, 64, 73, 60, 86, 62, 94,
                       58, 80, 56, 88, 67, 76, 61, 83, 63, 91,
                       57, 81, 64, 78, 60, 87, 66, 74, 59, 84,
                       63, 89, 65, 80, 57, 85, 61, 93, 65, 82,
                       60, 77, 58, 88, 68, 75, 59, 86, 64, 90,
                       62, 93, 61, 83, 57, 87, 66, 76, 58, 84],
        'Ejercicio_Favorito': ['Sentadillas', 'Peso Muerto', 'Correr', 'Bicicleta', 'Correr', 'Press Banca', 'Sentadillas', 'Correr', 'Peso Muerto', 'Bicicleta',
                              'Yoga', 'Press Banca', 'Sentadillas', 'Bicicleta', 'Correr', 'Peso Muerto', 'Yoga', 'Correr', 'Press Banca', 'Bicicleta',
                              'Sentadillas', 'Peso Muerto', 'Yoga', 'Press Banca', 'Correr', 'Bicicleta', 'Sentadillas', 'Peso Muerto', 'Yoga', 'Correr',
                              'Press Banca', 'Bicicleta', 'Sentadillas', 'Peso Muerto', 'Correr', 'Yoga', 'Press Banca', 'Bicicleta', 'Sentadillas', 'Peso Muerto',
                              'Correr', 'Press Banca', 'Yoga', 'Bicicleta', 'Sentadillas', 'Peso Muerto', 'Correr', 'Press Banca', 'Yoga', 'Bicicleta',
                              'Sentadillas', 'Peso Muerto', 'Correr', 'Yoga', 'Press Banca', 'Bicicleta', 'Sentadillas', 'Peso Muerto', 'Correr', 'Press Banca',
                              'Yoga', 'Bicicleta', 'Sentadillas', 'Peso Muerto', 'Correr', 'Press Banca', 'Yoga', 'Bicicleta', 'Sentadillas', 'Peso Muerto',
                              'Correr', 'Yoga', 'Press Banca', 'Bicicleta', 'Sentadillas', 'Peso Muerto', 'Correr', 'Press Banca', 'Yoga', 'Bicicleta'],
        'Horario': ['Mañana', 'Tarde', 'Mañana', 'Noche', 'Mañana', 'Tarde', 'Tarde', 'Noche', 'Mañana', 'Tarde',
                   'Mañana', 'Tarde', 'Mañana', 'Noche', 'Mañana', 'Tarde', 'Tarde', 'Noche', 'Mañana', 'Tarde',
                   'Mañana', 'Tarde', 'Noche', 'Mañana', 'Tarde', 'Noche', 'Mañana', 'Tarde', 'Tarde', 'Noche',
                   'Mañana', 'Tarde', 'Mañana', 'Noche', 'Tarde', 'Noche', 'Mañana', 'Tarde', 'Mañana', 'Tarde',
                   'Noche', 'Mañana', 'Tarde', 'Noche', 'Mañana', 'Tarde', 'Tarde', 'Noche', 'Mañana', 'Tarde',
                   'Mañana', 'Noche', 'Tarde', 'Noche', 'Mañana', 'Tarde', 'Mañana', 'Tarde', 'Noche', 'Mañana',
                   'Tarde', 'Noche', 'Mañana', 'Tarde', 'Tarde', 'Noche', 'Mañana', 'Tarde', 'Mañana', 'Noche',
                   'Tarde', 'Noche', 'Mañana', 'Tarde', 'Mañana', 'Tarde', 'Noche', 'Mañana', 'Tarde', 'Noche']
    }
    
    df = pd.DataFrame(datos)
    df["Progreso_Peso (%)"] = ((df["Peso_Inicial"] - df["Peso_Actual"]) / df["Peso_Inicial"]) * 100
    return df

df = cargar_datos()

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

st.caption("Dashboard desarrollado por Ariel Buchholz 🧠 | Instituto Tecnológico Beltrán")
