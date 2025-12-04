import streamlit as st
from src.utils.data_loader import DataLoader
from src.domain.analyzer import Analyzer

def main():
    """
    Función principal que construye la interfaz de usuario de la aplicación.
    """
    st.title("Analizador Léxico para un Diccionario Finito")

    st.write(
        "Programa que funciona como la primera fase de un compilador (Analizador"
        "Léxico o Scanner), utilizando un conjunto predefinido de palabras válidas"
        "para identificar y clasificar los tokens válidos en un texto de entrada."
    )

    st.header("Cargar los datos")

    # Inputs para los archivos CSV
    data_dictionary = st.file_uploader(
        "Diccionario (CSV)",
        type="csv",
        key="file1"
    )
    data_test = st.file_uploader(
        "Datos de prueba (CSV)",
        type="csv",
        key="file2"
    )

    # Lógica para cargar y procesar los datos
    if data_dictionary and data_test:
        data_loader = DataLoader()

        # Cargar los datos
        df_dictionary = data_loader.load_csv_data(data_dictionary)
        df_data_test  = data_loader.load_csv_data(data_test)

        if df_dictionary is not None and df_data_test is not None:
            st.success("¡Ambos archivos han sido cargados exitosamente!")
            
            # Instancia de la lógica del programa:
            analizer = Analyzer(df_dictionary=df_dictionary, df_data_test=df_data_test)

            st.divider()
            st.subheader("Resultados del Análisis")

            try:
                df_results = analizer.run()

                st.dataframe(df_results, use_container_width=True, hide_index=True)
                
                csv = df_results.to_csv(index=False).encode('utf-8')

                st.download_button(
                    label="Descargar resultados (CSV)",
                    data=csv,
                    file_name='resultados_lexicos.csv',
                    mime='text/csv',
                )

            except Exception as e:    
                st.error(f"Ocurrió un error durante el análisis: {e}")
                
                # Imprimir el traceback completo en la vista expandible si es un error complejo
                with st.expander("Ver detalles técnicos del error"):
                    st.exception(e)
        else:
            st.error("Hubo un error al leer uno o ambos archivos CSV. Por favor, verifica su formato.")

if __name__ == "__main__":
    main()
