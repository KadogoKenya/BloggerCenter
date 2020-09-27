from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

     title = 'Home - Welcome to The best Online blog center'

    return render_template('index.html', title = title)