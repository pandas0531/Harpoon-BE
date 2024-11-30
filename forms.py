from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from models import User, ProblemCategory, ProblemDifficulty
from flask_wtf.file import FileField, FileAllowed

class RegistrationForm(FlaskForm):
    userid = StringField('User ID', validators=[DataRequired(), Length(min=2, max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_userid(self, userid):
        user = User.query.filter_by(userid=userid.data).first()
        if user:
            raise ValidationError('User ID already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    userid = StringField('User ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ProblemUploadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    file = FileField('File', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    difficulty = SelectField('Difficulty', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Upload Problem')

    def __init__(self, *args, **kwargs):
        super(ProblemUploadForm, self).__init__(*args, **kwargs)
        self.category.choices = [(c.id, c.name) for c in ProblemCategory.query.all()]
        self.difficulty.choices = [(d.id, d.name) for d in ProblemDifficulty.query.all()]