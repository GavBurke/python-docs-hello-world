from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello, from gavinburke.azurewebsites.net</p>"

@app.route("/test")
def test():
    return "<p>Hello from specific /test page!</p>"

@app.route('/<path:anything>')
def show_anything(anything):
    return f'<p>Hello from dynamic {escape(anything)} page</p>'
