import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame:
    ext = os.path.splitext(file_path)[1].lower()
    if ext in [".xls", ".xlsx"]:
        return pd.read_excel(file_path)
    elif ext == ".csv":
        # Intentar leer con latin1 para evitar error de codificación
        return pd.read_csv(file_path, encoding="latin1", low_memory=False)
    else:
        raise ValueError(f"Extensión no soportada: {ext}")
