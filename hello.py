from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
#Create a Flask Instance

app = Flask(__name__)

app.config['SECRET_KEY'] = "my super secret that no one is "
#이 부분은 Flask APP의 보안을 위해 ***비밀키***를 설정하는 부분
#세션 암호화 or CSRF 보호를 위해 사용된다.

class NamerForm(FlaskForm): #Create a Form Class
    name = StringField("What's Your Name", validators=[DataRequired()])
    #name 필드는 텍스트 입력을 받는 필드이다
    #validators는 이 필드가 반드시 채워져야 한다는 유효성 검사를 설정
    submit = SubmitField("Submit")
    #폼을 제출할 떄 사용하는 버튼
    #SubmitField는 Submit이라는 버튼을 생성해준다



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
@app.route('/')
def base():
    first_name = "John"
    stuff = "this is bold text"
    favorite_pizza = ["PPPP", "Cheese", "Potato", 425]
    return render_template("base.html", 
                           first_name = first_name
                           ,stuff = stuff,
                           favorite_pizza = favorite_pizza)

#주소 : localhost:5000/user/name
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




@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm() #Form 객체를 생성, 
    #이 폼은 템플릿에서 사용자에게 이름을 입력받는 역할을 한다
    # Validate Form
    if form.validate_on_submit():# 폼이 제출되었고 유효한지 확인합니다//폼이 입력시 다시 함수가 돌아감
        name = form.name.data #폼이 제출되면 name 이라는 변수에 form.name.data 값이 들어감
        form.name.data = '' #그리고 다시 nULL로 초기화 시킴
        
    return render_template("name.html",
                           name = name,
                           form = form)
app.run(debug=True)