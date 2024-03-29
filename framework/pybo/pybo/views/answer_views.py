from flask import Blueprint, url_for, request, render_template, g, flash
from datetime import datetime
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, Answer
from pybo.forms import AnswerForm
from pybo.views.auth_views import login_required


bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))   # tuple
@login_required
def create(question_id):

    form = AnswerForm()

    question = Question.query.get_or_404(question_id)

    if form.validate_on_submit():       # Form 검증
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now(), user=g.user)
        # Question 쪽에 참조 걸기?
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))

    return render_template('question/question_deatil.html', question=question, form=form)


@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def modify(answer_id):
    answer = Answer.query.get_or_404(answer_id)

    if g.user != answer.user:
        flash('수정 권한 X')
        return redirect(url_for('question_detail', question_id=question_id))

    if request.method == 'POST':
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for("question.detail", question_id=answer.question.id))
    else:
        form = AnswerForm(obj=answer)

    return render_template('answer/answer_form.html', form=form)


@bp.route('/delete/<int:answer_id>')
@login_required
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id
    if g.user != answer.user:
        flash('삭제 권한 X')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))


@bp.route('/vote/<int:answer_id>')
@login_required
def vote(answer_id):
    _answer = Answer.query.get_or_404(answer_id)

    if g.user == _answer.user:
        flash('본인이 작성한 답변 추천 X')
    else:
        _answer.vote.append(g.user)     # 'append'
        db.session.commit()

    return redirect(url_for('question.detail', question_id=_answer.question.id))
