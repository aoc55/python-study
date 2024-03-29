# Question 관련 View Rendering

from flask import Blueprint, render_template, request, url_for, g, flash
from pybo.models import Question            # 사용할 Model
from pybo.forms import QuestionForm, AnswerForm
from datetime import datetime
from werkzeug.utils import redirect
from pybo.models import db
from pybo.views.auth_views import login_required

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
@login_required
def create():
    form = QuestionForm()

    if request.method == 'POST' and form.validate_on_submit():  # Validatoe 수행

        # Validate 수행 이후 이상 없을 경우
        question = Question(
            subject=form.subject.data,
            content=form.content.data,
            create_date=datetime.now(),
            user=g.user
        )

        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))

    # GET
    # 렌더링 시 Form 객체 함께 전달
    return render_template('question/question_form.html', form=form)


@bp.route('/modify/<int:question_id>', methods=('GET', 'POST'))
@login_required
def modify(question_id):
    question = Question.query.get_or_404(question_id)

    if g.user != question.user:
        flash('수정 권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id))

    if request.method == 'POST':
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(question)
            question.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('question_detail', question_id=question_id))
    else:
        form = QuestionForm(obj=question)

    return render_template('question/question_form.html', form=form)


@bp.route('/delete/<int:question_id>')
@login_required
def delete(question_id):
    question = Question.query.get_or_404(question_id)

    if g.user != question.user:
        flash("삭제 권한 X")
        return redirect(url_for('question.detail', question_id=question_id))

    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('question._list'))


# 추천기능
@bp.route('/vote/<int:question_id>/')
@login_required
def vote(question_id):
    _question = Question.query.get_or_404(question_id)

    if g.user == _question.user:
        flash('본인이 작성한 글 추천할 수 X')

    else:
        _question.voter.append(g.user)      # 'append'
        db.session.commit()

    return redirect(url_for('question.detail', question_id=question_id))

