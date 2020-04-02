from static import constants as cst
from from_pocket import read_export
from from_pocket import table_insert

tag_to_search = "lang " ### Don't forget the space in cases you want : lang fr, lang en, lang ru...

all_articles = read_export.getArticlesFromPocketExport()
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

perform = False ### Perform the insertion or just display extracted entries from input ?
if perform:
    print(">>> Inserting entries in notion db ...")
    table_insert.articles(cst.notion_coll_url, articles_to_insert)