## AIR ##
import pandas as pd
import sys
import unicodedata

KEYWORDS = [
    # CPU
    "cpu", "procesador", "ryzen", "intel", "i3", "i5", "i7", "i9", "xeon", "athlon", "pentium", "celeron", "apu",
    # Motherboard
    "mother", "placa madre", "motherboard", "mainboard", "mobo",
    # RAM
    "ram", "memoria ddr", "memoria ram", "ddr3", "ddr4", "ddr5", "sodimm",
    # Almacenamiento
    "ssd", "hdd", "disco rigido", "disco duro", "m.2", "nvme", "sata",
    # GPU
    "placa de video", "gpu", "geforce", "radeon", "gtx", "rtx", "vga",
    # Fuente de poder (PSU)
    "fuente atx", "fuente 500w", "fuente 600w", "fuente 650w", "psu", "power supply", "80 plus", "cooler master", "thermaltake",
    # Gabinete
    "gabinete", "case", "torre",
    # Refrigeración
    "cooler", "ventilador", "disipador", "fan", "watercooling", "aio", "heatsink",
    # Otros posibles componentes
    "placa pci", "expansion", "controladora usb"
]

EXCLUDE_KEYWORDS = [
    "servidor", "server", "rack", "r440", "td350", "dl380", "hp proliant",
    "sas", "raid", "controladora raid",
    "adaptador ide", "ide a sata", "adaptador sata",
    "grabadora dvd", "graba dvd", "lector dvd", "optico", "cd", "dvd",
    "bateria apc", "ups", "respaldo de energia",
    "skyhawk", "cctv", "surveillance",
    "fuente 9v", "fuente 12v", "fuente 5v", "fuente externa", "adaptador", "transformador", "tablet", "router",
    "impresora", "scanner", "proyector", "tv", "televisor",
    "cable", "switch", "hub", "extensor", "monitor industrial", "acces point", "access point", "carry", "canal", "webcam", "mouse", "teclado", "parlante", "audifono", "audifonos", "auricular", "auriculares",
    "cargador", "cargadores", "bocina", "parlantes", "audifonos bluetooth", "auriculares bluetooth", "repetidor wifi", "repetidor de señal", "router wifi", "modem", "antena wifi", "cable coaxial", "cable ethernet", "cable hdmi", "cable usb"
]

def normalizar(texto: str) -> str:
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join([c for c in texto if not unicodedata.combining(c)])
    return texto

def load_data(path: str) -> pd.DataFrame:
    if path.endswith('.xls') or path.endswith('.xlsx'):
        return pd.read_excel(path, header=0)
    elif path.endswith('.csv'):
        return pd.read_csv(path, low_memory=False, encoding='latin1')
    else:
        raise ValueError("Formato de archivo no soportado.")

def filtrar(df: pd.DataFrame) -> pd.DataFrame:
    if "Descripcion" not in df.columns:
        raise KeyError("No se encontró la columna 'Descripcion' en el archivo.")

    df["Descripcion_normalizada"] = df["Descripcion"].astype(str).apply(normalizar)

    def contiene_keywords(texto):
        return any(palabra in texto for palabra in KEYWORDS)

    def contiene_exclude(texto):
        return any(palabra in texto for palabra in EXCLUDE_KEYWORDS)

    df_filtrado = df[df["Descripcion_normalizada"].apply(contiene_keywords)]
    df_filtrado = df_filtrado[~df_filtrado["Descripcion_normalizada"].apply(contiene_exclude)].copy()

    df_filtrado.drop(columns=["Descripcion_normalizada"], inplace=True)
    return df_filtrado

def main():
    if len(sys.argv) < 2:
        print("Uso: python filter_proveedor2.py <archivo>")
        sys.exit(1)

    archivo = sys.argv[1]
    df = load_data(archivo)
    df_filtrado = filtrar(df)
    df_filtrado.to_csv("filtered_data_proveedor2.csv", index=False)
    print(df_filtrado)
    print("-------------------------")
    print("✅ Filtrado de Proveedor2 completado ✅")

if __name__ == "__main__":
    main()
