from . import auth
from flask import render_template

@auth.route('/')
def login():
    return render_template('auth/auth.html')