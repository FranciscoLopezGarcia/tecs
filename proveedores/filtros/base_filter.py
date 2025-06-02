from loaders.normalizer import normalizar
import pandas as pd

def aplicar_filtro(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    df = df.rename(columns=config["column_mapping"])
    
    if "categoria" in df.columns and config["filters"].get("incluir_categoria_prefix"):
        df = df[df["categoria"].fillna("").str.startswith(tuple(config["filters"]["incluir_categoria_prefix"]))]
    
    if config.get("normalizar_descripcion"):
        df["descripcion_normalizada"] = df["descripcion"].astype(str).apply(normalizar)
    else:
        df["descripcion_normalizada"] = df["descripcion"].astype(str).str.lower()
    
    if config["filters"].get("incluir_keywords"):
        df = df[df["descripcion_normalizada"].apply(lambda x: any(k in x for k in config["filters"]["incluir_keywords"]))]
    
    if config["filters"].get("excluir_keywords"):
        df = df[~df["descripcion_normalizada"].apply(lambda x: any(k in x for k in config["filters"]["excluir_keywords"]))]
    
    df.drop(columns=["descripcion_normalizada"], inplace=True)
    return df
