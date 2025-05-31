import pandas as pd

archivo = "/home/flg/Descargas/infoandina.xls"
df = pd.read_excel(archivo, header=1)

def create_pandas(csv_path: str) -> pd.DataFrame:
    data = pd.read_csv(csv_path, low_memory=False)
    return data

def filter(data: pd.DataFrame) -> pd.DataFrame:
    filtro = data[data["Categoría"].str.startswith("Componentes Y Partes", na=False)]
    return filtro

filtred_df = filter(df)
filtred_df.to_csv("filtred_data.csv", index=False)

print(filtred_df)