import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Cargar el DataFrame con joblib
try:
    df_train = joblib.load('df_train.joblib')  # Asegúrate de tener el archivo df_train.joblib en el directorio correcto
except FileNotFoundError:
    st.warning("El archivo 'df_train.joblib' no se encontró. Asegúrate de que el archivo de datos esté en el directorio adecuado.")
    df_train = None

# Cargar el archivo del modelo
modelo_cargado = joblib.load("Breast_cancer_model_gbc.joblib")

# Extraer el modelo del diccionario
modelo = modelo_cargado["model"]

# Configuración de la página
st.set_page_config(page_title="Predicción de Cáncer de Mama - Proyecto Final", layout="wide")

# CSS para diseño azul oscuro con texto negro y barra lateral con texto blanco
custom_css = """
<style>
body {
    background-color: #1A1A2E;  /* Fondo azul oscuro */
    color: black; /* Texto negro */
}
[data-testid="stSidebar"] {
    background-color: #16213E !important; /* Fondo más oscuro para la barra lateral */
    color: white !important; /* Texto blanco en la barra lateral */
}
.card {
    background-color: #0F3460; /* Fondo azul medio */
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
}
h1, h2, h3, h4, h5, h6 {
    color: black; /* Encabezados en negro */
}
.stMarkdown {
    color: black; /* Asegura que todo el texto sea negro */
}
.stButton > button {
    background-color: #0F3460 !important; /* Botones en azul medio */
    color: black !important; /* Texto negro en los botones */
    border-radius: 10px;
    padding: 10px;
    border: 1px solid black; /* Borde negro */
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] h4 {
    color: white !important; /* Asegura que los títulos en la barra lateral sean blancos */
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navegación del Proyecto")
selection = st.sidebar.radio("Ir a:", [
    "Introducción",
    "Análisis Exploratorio",
    "Optimización de Modelos",
    "Modelo Predictivo",
    "Conclusiones"
])

# Sección: Introducción
if selection == "Introducción":
    st.title("Proyecto Final - Predicción de Cáncer de Mama")
    st.markdown("""
        #### Latam Data Science - Promoción Nro. 3
        #### Predicción de Severidad del Cáncer de Mama
        ##### Autores:
        - **Heber Marin**
        - **Irvin Vallejo**
    """)

# Sección: Análisis Exploratorio
elif selection == "Análisis Exploratorio":
    st.header("Análisis Exploratorio de Datos")

    # Mostrar Análisis Univariado
    st.subheader("Análisis Univariado")
    if df_train is not None:
        fig, ax = plt.subplots(figsize=(20, 12))  # Tamaño grande para gráficos
        df_train.hist(ax=ax, bins=10, grid=False)
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.error("No se pudo cargar el DataFrame para el Análisis Univariado.")

    # Espacio entre gráficos
    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    # Mostrar Análisis Bivariado
    st.subheader("Análisis Bivariado: Heatmap de Correlación")
    if df_train is not None:
        fig, ax = plt.subplots(figsize=(20, 12))  # Tamaño grande para gráficos
        sns.heatmap(df_train.corr(), vmin=-1, vmax=1, annot=True, cmap="RdBu", ax=ax)
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.error("No se pudo cargar el DataFrame para el Análisis Bivariado.")

# Sección: Optimización de Modelos
elif selection == "Optimización de Modelos":
    st.header("Optimización de Modelos")
    st.markdown("""
        Para mejorar la precisión del modelo, se probaron varios algoritmos de Machine Learning, tales como Gradient Boosting y Random Forest.
        Además, se aplicó búsqueda de hiperparámetros para encontrar la mejor configuración de cada modelo.
    """)

# Sección: Modelo Predictivo
elif selection == "Modelo Predictivo":
    st.header("Modelo Predictivo de Cáncer de Mama")
    st.markdown("Ingrese las características del paciente:")

    # Sliders para ingresar las características del paciente
    val1 = st.slider("Symmetry Mean", min_value=0.1167, max_value=0.3040, value=0.180198, step=0.001)
    val2 = st.slider("Texture SE", min_value=0.3602, max_value=3.5680, value=1.204210, step=0.01)
    val3 = st.slider("Smoothness SE", min_value=0.002667, max_value=0.03113, value=0.007009, step=0.0001)
    val4 = st.slider("Symmetry SE", min_value=0.007882, max_value=0.07895, value=0.020307, step=0.001)
    val5 = st.slider("Symmetry Worst", min_value=0.1565, max_value=0.6638, value=0.287902, step=0.001)
    val6 = st.slider("PC1", min_value=-870.4226, max_value=3858.68, value=-5.197113e-14, step=1.0)

    # Botón para hacer la predicción
    if st.button("Predecir"):
        input_data = np.array([[val1, val2, val3, val4, val5, val6]])
        prediccion = modelo.predict(input_data)
        if prediccion[0] == 0:
            st.success("El modelo predice que el tumor es BENIGNO.")
        else:
            st.error("El modelo predice que el tumor es MALIGNO.")

# Sección: Conclusiones
elif selection == "Conclusiones":
    st.header("Conclusiones")
    st.markdown("""
        Este proyecto demuestra el poder de los modelos de Machine Learning en la predicción temprana del cáncer de mama.
        Los resultados del modelo predictivo muestran una alta precisión, ayudando a los profesionales médicos en la toma de decisiones.
        Sin embargo, siempre es importante recalcar que estos modelos deben ser complementados con evaluaciones clínicas tradicionales.
    """)
