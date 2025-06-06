from flask import Blueprint, request, jsonify, send_file, current_app
from app.services.downloaders import DOWNLOADERS
from app.services.common.detectar_proveedor import detectar_proveedor
from app.services.common.config import load_config
from app.services.common.loader import load_data
from app.services.common.base_filter import aplicar_filtro
from app.services.downloaders.air_downloader import get_air


scrap_bp = Blueprint('scrap', __name__)


@scrap_bp.route('/<provider>', methods=['GET'])
def scrap_providers(provider):
    if provider not in DOWNLOADERS.keys(): return jsonify({"error": "Unknown provider"})
    app_dir = current_app.root_path
    #file_dir = app_dir + "/files"
    file_dir = "/tmp"
    config = load_config(provider)
    getter = DOWNLOADERS.get(provider)
    file = getter()
    df = load_data(file_dir + "/" + file)
    df_filtrado = aplicar_filtro(df, config)
    out_name = f"{file_dir}/filtrado_{file}"
    df_filtrado.to_csv(out_name, index=False)
    return send_file(out_name, as_attachment=True)