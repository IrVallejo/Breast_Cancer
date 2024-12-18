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
[data-testid="stSidebar"] .css-1v3fvcr {
    color: white !important; /* Asegura que las opciones sean blancas */
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
    "Portada",
    "Introducción",
    "Dataset",
    "Análisis Exploratorio",
    "Variables Seleccionadas",
    "Algoritmos",
    "Modelo Predictivo",
    "Conclusiones"
], index=0)

# Sección: Portada
if selection == "Portada":
    st.title("Análisis Comparativo de Algoritmos de Machine Learning en la Predicción del Cáncer de Mama")
    st.image("mammograph.jpg", use_container_width=False, width=800, caption="Imagen representativa: Mamografía")
    st.markdown("""
        #### Latam Data Science - Promoción Nro. 5
        #### Predicción de Severidad del Cáncer de Mama
        ##### Autores:
        - **Heber Marin**
        - **Irvin Vallejo**
    """)

# Sección: Introducción
elif selection == "Introducción":
    st.header("Introducción")
    st.markdown("""
        <div style="background-color: #f7f7f9; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h3 style="text-align: center; color: #333;">El cáncer de mama es una enfermedad que se origina en las células del tejido mamario, cuando estas comienzan a crecer de manera anormal y descontrolada. Es uno de los principales problemas de salud pública a nivel mundial, siendo la forma de cáncer más común entre las mujeres.</h3>
            <p style="font-size: 20px; color: #555; text-align: justify;">
                Según la Organización Mundial de la Salud (OMS), el cáncer de mama representa aproximadamente el 25% de todos los casos de cáncer diagnosticados en mujeres. Esto lo convierte en un desafío global que afecta a millones de personas, no solo por su prevalencia, sino también por su impacto físico, emocional y social.
            </p>
            <p style="font-size: 20px; color: #555; text-align: justify;">
                En este contexto, el <strong>machine learning</strong> (aprendizaje automático) se presenta como una herramienta innovadora para abordar este problema. Mediante el uso de algoritmos avanzados, el machine learning permite analizar grandes volúmenes de datos médicos, identificar patrones significativos y realizar predicciones que pueden ser cruciales para la detección temprana y el tratamiento del cáncer de mama. Esto no solo mejora la precisión diagnóstica, sino que también optimiza la toma de decisiones clínicas, transformando significativamente el enfoque médico actual.
            </p>
        </div>
    """, unsafe_allow_html=True)

# Sección: Análisis Exploratorio
elif selection == "Dataset":
    st.header("Dataset")
    st.markdown("""
        El dataset utilizado en este proyecto contiene diversas características extraídas de imágenes mamográficas,
        que permiten identificar patrones relacionados con la presencia o ausencia de cáncer de mama. A continuación,
        se muestra una imagen representativa del análisis del dataset:
    """)
    st.image("dataset_mean.jpg", caption="Análisis descriptivo del dataset", width=1000)

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

# Sección: Variables Seleccionadas
elif selection == "Variables Seleccionadas":
    st.header("Variables Seleccionadas")
    st.markdown("""
        En esta sección, se presentan las variables más relevantes seleccionadas para la predicción del cáncer de mama.
        Estas variables fueron determinadas utilizando técnicas como la importancia de las características por permutación
        y su relación con el objetivo.
    """)

    # Mostrar Features vs Target
    st.subheader("Relación entre las Variables y el Objetivo")
    st.image("Features_Target.png", caption="Relación entre las características seleccionadas y la variable objetivo", width=800)

    # Mostrar Permutation Importance
    st.subheader("Importancia de las Variables (Permutation Importance)")
    st.image("Permutation_importance.png", caption="Importancia de las características mediante Permutation Importance", width=800)

# Sección: Algoritmos
elif selection == "Algoritmos":
    st.header("Algoritmos de Machine Learning")
    st.markdown("""
        <div style="font-size: 20px; color: #333; text-align: justify;">
        En esta sección se explican los algoritmos utilizados en el proyecto para la predicción del cáncer de mama.
        Cada algoritmo tiene sus ventajas y desventajas, y los resultados obtenidos nos permiten seleccionar el mejor modelo.
        
        <p>1. <strong>Árboles de Decisión:</strong> Modelos simples que dividen los datos en ramas basadas en reglas de decisión. Aunque son fáciles de interpretar, pueden sobreajustarse a los datos de entrenamiento.</p>
        
        <p>2. <strong>Random Forest:</strong> Conjunto de múltiples árboles de decisión entrenados en subconjuntos aleatorios. Ofrecen mayor precisión y reducen el riesgo de sobreajuste.</p>
        
        <p>3. <strong>Gradient Boosting:</strong> Modelo avanzado que combina múltiples predictores débiles, mejorando gradualmente el rendimiento. Es ideal para problemas complejos pero requiere mayor potencia computacional.</p>
        
        Estos algoritmos se evaluaron para determinar su precisión, sensibilidad y especificidad en la predicción del cáncer de mama.
        </div>
    """, unsafe_allow_html=True)
    st.image("Modelo_ML.jpg", caption="Resumen de Algoritmos de Machine Learning", width=800)

