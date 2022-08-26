from operator import methodcaller
from flask import Flask,render_template,request,redirect
from models import db,TaskModel

app = Flask(__name__, template_folder='templates')



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/submit' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        description = request.form['description']
        email = request.form['email']
        priority = request.form['priority']
        
        task = TaskModel(description=description, email=email, priority=priority)
        db.session.add(task)
        db.session.commit()
        return redirect('/')


@app.route('/')
def RetrieveList():
    tasks = TaskModel.query.all()
    return render_template('datalist.html',tasks = tasks)




@app.route('/clear', methods=['GET','POST'])
def DeleteList():
      
    tasks = TaskModel.query.all()
    for x in tasks:
                 db.session.delete(x)
                 db.session.commit()

              
    return redirect('/')




app.run(host='localhost', port=5000)