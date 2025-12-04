import pandas as pd
from src.models.identifier_model import Identifier
from src.models.dictionary_model import Dictionary

class Analyzer:
    def __init__(self, df_dictionary: pd.DataFrame, df_data_test: pd.DataFrame):
        self.dictionary: Dictionary = Dictionary(df = df_dictionary)
        self.identifier: Identifier = Identifier()
        self.data_test: pd.DataFrame = df_data_test
        self.results = pd.DataFrame(columns=["Caso","Token", "Lexema"])

    def process_lexical_errors(self, df_valid_tokens: pd.DataFrame) -> pd.DataFrame:
        error_buffer = []
        
        valid_pairs = set()
        if not df_valid_tokens.empty:
            valid_pairs = set(zip(df_valid_tokens['Caso'], df_valid_tokens['Lexema']))

        
        for index, row in self.data_test.iterrows():
            line = str(row.iloc[0])
            words = line.split()

            for word in words:
                if (index, word) not in valid_pairs:
                    error_buffer.append({
                        "Caso": index,
                        "Token": "ERROR_LEXICO",
                        "Lexema": word
                    })

        if error_buffer:
            return pd.DataFrame(error_buffer)
        return pd.DataFrame(columns=["Caso", "Token", "Lexema"])

    def run(self) -> pd.DataFrame:
        # 1. Verificar que si es una palabra reservada
        df_dict_results = self.dictionary.isKeyWork(df_data_test=self.data_test)

        # 2. Verificar que si es un identificador
        df_id_results = self.identifier.find_identifiers(df_data_test=self.data_test)

        # Juntar resultados
        valid_frames = [df_dict_results, df_id_results]
        valid_frames = [f for f in valid_frames if f is not None and not f.empty]
        
        df_valid_total = pd.DataFrame(columns=["Caso", "Token", "Lexema"])
        if valid_frames:
            df_valid_total = pd.concat(valid_frames, ignore_index=True)

        # 3. Descartar a todas como Errores Léxicos
        df_errors = self.process_lexical_errors(df_valid_tokens=df_valid_total)

        
        final_frames = [df_valid_total, df_errors]
        final_frames = [f for f in final_frames if not f.empty]

        if final_frames:
            self.results = pd.concat(final_frames, ignore_index=True)
            self.results = self.results.sort_values(by="Caso")
        
        return self.results
        