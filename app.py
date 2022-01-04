from flask import render_template
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'

#initalize database
db = SQLAlchemy(app)

# create db model
class Friends(db.Model):
   id = db.Column(db.Integer,primary_key=True)
   name = db.Column(db.String, nullable=False)
   date_created = db.Column(db.DateTime, default=datetime.utcnow)

# create a function to return a string when we add something
   def __repr__(self):
       return '<Name %r>' % self.id


subscribers = []


@app.route('/')
def  index():
   return render_template ('index.html')

@app.route('/about')
def about():
   return render_template ('about.html')


   
@app.route('/subscribe')
def subscribe():
   return render_template('subscribe.html')

@app.route('/form', methods = ['POST'])
def form():
   first_name = request.form.get('first_name')
   last_name = request.form.get('last_name')
   email = request.form.get('email')
   if not first_name or not last_name or not email:
      error_statement = 'All form fields are required,Kindly fill them...'
      return render_template("fail.html", error_statement=error_statement,first_name = first_name,
      last_name=last_name,email=email)

   subscribers.append(f"{first_name}  {last_name} | {email}")

   return render_template('form.html', first_name=first_name, last_name=last_name, email = email, subscribers=subscribers)

@app.route('/friends', methods=['POST','GET'])
def friends():
   if request.method == 'POST':
      return 'You clicked the button'
   else:
      return render_template ('friends.html')
