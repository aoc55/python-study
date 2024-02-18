# View File Rendering 용도
from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

print(f'__name__={__name__}')
# 'main' -> BluePrint 별칭, 추후 url_for 함수에서 사용
# '/' -> url 기본 접두어
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    # redriect : 입력 받은 URL 로 리다이렉트
    # url_for : 역으로 URL 찾는 함수
    # - 입력으로 "블루프린트별칭.등록된함수"
    # - url_for('question._list') -> '/question/list/ URL 반환
    return redirect(url_for('question._list'))


@bp.route('/hello')
def hello_pybo():
    return 'Hello Pybo!'

