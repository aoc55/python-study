from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


# 질문 Form 객체
class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목 필수')])
    content = TextAreaField('내용', validators=[DataRequired('내용 필수')])


# 답변 Form 객체
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용 필수 입력 항목')])
