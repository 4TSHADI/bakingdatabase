from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app, db
from app.forms import EditRecipeForm
from app.models import Recipe
import os
from config import Config, UPLOAD_FOLDER
from flask import current_app


from werkzeug.utils import secure_filename

# User file upload config
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_UPLOAD_LENGTH"] = 4 * 1024 * \
    1024  # Set max file upload size to be 4 MB


# Database config and import
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///database.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route('/')
@app.route('/index')
def index():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)


@app.route('/groups')
def groups():
    recipes = Recipe.query.all()
    return render_template('groups.html', recipes=recipes)


@app.route('/recipe/<name>')
def recipe(name):
    recipe = Recipe.query.filter_by(name=name).first_or_404()

    return render_template('recipecard.html', recipe=recipe)


@app.route('/new_recipe', methods=['GET', 'POST'])
def new_recipe():
    print("Edit recipe route accessed.")
    form = EditRecipeForm()
    if request.method == 'POST':
        print("Edit recipe route accessed2222.")
        new_recipe = Recipe(
        name=form.name.data,
        image=form.image.data,
        group=form.group.data,
        description=form.description.data,
        ingredients=form.ingredients.data,
        steps=form.steps.data,
        notes=form.notes.data
        )

        try:
            db.session.add(new_recipe)
            db.session.commit()
            flash('Recipe added successfully.')
            return redirect(url_for('recipe', name=new_recipe.name, recipe=new_recipe))
        except Exception as e:
            print("Error:", str(e))
            db.session.rollback()  # Roll back the transaction

    return render_template('new_recipe.html', title='Edit Recipe',
                           form=form)

@app.route('/edit_recipe/<name>', methods=['GET', 'POST'])
def edit_recipe(name):
    recipe = Recipe.query.filter_by(name=name).first_or_404()
    form = EditRecipeForm(obj=recipe)  # Prepopulate the form with recipe data
    if form.validate_on_submit():
        form.populate_obj(recipe)  # Update recipe with form data
        # Handle image upload
        if form.image.data:
            image_file = form.image.data
            image_filename = secure_filename(image_file.filename)
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image_filename)
            image_file.save(image_path)
            recipe.image = f'/static/images/recipe/{image_filename}'  # Update the image path

        db.session.commit()
        print("changes")
        flash(('Your changes have been saved.'))
        return redirect(url_for('recipe', name=recipe.name))  # Redirect to recipe view

    return render_template('edit_recipe.html', title='Edit Recipe', form=form, recipe=recipe)