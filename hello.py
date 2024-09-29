from flask import Flask, render_template, flash, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Create a Flask Instance

app = Flask(__name__)

#Add DataBase__SQLite 루트 Dir에 users테이블 생성
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/our_users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
#이 부분은 Flask APP의 보안을 위해 ***비밀키***를 설정하는 부분
#세션 암호화 or CSRF 보호를 위해 사용된다.
app.config['SECRET_KEY'] = "my super secret that no one is "

class NamerForm(FlaskForm): #이건 입력, 전달에 관한 format을 제공해준다!
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")
    #폼을 제출할 떄 사용하는 버튼
    #SubmitField는 Submit이라는 버튼을 생성해준다
class UserForm(FlaskForm): #이건 입력, 전달에 관한 format을 제공해준다!
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    #name 필드는 텍스트 입력을 받는 필드이다
    #validators는 이 필드가 반드시 채워져야 한다는 유효성 검사를 설정
    submit = SubmitField("Submit")
    #폼을 제출할 떄 사용하는 버튼
    #SubmitField는 Submit이라는 버튼을 생성해준다

# Initialize The Database
db = SQLAlchemy(app)
# Create User에 관한 Table 설정하기
class Users(db.Model): #db.Model을 상속 받아 User Class 생성
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), nullable = False, unique = True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    #Create A  String
    def __repr__(self):
        return f'<User {self.username}>'
    
#테이블과 db를 Flask App에 생성한다!
with app.app_context():
    db.create_all()    

#이제 해당 웹에서 DB를 이용하는 방법을 지정한다
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm() #wtfForm을 통해 쉽게 만들 수 있는 입력,저장 format을 이용
    if form.validate_on_submit():# 폼이 제출되었고 유효한지 확인합니다//폼이 입력시 다시 함수가 돌아감
        user = Users.query.filter_by(email=form.email.data).first() 
        #입력된 이메일의 값은 unique = True를 통해 중복이 안됨
        #그럼 .first()를 사용한다는 것은 해당 이메일이 테이블에 존재하느냐를 따지는 명령문이 됨
        if user is None :
            user = Users(name = form.name.data, email = form.email.data)
            #Users라는 테이블의 이름과 이메일에 입력된 값을 넣어준다.
            db.session.add(user) #db 세션에 user를 저장
            db.session.commit() #commit을 통해 완전히 넣는다
        name = form.name.data #로컬 변수 name에 전달된 값을 저장
        form.name.data = '' #초기화
        form.email.data = '' #초기화
    our_users = Users.query.order_by(Users.date_added)
    #저장된 순서로 Users 테이블 LIST를 our_users에 저장
    return render_template("add_user.html",
                           form = form,
                           name = name,
                           our_users = our_users)

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm() #Form 객체를 생성, 
    #이 폼은 템플릿에서 사용자에게 이름을 입력받는 역할을 한다
    # Validate Form
    if form.validate_on_submit():# 폼이 제출되었고 유효한지 확인합니다//폼이 입력시 다시 함수가 돌아감
        name = form.name.data #폼이 제출되면 name 이라는 변수에 form.name.data 값이 들어감
        form.name.data = '' #그리고 다시 nULL로 초기화 시킴
    else:
        print("오류 발생")
    return render_template("name.html",
                           name = name,
                           form = form)
    
@app.route('/update/<int:id>',methods=["POST", "GET"])
def update(id):
    name = None
    our_users = Users.query.order_by(Users.date_added)
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        try:
            db.session.commit()
            flash("User Updated Successfully!")
            return render_template("add_user.html",
                                   form = form,
                                   name = name,
                                   our_users = our_users)
        except:
            flash("ERROR!")
            return render_template("update.html",
                                   form = form,
                                   name_to_update = name_to_update)
    else:
        return render_template("update.html",
                                   form = form,
                                   name_to_update = name_to_update)


# Create a route decorator__URL~~~.HTML
# render_template 를 통해서 html파일 불러오기

#Filters!!!
#{{value|--something--}}
#safe  : 
#capitalize
#lower
#upper
#title
#trim
#striptags
@app.route('/user/<name>/')
def user(name):
    return render_template("user.html", user_name = name)

#Create Custom Error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500




app.run(debug=True)

