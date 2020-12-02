from flask import Flask, render_template, request, flash, url_for, redirect, session
from datetime import date
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'Flask Blog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	email = db.Column(db.String(100))
	content = db.Column(db.String(1000))
	date_posted = db.Column(db.String(100))

	def __init__(self, title, email, content, date_posted):
		self.title = title
		self.email = email
		self.content = content
		self.date_posted = date_posted

@app.route('/home')
@app.route('/')	
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/blogs')
def blogs():
	found_user = users.query.all()
	return render_template('Blogs.html', found_user=found_user)
	#168cm 90kg

@app.route('/post/new', methods=['POST', 'GET'])
def post_new():
	if request.method == 'POST':
		title = request.form['title']
		session['title'] = title
		email = request.form['em']
		session['em'] = email
		message = request.form['msg']
		session['msg'] = message
		now = date.today()
		now = now.strftime("%B %d %Y")
		
		usr = users(title, email, message, now)
		db.session.add(usr)
		db.session.commit()

		return redirect(url_for('home'))
	else:
		return render_template('new_post.html')

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)








