from flask import Blueprint

bp = Blueprint('hello', __name__)
@bp.route('/')
def hello_world():
    return 'Hello! world'