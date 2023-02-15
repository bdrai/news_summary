
class Article:
    def __init__(self, url, category, subcategory, title, subtitle, date, image, paragraphs):
        self.url = url
        self.category = category
        self.subcategory = subcategory
        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.image = image
        self.paragraphs = paragraphs
        self.id_ = url.split('/')[-1].split("-")[0]

    def get_article(self):
        pass

    def __str__(self):
        return f"{self.title} ({self.date})"

