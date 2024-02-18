from flask import Blueprint, url_for, request, render_template
from datetime import datetime
from werkzeug.utils import redirect

from pybo import db
from pybo.models import Question, Answer
from pybo.forms import AnswerForm

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))   # tuple
def create(question_id):

    form = AnswerForm()

    question = Question.query.get_or_404(question_id)

    if form.validate_on_submit():       # Form 검증
        content = request.form['content']
        answer = Answer(content=content, create_date=datetime.now())
        # Question 쪽에 참조 걸기?
        question.answer_set.append(answer)
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))

    return render_template('question/question_deatil.html', question=question, form=form)
