# 루트 디렉터리
import os

# SQL Alcehmy 관련 설정
BASE_DIR = os.path.dirname(__file__)
# __file__=/Users/gh.k/Study/PyCharmProjects/python-study/framework/pybo/config.py
# BASE_DIR=/Users/gh.k/Study/PyCharmProjects/python-study/framework/pybo

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"      # DEV Only

