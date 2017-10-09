#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, request, render_template
import json
from models import *

app = Flask(__name__)

def getdata(key='data'):
    data = request.form.get(key)
    data = json.loads(data)
    return data

@app.route('/', methods=['POST', 'GET'])
def add():

    if request.method == 'POST':
        word = request.form.get('word')
        trans = request.form.get('trans')
        try:
            from_ins = Word.get(Word.word == word)
            from_ins.count += 1
            if from_ins.trans and trans not in from_ins.trans:
                from_ins.trans += ',' + trans
            from_ins.save()
        except Word.DoesNotExist:
            from_ins = Word(word=word, trans=trans, count=1)
            from_ins.save()

    words = Word.select().order_by(Word.count.desc())
    return render_template('main.html', words=words)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
