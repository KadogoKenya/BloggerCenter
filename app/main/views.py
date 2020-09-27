from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    quotes = get_quotes(quote)
    page = request.args.get('page',1, type = int )
    blogs = Blog.query.order_by(Blog.posted.desc()).paginate(page = page, per_page = 3)
        title = 'Home - Welcome to The best Movie Review Website Online'

    return render_template('index.html', quote = quotes,blogs=blogs)
    # return render_template('index.html', title = title,popular = quotes)