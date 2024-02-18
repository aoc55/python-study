# Question 관련 View Rendering

from flask import Blueprint, render_template, request, url_for
from pybo.models import Question            # 사용할 Model
from pybo.forms import QuestionForm, AnswerForm
from datetime import datetime
from werkzeug.utils import redirect
from pybo.models import db

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def _list():

    # Paging 구현하기
    page = request.args.get('page', type=int, default=1)            # page from Query Parameter

    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    # question = Question.query.get(question_id)
    question = Question.query.get_or_404(question_id)
    form = AnswerForm()
    return render_template('question/question_detail.html', question=question, form=form)


@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()

    if request.method == 'POST' and form.validate_on_submit():  # Validatoe 수행

        # Validate 수행 이후 이상 없을 경우
        question = Question(
            subject=form.subject.data,
            content=form.content.data,
            create_date=datetime.now()
        )

        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))

    # GET
    # 렌더링 시 Form 객체 함께 전달
    return render_template('question/question_form.html', form=form)






