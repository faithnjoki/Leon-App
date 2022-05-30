from flask import render_template
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import redirect





app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/friends.db'

# This avoids the notifications on terminal
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#initalize database
db = SQLAlchemy(app)

subscribers = []

# create db model
class Friends(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50), nullable=False)
   date_created = db.Column(db.DateTime, default=datetime.utcnow)

# create a function to return a string when we add something
   def __repr__(self):
       return '<Name %r>' % self.id


  # ROUTES
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
      friend_name = request.form['name']
      # Friends is db table
      new_friend = Friends(name=friend_name)
      # push to database
      # a  try block
      try:
         db.session.add(new_friend)
         db.session.commit()
         return redirect('/friends')
      except:
         return 'There was an Error Ading your Friend...'
   else:
      friends = Friends.query.order_by(Friends.date_created)
      
      return render_template ('friends.html',friends = friends)
