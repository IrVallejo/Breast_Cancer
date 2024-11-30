import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Explorador de Datos CSV")

# Ruta del archivo CSV
file_path = 'data.csv'

# Leer el archivo
df_raw = pd.read_csv(file_path)

# Eliminar columnas sin título
df_raw = df_raw.loc[:, ~df_raw.columns.str.contains('^Unnamed')]

# Mostrar una vista previa
st.subheader("Vista Previa de los Datos")
st.write(df_raw.head())

# Información del DataFrame procesada como tabla
st.subheader("Información del DataFrame")
info_data = {
    "Column": df_raw.columns,
    "Non-Null Count": df_raw.notnull().sum(),
    "Dtype": df_raw.dtypes.astype(str)
}
info_df = pd.DataFrame(info_data)
st.write(info_df)  # Mostrar información como tabla estática

# Estadísticas descriptivas ajustadas
st.subheader("Estadísticas Descriptivas")

# Transponer las estadísticas descriptivas
stats_df = df_raw.describe().T

# Mostrar estadísticas descriptivas ajustadas al ancho de la pantalla
st.write(stats_df.style.set_table_styles([
    {'selector': 'th', 'props': [('font-size', '12px'), ('text-align', 'center')]},
    {'selector': 'td', 'props': [('font-size', '12px'), ('text-align', 'center'), ('padding', '5px')]}
]).set_properties(**{'max-width': '800px', 'overflow': 'hidden'}))
