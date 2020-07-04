from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
  api_key = app.config['NEWS_API_KEY']
  #Getting the news base url
  base_url = app.config['NEWS_API_BASE_URL']

  def get_sources():
    '''
    This function gets json response from the news site
    '''

    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response ['sources']:
            sources_result_list = get_sources_response['sources']
            sources_results = process_results(sources_result_list)

    return sources_results