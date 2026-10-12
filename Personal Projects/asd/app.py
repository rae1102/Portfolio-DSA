from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return f"<h1>Hello World</h1>"


app.run(debug=True)