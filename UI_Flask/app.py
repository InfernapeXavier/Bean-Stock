from flask import Flask
from flask import render_template
from test import listone

app=Flask(__name__)

# @app.route("/index")
@app.route("/")
def index():
	return render_template('pg1.html', data=listone)
	# return ''.join(str(listone())).strip(' ')
	# return render_template('pg1.html')

@app.route("/pg1.html")
def pg1():
	return render_template('pg1.html')	

@app.route("/company1.html")
def company1():
	return render_template('company1.html')	

@app.route("/company2.html")
def company2():
	return render_template('company2.html')	

@app.route("/company3.html")
def company3():
	return render_template('company3.html')	

if __name__ == '__main__':
	app.run(debug=True)

