from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_blog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=6, max=25)])
    email = StringField('Email', [DataRequired(), Email(), Length(min=6, max=25)])
    password = PasswordField('Password', [DataRequired(), Length(min=6, max=25)])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), Length(min=6, max=25),
                                                          EqualTo('password', message='Password is not match')])
    submit = SubmitField('Register')

    def validate_username(form, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Choose a different one')

    def validate_email(form, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already taken. Choose a different one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Confirm')
    new_password = PasswordField('New Password', [DataRequired(), Length(min=6, max=25)])
    confirm_password = PasswordField('Confirm New Password', [DataRequired(), Length(min=6, max=25),
                                                              EqualTo('password', message='Password is not match')])
