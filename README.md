# Analizador Léxico para un Diccionario Finito

Este proyecto es una aplicación web construida con Streamlit que actúa como un analizador léxico (scanner). Utiliza un diccionario de palabras predefinido para identificar y clasificar lexemas en un texto de entrada, distinguiendo entre palabras reservadas, identificadores válidos y errores léxicos.

## Cómo Ejecutar el Proyecto

Sigue estos pasos para configurar y ejecutar la aplicación en tu entorno local.

### Prerrequisitos

- Python 3.8 o superior
- pip (administrador de paquetes de Python)

### Instalación

1.  **Clonar el Repositorio (Opcional)**
    Si no tienes el proyecto, clónalo desde el repositorio.

    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd <NOMBRE-DEL-DIRECTORIO>
    ```

2.  **Crear un Entorno Virtual (Recomendado)**
    Es una buena práctica crear un entorno virtual para aislar las dependencias del proyecto.

    ```bash
    # Para Windows
    python -m venv venv
    venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar Dependencias**
    Instala todas las librerías necesarias que se encuentran en el archivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

### Ejecución

Una vez que las dependencias estén instaladas, puedes iniciar la aplicación Streamlit.

1. **Ejecutar la Aplicación**
   En la terminal, desde la raíz del proyecto, ejecuta el siguiente comando:

   ```bash
   streamlit run app.py
   ```

2. **Acceder a la Aplicación**
   Abre tu navegador web y ve a la dirección URL que aparece en la terminal (normalmente `http://localhost:8501`).

3. **Uso**
   - Carga el archivo CSV del diccionario de palabras reservadas en el primer campo.
   - Carga el archivo CSV con los datos de prueba a analizar en el segundo campo.
   - La aplicación procesará los datos automáticamente y mostrará una tabla con los resultados.
   - Puedes descargar los resultados en formato CSV usando el botón "Descargar resultados".

---

## Implementación del Código

El proyecto está estructurado para separar la interfaz de usuario de la lógica de negocio, promoviendo un código más limpio y mantenible.

### Estructura de Archivos

```text
.
├── app.py                  # Interfaz de usuario con Streamlit
├── requirements.txt        # Dependencias del proyecto
├── data/                   # Directorio para datos de entrada (ej. diccionarios)
└── src/
    ├── domain/
    │   └── analyzer.py       # Lógica principal del analizador
    ├── models/
    │   ├── dictionary_model.py # Modelo para palabras reservadas
    │   └── identifier_model.py # Modelo para identificadores
    └── utils/
        └── data_loader.py    # Utilidad para cargar datos
```

### Descripción de Componentes

#### `app.py`

Es el punto de entrada de la aplicación. Se encarga de:

- Renderizar la interfaz gráfica usando la librería **Streamlit**.
- Crear los campos para que el usuario cargue los archivos CSV (diccionario y datos de prueba).
- Orquestar el flujo de datos:
  1. Llama a `DataLoader` para cargar los archivos en DataFrames de Pandas.
  2. Instancia la clase `Analyzer` con los datos cargados.
  3. Ejecuta el análisis llamando al método `run()` del analizador.
  4. Muestra los resultados en una tabla y ofrece un botón para su descarga.

#### `src/utils/data_loader.py`

- **Clase `DataLoader`**: Contiene la lógica para leer un archivo CSV subido desde la interfaz de Streamlit. El método `load_csv_data` convierte el archivo en un DataFrame de **Pandas** para su posterior procesamiento.

#### `src/domain/analyzer.py`

- **Clase `Analyzer`**: Es el núcleo del programa.
  - Recibe en su constructor los DataFrames del diccionario y de los datos de prueba.
  - El método `run()` coordina el análisis léxico en tres pasos:
    1. Utiliza el `Dictionary` para identificar las palabras reservadas.
    2. Utiliza el `Identifier` para encontrar los lexemas que cumplen con la regla de identificadores.
    3. Clasifica cualquier palabra no reconocida en los pasos anteriores como `ERROR_LEXICO`.
  - Finalmente, consolida todos los resultados en un único DataFrame ordenado por número de caso.

#### `src/models/`

Este directorio contiene las clases que modelan las entidades del dominio.

- **`dictionary_model.py`**: La clase `Dictionary` almacena las palabras reservadas y sus tipos de token. Su método `isKeyWork` busca coincidencias en los datos de prueba.
- **`identifier_model.py`**: La clase `Identifier` define el patrón (mediante una expresión regular) para un identificador válido (ej. `^VAR[a-z]+$`). Su método `find_identifiers` busca todos los lexemas que cumplen con dicho patrón.
