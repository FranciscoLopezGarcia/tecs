import json
import os

def load_config(proveedor: str) -> dict:
    ruta = os.path.join(os.path.dirname(__file__), f"{proveedor}.json")
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)
