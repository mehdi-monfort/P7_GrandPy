from flask import render_template, jsonify, request
from . import app
from .view.main import Main


@app.route('/')
def home():
    return render_template('pages/index.html')


@app.route("/robot", methods=["POST"])
def robot():
    main = Main()
    response = main.query(request.form["userText"])
    return jsonify(response)
