from flaskblog import app
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min=4)])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

