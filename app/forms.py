from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from app.models import Recipe
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import ValidationError, DataRequired, Length

class EditRecipeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    group = StringField('Group', validators=[DataRequired()])
    image = FileField('Recipe Image', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')])
    description = TextAreaField('Description', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    steps = TextAreaField('Steps', validators=[DataRequired()])
    notes = TextAreaField('Notes')
    submit = SubmitField('Save Changes')


    # def __init__(self, original_name, *args, **kwargs):
    #     super(EditRecipeForm, self).__init__(*args, **kwargs)
    #     self.original_name = original_name

    # def validate_name(self, name):
    #     if name.data != self.original_name:
    #         recipe = Recipe.query.filter_by(name=self.name.data).first()
    #         if recipe is not None:
    #             raise ValidationError(_('Please use a different name.'))