# Sección: Modelo Predictivo
elif selection == "Modelo Predictivo":
    st.header("Modelo Predictivo de Cáncer de Mama")
    st.markdown("Ingrese las características del paciente:")

    # Sliders para ingresar las características del paciente
    simetria_promedio = st.slider("Simetría Promedio", min_value=0.1167, max_value=0.3040, value=0.180198, step=0.001)
    textura_error_estandar = st.slider("Error Estándar de la Textura", min_value=0.3602, max_value=3.5680, value=1.204210, step=0.01)
    suavidad_error_estandar = st.slider("Error Estándar de la Suavidad", min_value=0.002667, max_value=0.03113, value=0.007009, step=0.0001)
    simetria_error_estandar = st.slider("Error Estándar de la Simetría", min_value=0.007882, max_value=0.07895, value=0.020307, step=0.001)
    simetria_peor = st.slider("Peor Valor de Simetría", min_value=0.1565, max_value=0.6638, value=0.287902, step=0.001)
    componente_principal_1 = st.slider("Primera Componente Principal", min_value=-870.4226, max_value=3858.68, value=-5.197113e-14, step=1.0)

    # Botón para hacer la predicción
    if st.button("Predecir"):
        input_data = np.array([[simetria_promedio, textura_error_estandar, suavidad_error_estandar, 
                                simetria_error_estandar, simetria_peor, componente_principal_1]])
        prediccion = modelo.predict(input_data)
        if prediccion[0] == 0:
            st.success("El modelo predice que el tumor es BENIGNO.")
        else:
            st.error("El modelo predice que el tumor es MALIGNO.")

# Sección: Conclusiones
elif selection == "Conclusiones":
    st.header("Conclusiones")
    st.markdown("""
        <div style="background-color: #f7f7f9; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
            <h3 style="text-align: center; color: #333; font-size: 24px;">Resultados y Análisis de Modelos</h3>
            <p style="font-size: 18px; color: #555; text-align: justify;">
                Tras evaluar tres algoritmos de Machine Learning en la predicción del cáncer de mama (Decision Tree, Random Forest y Gradient Boosting), los resultados destacan lo siguiente:
            </p>
            <ul style="font-size: 18px; color: #555; text-align: justify;">
                <li><strong>Gradient Boosting:</strong> Fue el modelo con el mejor desempeño global:
                    <ul>
                        <li>Accuracy: 94.73%, la más alta entre los modelos.</li>
                        <li>ROC AUC: 0.9484, indicando excelente capacidad de diferenciación entre clases.</li>
                        <li>Recall: 95.23%, sobresaliente en la identificación de casos positivos.</li>
                        <li>F1-Score: 93.02%, reflejando un balance ideal entre precisión y sensibilidad.</li>
                    </ul>
                    Este modelo es especialmente útil en un contexto clínico donde es crucial minimizar falsos negativos, dado el impacto de no detectar un caso positivo.
                </li>
                <li><strong>Random Forest:</strong> También mostró un rendimiento sólido:
                    <ul>
                        <li>Accuracy: 93.85%, cercana a la de Gradient Boosting.</li>
                        <li>ROC AUC: 0.9315, demostrando robustez en la clasificación.</li>
                        <li>Precision: 92.68%, superior al Gradient Boosting en la predicción correcta de positivos.</li>
                    </ul>
                    Si bien su sensibilidad es menor que la de Gradient Boosting, su simplicidad y buen balance lo hacen una alternativa práctica y efectiva.
                </li>
                <li><strong>Decision Tree:</strong> Presentó un desempeño adecuado, pero inferior:
                    <ul>
                        <li>Accuracy: 90.35%, más baja que los otros modelos.</li>
                        <li>ROC AUC: 0.8988, reflejando menor capacidad para diferenciar clases.</li>
                        <li>Precision y Recall: 86.04% y 88.09%, respectivamente, indicando un rendimiento limitado en comparación.</li>
                    </ul>
                    Aunque es el modelo más simple, su menor precisión y sensibilidad podrían ser insuficientes en un contexto crítico como el diagnóstico médico.
                </li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
