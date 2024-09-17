from flask import Flask, render_template

#Create a Flask Instance

app = Flask(__name__)

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

app.run(debug=True)