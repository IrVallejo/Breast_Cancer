import streamlit as st
import joblib
import numpy as np

# Cargar el archivo .joblib que contiene el diccionario
modelo_cargado = joblib.load("Breast_cancer_model_gbc.joblib")

# Extraer el modelo del diccionario
modelo = modelo_cargado["model"]

# Título de la aplicación
st.title("Predicción de Cáncer de Mama")

# Ingreso de datos de características del paciente
st.header("Ingrese las características del paciente:")

# Agregar sliders para cada característica utilizando val1, val2, etc.
val1 = st.slider(
    "Symmetry Mean", min_value=0.1167, max_value=0.3040, value=0.180198, step=0.001
)
val2 = st.slider(
    "Texture SE", min_value=0.3602, max_value=3.5680, value=1.204210, step=0.01
)
val3 = st.slider(
    "Smoothness SE", min_value=0.002667, max_value=0.03113, value=0.007009, step=0.0001
)
val4 = st.slider(
    "Symmetry SE", min_value=0.007882, max_value=0.07895, value=0.020307, step=0.001
)
val5 = st.slider(
    "Symmetry Worst", min_value=0.1565, max_value=0.6638, value=0.287902, step=0.001
)
val6 = st.slider(
    "PC1", min_value=-870.4226, max_value=3858.68, value=-5.197113e-14, step=1.0
)

# Botón para hacer la predicción
if st.button("Predecir"):
    try:
        # Crear un array con los datos ingresados (y asegurarse de que sea de tipo float)
        input_data = np.array([[val1, val2, val3, val4, val5, val6]], dtype=float)

        # Realizar la predicción con el modelo extraído del diccionario
        prediccion = modelo.predict(input_data)

        # Mostrar el resultado de la predicción
        if prediccion[0] == 0:
            st.success("El modelo predice que el tumor es BENIGNO.")
        else:
            st.error("El modelo predice que el tumor es MALIGNO.")
    except Exception as e:
        st.error(f"Ocurrió un error al realizar la predicción: {e}")
