from scrapping.scrapper import main_scrapper
from database.article_database import ArticleDatabase
from env import Env
import pymysql.cursors


if __name__ == '__main__':
    env = Env()
    db = ArticleDatabase(env)
    db.create_database()

    connection = pymysql.connect(host=env.HOST_MYSQL, user=env.USER_MYSQL, password=env.PWD_MYSQL, database=env.DB_MYSQL, autocommit=True)
    cursor = connection.cursor()
    db.create_tables(cursor)

    articles = main_scrapper("international")
    ids = db.get_all_ids(cursor)

    for article in articles:
        article.save_article_in_db(cursor, ids)