from flask import Flask, Blueprint, request, url_for, redirect

Main = Blueprint("main", __name__)

@Main.route("/")
def index(): 
    return render_template("index.html")