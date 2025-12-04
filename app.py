import streamlit as st
import pandas as pd
from src.utils.data_loader import DataLoader

def main():
    """
    Función principal que construye la interfaz de usuario de la aplicación.
    """
    st.title("Analizador Léxico para un Diccionario Finito")

    st.write(
        "Esta aplicación permite analizar datos cargados desde archivos CSV "
        "para aplicar conceptos de la materia de Lenguajes y Autómatas."
    )

    st.header("Parte 1: Cargar los datos")

    # Inputs para los archivos CSV
    uploaded_file_1 = st.file_uploader(
        "Cargar Data 1 (CSV)",
        type="csv",
        key="file1"
    )
    uploaded_file_2 = st.file_uploader(
        "Cargar Data 2 (CSV)",
        type="csv",
        key="file2"
    )

    # Lógica para cargar y procesar los datos
    if uploaded_file_1 and uploaded_file_2:
        data_loader = DataLoader()

        # Cargar los datos
        data_loader.data1 = data_loader.load_csv_data(uploaded_file_1)
        data_loader.data2 = data_loader.load_csv_data(uploaded_file_2)

        if data_loader.data1 is not None and data_loader.data2 is not None:
            st.success("¡Ambos archivos han sido cargados exitosamente!")
        else:
            st.error("Hubo un error al leer uno o ambos archivos CSV. Por favor, verifica su formato.")

if __name__ == "__main__":
    main()
