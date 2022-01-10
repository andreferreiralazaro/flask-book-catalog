from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User


## Função para verificar se e-mail já existe ##

def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email Already Exists')

###############################################

## Criação de formulário de registro ##

class RegistrationForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired(), Length(3,15, message='between 3 and 15 characters')])
    email = StringField('E-mail', validators=[DataRequired(), Email(), email_exists])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(5),     # mínimo de 5 caracteres
                                         EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

##############################################

## Criação de formulário de login ##

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('Stay logged in')
    submit = SubmitField('Log In')

##############################################