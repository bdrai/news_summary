class ArticleSummary:
    def __init__(self, id_, summary):
        self.id_ = id_
        self.summary = summary

    def __str__(self):
        return f"{self.id_} ({self.summary})"

    def save_in_db(self, cursor):
        query_insert = """
           INSERT IGNORE INTO `ArticleSummary` (
               `article_id`,
               `summary`           
           ) VALUES (%s, %s)
        """
        cursor.execute(query_insert, (self.id_, self.summary))
