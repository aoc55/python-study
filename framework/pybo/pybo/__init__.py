from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

# DB 설정

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))       # 다른 모듈에서 사용 가능하게 전역변수
migrate = Migrate()     # 다른 모듈에서 사용 가능하게 전역변수

# Application Factory => 'create_app()'
# - create_app -> 내부에서 정의된 함수명임 (변경X)
def create_app():

    # app 객체가 이제 전역이 아닌 create_app Method 내 Scope 로 한정됨
    app = Flask(__name__)

    # app 내 Config 설정
    app.config.from_object(config)  # config 별도 파일에서 가져옴

    # ORM 설정 및 초기화
    # (Flask 사용 자주하는 패턴)
    # - (1) 전역변수 설정
    # - (2) 팩토리 같은 내부 메서드에서 초기화
    db.init_app(app)            # 전역변수 초기화
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    # model 설정
    from . import models

    # BluePrint 등록
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # Filter 설정
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app
