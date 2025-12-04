import re

import pandas as pd

class Identifier:
    def __init__(self):
        self._regex_pattern = re.compile(r'^VAR[a-z]+$')

    def is_identifier(self, word: str) -> bool:
        if self._regex_pattern.match(word):
            return True
        return False
    
    def find_identifiers(self, df_data_test: pd.DataFrame) -> pd.DataFrame:
        data_buffer = []

        for index, row in df_data_test.iterrows():
            line = str(row.iloc[0])
            words = line.split()

            for word in words:
                if self.is_identifier(word):
                    data_buffer.append({
                        "Caso": index,
                        "Token": "IDENTIFICADOR",
                        "Lexema": word
                    })
        
        if data_buffer:
            return pd.DataFrame(data_buffer)
        return pd.DataFrame(columns=["Caso", "Token", "Lexema"])