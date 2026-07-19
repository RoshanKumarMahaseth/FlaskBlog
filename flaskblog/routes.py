from flask import render_template,redirect,url_for,flash
from flaskblog import app
from flaskblog.forms import RegistrationForm,LoginForm


posts = [
    {
        'author' : 'Roshan',
        'title' : 'Blog 1',
        'content' : 'This is my first blog',
        'date_posted' : '19 july 2026'
    },

    {
        'author' : 'Elon Musk',
        'title' : 'Blog 2',
        'content' : 'This is my Second blog',
        'date_posted' : '20 july 2026'
    }

]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    form  = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account has been created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You are logged in','success')
            return redirect('home')
        else:
            flash(f'Login Failed Please check your Email and Password', 'danger')
    return render_template('login.html',title = 'Login', form=form)



