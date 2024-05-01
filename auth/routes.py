from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
     return render_template('auth/login.html')
@auth.route('/logout')
def logout():
    return "Logout Page"