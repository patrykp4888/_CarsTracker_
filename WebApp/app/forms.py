from wtforms import Form, StringField, PasswordField, EmailField, validators


class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=100), validators.DataRequired()])
    email = EmailField('Email', [validators.Length(min=6, max=120), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm_password', message='Password must match!')])
    confirm_password = PasswordField('Repeat password')