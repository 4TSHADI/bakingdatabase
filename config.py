import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
UPLOAD_FOLDER_UNIX = "./app/static/images/recipe"
# Define the upload path with backslashes (for Windows)
UPLOAD_FOLDER_WINDOWS = '.\\app\\static\\images\\recipe'

# Use one of the defined paths based on the operating system
UPLOAD_FOLDER = UPLOAD_FOLDER_WINDOWS if os.name == 'nt' else UPLOAD_FOLDER_UNIX

