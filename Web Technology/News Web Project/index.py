from flask import Flask, url_for, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

custom_img = 'http://4827-presscdn.pagely.netdna-cdn.com/wp-content/uploads/2015/06/Apple-News-App-Icon.png'

@app.route('/')
def index():
    # topic = 'interesting'
    # print(topic)
    newsapi = NewsApiClient(api_key='23f5a5b7721544f5bcecfc58c4cb9822')
    top_headlines = newsapi.get_top_headlines(country='in')
    articles_online = top_headlines['articles']
    articles = []
    for art in articles_online:
        title = art['title']
        url = art['url']
        description = art['description']
        img_link = art['urlToImage']
        if img_link == None:
            img_link = custom_img
        articles.append((title, url, description, img_link))
    return render_template("homepage.html", articles=articles)


@app.route('/<topic>/')
def profile(topic):
    # print(topic)
    newsapi = NewsApiClient(api_key='23f5a5b7721544f5bcecfc58c4cb9822')
    top_headlines = newsapi.get_top_headlines(category=topic, country='in')

    if not top_headlines['articles']:
        return render_template("homepage.html", articles=[], error_text="Error")

    articles_online = top_headlines['articles']
    articles = []
    for art in articles_online:
        title = art['title']
        url = art['url']
        description = art['description']
        img_link = art['urlToImage']
        if img_link == None:
            img_link = custom_img
        articles.append((title, url, description, img_link))
    return render_template("homepage.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
