from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email

# Contact Form
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    subject = StringField('Subject', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])
    submit = SubmitField('Submit')