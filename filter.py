import pandas as pd
import sys




def load_data(path: str) -> pd.DataFrame:
    if path.endswith('.xls') or path.endswith('.xlsx'):
        return pd.read_excel(path, header=1)
    elif path.endswith('.csv'):
        return pd.read_csv(path, low_memory=False)
    else:
        raise ValueError("Unsupported file format. Please provide an Excel or CSV file.")
    
def filter(data: pd.DataFrame) -> pd.DataFrame:
    filtro = data[data["Categoría"].str.startswith("Componentes Y Partes", na=False)]
    return filtro


def main():
    if len(sys.argv) < 2:
        print("Usage: python filter.py <path_to_file>")
        sys.exit(1)

    archivo = sys.argv[1]
    df = load_data(archivo)
    df_filtered = filter(df)
    df_filtered.to_csv("filtered_data.csv", index=False)
    print(df_filtered)
    print("-------------------------")
    print("✅filtrado mi rey✅")


if __name__ == "__main__":
    main()