from datetime import datetime
from hashlib import md5
from app import app, db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100))
    group = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    steps = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text)

    def __repr__(self):
        return '<Recipe {}>'.format(self.name)

    def __init__(self, name, group, description, ingredients, steps, notes=None, image=None):
        self.name = name
        self.image = image
        self.group = group
        self.description = description
        self.ingredients = ingredients
        self.steps = steps
        self.notes = notes

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)