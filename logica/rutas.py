from flask import Blueprint, request, jsonify
from lexico.lexer import analisis

bp = Blueprint('rutas', __name__)

@bp.route('/lexico', methods=['POST'])
def lexico():
    codigo_fuente = request.json.get('codigo_fuente','')
    tokens = analisis(codigo_fuente)
    print(tokens)
    return jsonify({'tokens': tokens})