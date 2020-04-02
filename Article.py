class Article:
    link = ""
    tags = []
    added_on = ""
    title = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, link, tags, added_on, title):
        self.link = link
        self.tags = tags
        self.added_on = added_on
        self.title = title