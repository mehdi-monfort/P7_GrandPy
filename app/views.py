from flask import render_template, jsonify, request
from . import app
from .view.main import Main


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
