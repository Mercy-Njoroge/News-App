from flask import render_template
from app import app
from .request import get_sources
from .requests import get_articles,get_article

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_sources = get_sources('popular')
    print(popular_sources)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, popular = popular_sources)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    article = get_article(id)
    title = f'{article.title}'

    return render_template('news.html', title = title, id = news_id)

