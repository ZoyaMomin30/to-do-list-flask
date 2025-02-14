from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def current_time_rounded_to_minute():
    now = datetime.utcnow()
    return now.strftime('%Y-%m-%d %H:%M')

# Define the database schema
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(600))
    date_created = db.Column(db.String, default=current_time_rounded_to_minute)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# Create database tables if they don't exist
with app.app_context():
    db.create_all()
    print("Database tables created.")

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        todo = Todo(title = title, content=content)
        db.session.add(todo)
        db.session.commit()
         
    allTodo = Todo.query.all()
    # print(allTodo)
    return render_template('index.html', allTodo=allTodo)

@app.route('/show')
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'This page is for products'


@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method=="POST" :
        title = request.form['title']
        content = request.form['content']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.content= content
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)


@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo) 
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
