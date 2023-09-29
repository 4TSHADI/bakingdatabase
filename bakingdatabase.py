from app import create_app, db, cli
from app.models import Recipe

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Recipe' : Recipe}


# 'name' : name
#         ,'image' : image
#         ,'group' : group
#         ,'description' : description
#         ,'ingredients' : ingredients
#         ,'steps' : steps
#         ,'notes' : notes}
