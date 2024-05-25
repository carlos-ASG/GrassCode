from flask import Blueprint, request, jsonify
from lexico.lexer import analisis
from lexico.sintactico import prueba_sintactica

bp = Blueprint('rutas', __name__)

@bp.route('/lexico', methods=['POST'])
def lexico():
    codigo_fuente = request.json.get('codigo_fuente','')
    #print(codigo_fuente)
    tokens = analisis(codigo_fuente['codigo_fuente'])
    sintactico = prueba_sintactica(codigo_fuente['codigo_fuente'])
    return jsonify({
        'tokens': tokens,
        'sintactico': sintactico,
        })


