from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from main.models import URL


class Url_form(FlaskForm):
    url =StringField("Enter url here", validators=[DataRequired()])
    submit = SubmitField ("Shorten")

    def validate_url(self, url):
        link = URL.query.filter_by(new_link=url.data).first()
        if link:
            raise ValidationError("Please try another word")


class Customise(FlaskForm):
    url = StringField("Old Url", validators=[DataRequired()])
    custom =  StringField("customise", validators=[DataRequired()])
    submit = SubmitField ("Shorten")

    def validate_custom(self, custom):
        link = URL.query.filter_by(new_link=custom.data).first()
        if link:
            raise ValidationError("Sorry this link is already taken please try another one")
