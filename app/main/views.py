from . import main
from flask import render_template


@main.route('/')
def index():
    return render_template('base.html')


@main.route('/login')
def login():
    return render_template('auth/login.html')
