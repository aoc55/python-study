import os
from flask import Flask


# Flask Instance 를 Function 안에서 생성하기
# 'application Factory'
# Any configuration, registration, and other setup the application needs will happen
# inside the function, then the application will be returned.

def create_app(test_config=None):       # application Factory Function
    # Create & Config App

    # The instance folder is located outside the flaskr package and can hold local data that shouldn’t be committed to version control,
    # such as configuration secrets and the database file.
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return "Hello World 2"


    # DB 초기화
    from . import db
    db.init_app(app)

    # Auth BluePrint 등록
    from . import auth
    app.register_blueprint(auth.bp)

    return app

