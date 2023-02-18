from scrapping.scrapper import main_scrapper, CATEGORIES
from database.article_database import ArticleDatabase
from env import Env
import pymysql.cursors


if __name__ == '__main__':
    env = Env()
    db = ArticleDatabase(env)
    db.create_database()

    connection = pymysql.connect(host=env.HOST_MYSQL, user=env.USER_MYSQL, password=env.PWD_MYSQL,
                                 database=env.DB_MYSQL, autocommit=True)
    cursor = connection.cursor()
    db.create_tables(cursor)
    N_PAGES = 10
    for category in CATEGORIES:
        ids = db.get_all_ids(cursor)
        for page_number in range(1, N_PAGES + 1):
            articles = main_scrapper(category, page_number)
            for article in articles:
                article.save_article_in_db(cursor, ids)
    cursor.close()
    connection.close()
