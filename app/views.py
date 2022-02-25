from flask import Flask, render_template, jsonify, request

from pprint import pprint
from . import app
from .view.maps import *
from .view.wiki import *
from .view.main import *


@app.route('/')
def home():
    return render_template('pages/index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


@app.route("/robot", methods=["POST"])
def robot():
    main = Main()
    response = main.query(request.form["userText"])
    return jsonify(response)
