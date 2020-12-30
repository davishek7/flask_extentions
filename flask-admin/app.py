from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='b097c9499dba41b4496c9a87361845c9'

db=SQLAlchemy(app)

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(255))

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    content=db.Column(db.Text)

db.create_all()

admin = Admin(app, name='microblog', template_mode='bootstrap4')
# Add administrative views here
admin.add_view(ModelView(Users, db.session))
admin.add_view(ModelView(Post, db.session))

if __name__=='__main__':
    app.run(debug=True)
