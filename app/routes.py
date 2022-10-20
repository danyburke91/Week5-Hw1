from app import app

from flask import render_template

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/About')
def About():
    fav_artist = ['Elton John', 'Pink', 'Morat', 'Celine Dion', 'Fonseca']
    return render_template('About.html',fav5 = fav_artist)



    
    
