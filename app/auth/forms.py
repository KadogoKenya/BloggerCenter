from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required, Length, Email, EqualTo, ValidationError
from ..models import User


class SignupForm(FlaskForm):

    email = StringField('email',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required(), EqualTo("password")])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField("email", validators=[Email(),Required()])
    password = PasswordField("password", validators=[Required()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")