import pandas as pd
from io import StringIO

class DataLoader:
    """
    Clase para manejar la carga y procesamiento inicial de datos.
    """
    def __init__(self):
        pass
    
    def load_csv_data(self, uploaded_file) -> pd.DataFrame:
        """
        Carga datos desde un archivo CSV subido a través de Streamlit.

        Args:
            uploaded_file: El objeto de archivo subido por st.file_uploader.

        Returns:
            Un DataFrame de pandas si la carga es exitosa, de lo contrario None.
        """
        if uploaded_file is not None:
            try:
                # Para leer el archivo subido, lo decodificamos como UTF-8
                string_data = StringIO(uploaded_file.getvalue().decode("utf-8"))
                dataframe = pd.read_csv(string_data)
                return dataframe
            except Exception as e:
                print(f"Error al cargar el archivo: {e}")
                return None
        return None
