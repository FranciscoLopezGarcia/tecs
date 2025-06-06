def detectar_proveedor(nombre_archivo: str) -> str:
    if "infoandina" in nombre_archivo.lower():
        return "infoandina"
    elif "air" in nombre_archivo.lower():
        return "air"
    else:
        raise ValueError("No se pudo detectar el proveedor.")
