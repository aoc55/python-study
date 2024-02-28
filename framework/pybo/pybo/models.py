from pybo import db

# ORM Model 정의

# M:N Table
question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True))

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True))


class Question(db.Model):                                       # db.Model 상속
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)       # nullable=True, server_default='1'
    user = db.relationship('User', backref=db.backref('question_set'))

    modify_date = db.Column(db.DateTime(), nullable=True)

    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))


class Answer(db.Model):                                        # db.Model 상속
    id = db.Column(db.Integer, primary_key=True)

    # 외래키
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))

    # db.relationship 통해서 (ex. answer.question.subject) 식으로 참조할 수 있음
    # - backref : 역참조 가능여부 (ex. question.answer_set.content)
    question = db.relationship('Question', backref=db.backref('answer_set'))

    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))

    modify_date = db.Column(db.DateTime(), nullable=True)

    voter = db.relationship('User', secondary=answer_voter, backref='answer_voter_set')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


