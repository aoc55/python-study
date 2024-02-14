from flask import Blueprint

print(f'__name__={__name__}')
# 'main' -> BluePrint 별칭, 추후 url_for 함수에서 사용
# '/' -> url 기본 접두어
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index_pybo():
    return 'Pybo Index'


@bp.route('/hello')
def hello_pybo():
    return 'Hello Pybo!'

