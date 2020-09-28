from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class SignupForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(),Length(min=3,max=21)])
    email = StringField("email", validators=[Email(),DataRequired()])
    password = PasswordField("password" ,validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password",validators=[DataRequired(),EqualTo("password")])
    submit = SubmitField("Sign Up")



class LoginForm(FlaskForm):
    email = StringField("email", validators=[Email(),DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")