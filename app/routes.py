from app import app

from flask import render_template

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/About')
def About():
    return render_template('About.html')
    
