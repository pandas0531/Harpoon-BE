from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, User, Problem, ProblemCategory, ProblemDifficulty
from config import Config
from datetime import datetime, timezone, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, ProblemUploadForm
import uuid
import hashlib
import os
from werkzeug.utils import secure_filename

KST = timezone(timedelta(hours=9))
app = Flask(__name__)
app.config.from_object(Config)

# 데이터베이스 초기화
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/join', methods=['GET', 'POST'])
def auth_join():
    if 'userid' in session:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        userid = form.userid.data
        password = generate_password_hash(form.password.data)
        new_user = User(userid=userid, password=password, isadmin=True)
        db.session.add(new_user)
        db.session.commit()
        flash('회원가입이 완료되었습니다!')
        return redirect(url_for('auth_login'))
    return render_template('auth/join.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def auth_login():
    if 'userid' in session:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(userid=form.userid.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['userid'] = user.userid
            return redirect(url_for('index'))
        else:
            flash('로그인 실패. 아이디나 비밀번호를 확인하세요.')
    return render_template('auth/login.html', form=form)

@app.route('/admin', methods=['GET', 'POST'])
# 문제 제목 중복 처리 해야함
def auth_admin():
    if 'userid' not in session:
        flash('로그인이 필요합니다.')
        return redirect(url_for('auth_login'))
    
    user = User.query.filter_by(userid=session.get('userid')).first()
    if not user.isadmin:
        flash('관리자만 접근 가능합니다.')
        return redirect(url_for('index'))
    
    form = ProblemUploadForm()
    form.category.choices = [(1, '사칙연산'), (2, '중등 수학'), (3, '수(상)'),(4, '수(하)'),(5, '수1'),(6, '수2'),(7, '미분'),(8, '적분'),(9, '모고 3점'),(10, '모고 4점'),(11, '킬러')]
    form.difficulty.choices = [(1, '기본'), (2, '실력')]
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        file = form.file.data
        category_id = form.category.data
        difficulty_id = form.difficulty.data

        existing_problem = Problem.query.filter_by(title=title).first()
        if existing_problem:
            flash('문제 제목이 이미 존재합니다.')
            return redirect(url_for('auth_admin'))
        

        folder_path = os.path.join(app.config['UPLOAD_FOLDER'], '1',secure_filename(title))
        os.makedirs(folder_path, exist_ok=True)
        
        filename = None
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(folder_path, filename))
        
        new_problem = Problem(
            title=title,
            description=description,
            file=filename,
            category_id=category_id, # 카테고리 순서대로
            difficulty_id=difficulty_id # 1이 기본, 2가 실력.
        )
        db.session.add(new_problem)
        db.session.commit()
        flash('문제가 성공적으로 업로드되었습니다!')
        return redirect(url_for('auth_admin'))
    
    return render_template('auth/admin.html', form=form, islogin=True)

@app.route('/mypage', methods=['GET'])
def auth_mypage():
    if 'userid' not in session:
        flash('로그인이 필요합니다.')
        return redirect(url_for('auth_login'))
    
    user = User.query.filter_by(userid=session.get('userid')).first()
    correct_problems = user.correct_p
    incorrect_problems = user.miss_p
    
    return render_template(
        'auth/mypage.html', 
        islogin=True, 
        userid=user.userid, 
        correct_problems=correct_problems, 
        incorrect_problems=incorrect_problems, 
        my_score=user.my_score
    )

@app.route('/category/<category_name>', methods=['GET'])
def blog_category(category_name):
    return render_template(f'blog/question{category_name}.html')

@app.route('/', methods=['GET'])
def index():
    is_admin = False
    if 'userid' in session:
        user = User.query.filter_by(userid=session.get('userid')).first()
        is_admin = user.isadmin
        return render_template('blog/home.html', islogin=True, is_admin=is_admin)
    else:
        return render_template('blog/home.html', islogin=False, is_admin=is_admin)


if __name__ == '__main__':
    app.run(debug=True)