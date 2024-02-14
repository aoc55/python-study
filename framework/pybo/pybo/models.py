from pybo import db


# ORM Model 정의
class Question(db.Model):                                       # db.Model 상속
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):                                        # db.Model 상속
    id = db.Column(db.Integer, primary_key=True)

    # 외래키
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))

    # db.relationship 통해서 (ex. answer.question.subject) 식으로 참조할 수 있음
    # - backref : 역참조 가능여부 (ex. question.answer_set.content)
    question = db.relationship('Question', backref=db.backref('answer_set'))

    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)



