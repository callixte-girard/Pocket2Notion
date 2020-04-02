from static import variables as var

def articles(table_url, articles):
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
