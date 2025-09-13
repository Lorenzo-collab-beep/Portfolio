from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.environ.get("APP_SECRET_KEY")


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about-me/')
def about_me():
    return render_template("aboutme.html")

if __name__ == "__main__":
    app.run(debug=True)