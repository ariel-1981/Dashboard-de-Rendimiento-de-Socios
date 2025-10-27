# 💪 Dashboard de Rendimiento Físico de Socios

Dashboard interactivo desarrollado con Streamlit para análisis y visualización del rendimiento físico de socios de gimnasio.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dashboard-gimnasio.streamlit.app/)

## 📋 Descripción

Aplicación web que permite analizar el rendimiento de 80 socios de un gimnasio, incluyendo métricas de asistencia, progreso de peso, preferencias de ejercicio y patrones de entrenamiento. El dashboard ofrece visualizaciones interactivas y filtros dinámicos para explorar los datos desde diferentes perspectivas.

## 🎯 Características

- **Métricas en tiempo real**: Indicadores clave de rendimiento
- **Visualizaciones interactivas**: Gráficos dinámicos con Plotly
- **Filtros personalizables**: Por género, nivel y horario
- **Análisis de progreso**: Seguimiento de evolución de peso
- **Datos integrados**: Dataset incorporado en el código

## 📊 Visualizaciones Incluidas

1. **Progreso de Peso por Socio** - Gráfico de barras con código de colores por nivel
2. **Ejercicios Más Populares** - Gráfico de pastel con distribución de preferencias
3. **Relación Frecuencia vs Duración** - Scatter plot interactivo
4. **Promedio de Progreso por Nivel** - Comparativa entre niveles de entrenamiento
5. **Tabla de Datos Filtrados** - Dataset completo con filtros aplicados

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Streamlit** - Framework de aplicación web
- **Pandas** - Manipulación y análisis de datos
- **Plotly** - Visualizaciones interactivas

## 📦 Instalación

### Requisitos Previos

```bash
python >= 3.8
pip
```

### Pasos de Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/ariel-1981/Dashboard-de-Rendimiento-de-Socios.git
cd Dashboard-de-Rendimiento-de-Socios
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
streamlit run app.py
```

4. Abre tu navegador en `http://localhost:8501`

## 🚀 Deployment en Streamlit Cloud

### Opción 1: Desde GitHub (Recomendado)

1. Pushea tu código a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu repositorio
4. Selecciona la rama `main` y el archivo `app.py`
5. ¡Deploy!

### Opción 2: Desde la App

```bash
streamlit run app.py
# Click en "Deploy" en el menú superior derecho
```

## 📁 Estructura del Proyecto

```
Dashboard-de-Rendimiento-de-Socios/
│
├── app.py                 # Aplicación principal de Streamlit
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
└── informe.md            # Informe descriptivo de resultados
```

## 📈 Dataset

El dataset incluye información de **80 socios** con las siguientes variables:

| Variable | Descripción |
|----------|-------------|
| ID | Identificador único del socio |
| Socio | Nombre del socio |
| Edad | Edad del socio (22-41 años) |
| Género | Femenino / Masculino |
| Nivel | Principiante / Intermedio / Avanzado |
| Frecuencia_Semanal | Días de entrenamiento por semana (2-6) |
| Duración_Promedio | Minutos promedio por sesión (45-85) |
| Peso_Inicial | Peso al inicio del período (kg) |
| Peso_Actual | Peso actual (kg) |
| Ejercicio_Favorito | Ejercicio preferido del socio |
| Horario | Mañana / Tarde / Noche |

**Nota**: Los datos son ficticios y fueron generados con fines educativos y de demostración.

## 🎨 Filtros Disponibles

- **Género**: Femenino, Masculino
- **Nivel de Entrenamiento**: Principiante, Intermedio, Avanzado
- **Horario**: Mañana, Tarde, Noche

Los filtros se actualizan en tiempo real y afectan todas las visualizaciones y métricas.

## 📊 Métricas Principales

- **Promedio Frecuencia Semanal**: 4.4 días/semana
- **Duración Promedio**: 61 minutos
- **Promedio Progreso Peso**: 2.9%
- **Peso Promedio Actual**: 71.6 kg

## 🔍 Casos de Uso

- **Gestión de gimnasios**: Análisis de comportamiento de socios
- **Entrenadores personales**: Seguimiento de progreso de clientes
- **Investigación deportiva**: Estudio de patrones de entrenamiento
- **Educación**: Ejemplo de análisis de datos y visualización

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la [MIT License](LICENSE).

## 👤 Autor

**Ariel Buchholz**

- GitHub: [@ariel-1981](https://github.com/ariel-1981)
- Institución: Instituto Tecnológico Beltrán

## 🙏 Agradecimientos

- Instituto Tecnológico Beltrán por el apoyo académico
- Comunidad de Streamlit por la excelente documentación
- Plotly por las herramientas de visualización

## 📧 Contacto

Si tenés preguntas o sugerencias, no dudes en abrir un issue en el repositorio.

---

⭐ Si este proyecto te resultó útil, considerá darle una estrella en GitHub!

**Desarrollado con ❤️ por Ariel Buchholz | 2025**
