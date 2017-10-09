#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def add():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'

    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
