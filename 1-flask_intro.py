from flask import Flask

app=Flask(__name__)
#app - creating application

@app.route('/')
def index():

	return "This is my Home Page!"

@app.route('/page1')
def page1():

	return "This the Page 1!"

@app.route('/page2')
def page2():

	return "This the Page 2!"


app.run(debug=True)

