from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='a9037c898f658e8d4b72d540d8490d82'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



@app.route("/")
@app.route("/home")
def home():
	print(len(posts))
	return render_template('home.html',posts=posts)


@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register",methods=['GET','POST'])
def register():
	form = RegistrationForm()

	if form.validate_on_submit():
		flash(f'Account Created for {form.username.data}!','success')
		return redirect(url_for('home'))
		

	return render_template('register.html',title='Register',form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html',title='Login',form=form)


if __name__ == '__main__':
    app.run(debug=True)