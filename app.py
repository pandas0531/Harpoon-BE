# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, User
from config import Config
from datetime import date, datetime, timezone, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import hashlib

KST = timezone(timedelta(hours=9))

app = Flask(__name__)
app.config.from_object(Config)

# 데이터베이스 초기화
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def index():
    if session.get('userid'):
        return render_template('blog/home.html', islogin=True)
    else:
        return render_template('blog/home.html')

@app.route('/category', methods=['GET'])
def blog_category():
    if session.get('userid'):
        return render_template('blog/category.html', islogin=True)
    else:
        return render_template('blog/category.html')

@app.route('/question', methods=['GET'])
def blog_question():
    if session.get('userid'):
        return render_template('blog/question.html', islogin=True)
    else:
        return render_template('blog/question.html')

@app.route('/admin', methods=['GET'])
def auth_admin():
    if session.get('userid'):
        return render_template('auth/admin.html', islogin=True)
    else:
        return render_template('auth/admin.html')

@app.route('/mypage', methods=['GET'])
def auth_mypage():
    if session.get('userid'):
        print(session.get('userid'))
        user = User.query.filter_by(userid=session.get('userid')).first()
        return render_template('auth/mypage.html', islogin=True, userid=user.userid, correct_p=user.correct_p, miss_p=user.miss_p, my_score=user.my_score)
    else:
        flash('로그인이 필요합니다.')
        return redirect('auth/login.html')

@app.route('/join', methods=['GET', 'POST'])
def auth_join():
    if request.method == 'GET':
        return render_template('auth/join.html')
    elif request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if (User.query.filter_by(userid=userid).first()):
            flash('ID가 이미 존재 합니다.')
            return redirect('/join')
        if len(password) < 8:
            flash('비밀번호는 8자 이상이어야 합니다.')
            return redirect('/join')
        if password != confirm_password:
            flash('비밀번호와 비밀번호 확인이 일치하지 않습니다.')
            return redirect('/join')
        hashed_password = hashlib.sha512(str(password).encode('utf-8')).hexdigest()
        user = User(id=uuid.uuid4(), userid=userid, password=hashed_password, created_at=datetime.now(KST), updated_at=datetime.now(KST), isadmin=False)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth_login'))
    else:
        return render_template('auth/join.html')

@app.route('/login', methods=['GET', 'POST'])
def auth_login():
    if request.method == 'GET':
        if session.get('userid'):
            flash('이미 로그인 되어 있습니다.')
            return redirect('/')
        return render_template('auth/login.html')
    elif request.method == 'POST':
        if session.get('userid'):
            flash('이미 로그인 되어 있습니다.')
            return redirect('/')
        userid = request.form['userid']
        password = request.form['password']
        user = User.query.filter_by(userid=userid).first()
        if not (user):
            flash('존재하지 않는 ID이거나 비밀번호가 일치하지 않습니다.')
            return redirect('/login')
        if user.password == hashlib.sha512(str(password).encode('utf-8')).hexdigest():
            if user.isadmin:
                session['isadmin'] = True
            session['userid'] = user.userid
            return redirect('/')
        else:
            flash('존재하지 않는 ID이거나 비밀번호가 일치하지 않습니다.')
            return redirect('/login')
    else:
        return render_template('auth/login.html')

if __name__ == '__main__':
    app.run(debug=True)