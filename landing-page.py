from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas_page():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos_page():
    return render_template('dojos.html')

@app.route('/new-users', methods=['POST'])
def create_user():
   print "Recieved Form"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   first_name = request.form['first-name']
   last_name = request.form['last-name']
   phone = request.form['phone']
   email = request.form['email']
   print first_name, " | ", last_name

   return redirect('/')

app.run(port=5001, debug=True)
