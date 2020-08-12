from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Url_form(FlaskForm):
    url =StringField("url", validators=[DataRequired()])
    submit = SubmitField ("submit")
