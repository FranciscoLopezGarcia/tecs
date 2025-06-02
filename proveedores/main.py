import sys
import os
from config.config import load_config
from loaders.loader import load_data
from filtros.base_filter import aplicar_filtro

def detectar_proveedor(nombre_archivo: str) -> str:
    if "infoandina" in nombre_archivo.lower():
        return "infoandina"
    elif "air" in nombre_archivo.lower():
        return "air"
    else:
        raise ValueError("No se pudo detectar el proveedor.")

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo>")
        sys.exit(1)

    archivo = sys.argv[1]
    proveedor = detectar_proveedor(archivo)
    config = load_config(proveedor)
    df = load_data(archivo)
    df_filtrado = aplicar_filtro(df, config)

    out_name = f"filtrado_{proveedor}.csv"
    df_filtrado.to_csv(out_name, index=False)
    print(f"✅ Filtrado completado para {proveedor}: {out_name}")

if __name__ == "__main__":
    main()
