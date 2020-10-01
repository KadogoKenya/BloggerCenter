from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class BlogpostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    content = TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField("Give your thoughts")
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')