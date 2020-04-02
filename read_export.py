from bs4 import BeautifulSoup as bs
import os
from from_pocket import constants as cst
from from_pocket.Article import Article

def getArticlesFromPocketExport():
    print(">>> Reading articles from pocket export ...")
    ### read file from exported html (must have exported manually from getpocket.com before)
    file_ = open(cst.path_pocket)
    soup = bs(file_, "html.parser")
    # print(soup)
    ### parse and get title, url and tags
    all_articles = []

    articles = soup.find_all('a')
    for article in articles:
        # print(article)
        link = article['href']
        tags = article['tags'].split(',')
        added_on = article['time_added']
        title = article.get_text()
        # print(link)
        # print(tags)
        # print(added_on)
        # print(title)
        art = Article(link, tags, added_on, title)
        # print(art)
        # print("------------------------")
        all_articles.append(art)

    return all_articles