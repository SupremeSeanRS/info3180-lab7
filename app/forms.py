from flask_wtf import FlaskForm
from wtforms import TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired, DataRequired

class UploadForm(FlaskForm):
    description = TextAreaField('Message', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    