from flask import  Flask
app=Flask(__name__)

@app.route('/')
@app.route('/hi')
def index():
    return '<h1>Hello Flask!</h1>'

@app.route('/greet',defaults={'name':'Programmer'})    #如果用户访问/greet,name使用默认值Programmer
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello %s!</h1>' %name