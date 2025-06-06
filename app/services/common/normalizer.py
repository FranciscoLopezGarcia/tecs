import unicodedata

def normalizar(texto: str) -> str:
    texto = texto.lower()
    texto = unicodedata.normalize("NFKD", texto)
    texto = ''.join(c for c in texto if not unicodedata.combining(c))
    return texto
