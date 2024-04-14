from flask import Blueprint


bp = Blueprint('rutas', __name__)

@bp.route('/enviar')
def enviar():
    pass