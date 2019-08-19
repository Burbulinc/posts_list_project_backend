from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class SendPostForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    text = StringField('text', validators=[DataRequired()])
    submit = SubmitField('Send post')
