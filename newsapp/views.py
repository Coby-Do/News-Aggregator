from unicodedata import category
from django.shortcuts import render
import requests

# Create your views here.
def index(request, category=None):
    # https for paid version/ http for free version
    key = "https://newsapi.org/v2/top-headlines?country=us&apiKey=<INSERT KEY>"
    
    if category:
        key += f'&category={category}'

    r = requests.get(key)

    res = r.json()
    data = res['articles']
    title, description, image, url, source, time = [], [], [], [], [], []
    for i in data:
        title.append(i['title'])
        description.append(i['description'])
        image.append(i['urlToImage'])
        url.append(i['url'])
        source.append(i['source']['name'])
        time.append(i['publishedAt'][0:10])
    
    news = zip(title, description, image, url, source, time)
    return render(request, 'newsapp/index.html', {'news':news})