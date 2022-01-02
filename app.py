from flask import render_template
from flask import Flask

app = Flask(__name__)


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
   return render_template('form.html')
#    # first_name = request.form.get('first_name')
#    # last_name = request.form.get('last_name')
#    # email = request.form.get('email')