from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# 질문 Form 객체
class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목 필수')])
    content = TextAreaField('내용', validators=[DataRequired('내용 필수')])


# 답변 Form 객체
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용 필수 입력 항목')])


# 회원가입 Form 객체
class UserCreateForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호',
                              validators=[DataRequired(), EqualTo('password2', '비밀번호 불일치')])
    password2 = PasswordField('비밀번호 확인',
                              validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])


# 로그인 Form 객체
class UserLoginForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

