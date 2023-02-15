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
        self.id_ = int(url.split('/')[-1].split("-")[0])

    def __str__(self):
        return f"{self.title} ({self.date})"

    def save_summary_in_db(self, cursor):
        pass

    def save_article_in_db(self, cursor, list_ids):
        if self.id_ in list_ids:
            return
        query_insert = """
           INSERT INTO `Article` (
               `id`,
               `url`,
               `date`,
               `category`,
               `subcategory`,
               `image`,
               `title`, 
               `subtitle`,
               `paragraphs`           
           ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query_insert, (self.id_, self.url,
                                      self.date, self.category,
                                      self.subcategory, self.image,
                                      self.title, self.subtitle,
                                      self.paragraphs))
