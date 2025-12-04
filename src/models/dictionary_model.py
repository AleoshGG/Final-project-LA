import pandas as pd

class Dictionary:
    def __init__(self, df: pd.DataFrame):
        self.dictionary = dict(zip(df['Lexema'], df['Tipo_de_Token']))

    def isKeyWork(self, df_data_test: pd.DataFrame) -> pd.DataFrame:
        # Implementación, solo las palabras que estén el diccionario 
        data_buffer = []

        for index, row in df_data_test.iterrows():
            line = str(row.iloc[0])
            words = line.split()

            for word in words:
                token_match = self.dictionary.get(word)

                if token_match:
                    data_buffer.append({
                        "Caso": index,
                        "Token": token_match,
                        "Lexema": word
                    })

        if data_buffer:
            return pd.DataFrame(data_buffer)
        return pd.DataFrame(columns=["Caso", "Token", "Lexema"])
        
