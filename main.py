from static import constants as cst
from static import variables as var

from bs4 import BeautifulSoup as bs
import os


##### ******** IMPORTANT VARIABLES ********
tag_to_search = "lang " ### Don't forget the space in cases you want to extract tags like : lang fr, lang en, lang ru...
perform = False ### Perform the insertion or just display extracted entries from input ?



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



def insertArticlesIntoNotionTable(table_url, articles):
    ### Access a database using the URL of the database page or the inline block
    art_index = 0
    cv = var.client.get_collection_view(table_url)
    for article in articles:
        art_index += 1
        row = cv.collection.add_row()
        # if art.title != art.link : ### it's better with url as title than nothing
        row.name = article.title
        row.url = article.link
        row.pocket_timestamp = article.added_on ### show that item has been imported from Pocket
        langs = []
        for tag in article.tags:
            lang = tag.split(" ")[1]
            lang = lang.replace("-", " ")
            # subj = subj.capitalize() ### not really important because options should already exist in Notion (or added manually)
            print(article.tags, article.title, article.link)
            print("lang : [ {} ]".format(lang))
            langs.append(lang)
        row.languages = langs
        print("{} / {} done".format(art_index, len(articles)))
        print("---------------------")




if __name__ == "__main__":

    all_articles = getArticlesFromPocketExport()
    articles_to_insert = []
    for article in all_articles:
        insert_this_article = False ### by default : don't insert article (if it's not about tag_to_search)
        # print(article.link)
        # print(article.tags)
        # print(article.added_on)
        # print(article.title)
        for tag in article.tags:
            if (tag_to_search in tag):
                insert_this_article = True
                tags_preserve = next(t for t in article.tags if tag_to_search in t)
                print("—> ", tags_preserve)
                article.tags = [ tags_preserve ]
            else:
                insert_this_article = False
                # break ### comment this line to inspect ALL item's tags and not ONLY THE FIRST ONE
        if insert_this_article:
            articles_to_insert.append(article)
            print(article.tags, article.title, article.link)
            print("--------------------")
            # print(article.tags)

    if perform:
        print(">>> Inserting entries in notion db ...")
        insertArticlesIntoNotionTable(cst.notion_coll_url, articles_to_insert)