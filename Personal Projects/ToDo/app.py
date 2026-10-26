from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your database URI (e.g., SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

# Initialize the extension
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200) , nullable = False)

tasks = []

@app.route("/", methods =["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        tasks.append(task)
        return redirect(url_for("home"))
    else:
        return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:index>", methods = ["GET", "POST"])
def delete(index):
    tasks.pop(index)
    return redirect(url_for("home"))


with app.app_context():
    db.create_all()
if __name__ == "__main__":
    app.run(debug=True)