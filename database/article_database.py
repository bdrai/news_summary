import pymysql.cursors
from env import Env


class ArticleDatabase:
    """Class to manage Article database"""

    def __init__(self, env: Env):
        self.env = env

    def create_database(self):
        """Create database with the name configured in .env file"""
        connection = pymysql.connect(host=self.env.HOST_MYSQL, user=self.env.USER_MYSQL, password=self.env.PWD_MYSQL)
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.env.DB_MYSQL};")
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def create_table_article(cursor):
        """Creates table `Article`"""
        query = """
            CREATE TABLE IF NOT EXISTS Article (
                `id` BIGINT NOT NULL PRIMARY KEY,
                `url` VARCHAR(250) NOT NULL,
                `date` DATETIME NOT NULL,
                `category` VARCHAR(50),
                `subcategory` VARCHAR(50),
                `image` VARCHAR(250),
                `title` MEDIUMTEXT, 
                `subtitle` MEDIUMTEXT,
                `paragraphs` LONGTEXT
            );
        """
        cursor.execute(query)

    @staticmethod
    def create_table_article_summary(cursor):
        """Creates table `ArticleSummary`"""
        query = """
            CREATE TABLE IF NOT EXISTS ArticleSummary (
                `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                `article_id` BIGINT,
                `summary` LONGTEXT NOT NULL,
                FOREIGN KEY (article_id) REFERENCES Article(id)
            );
        """
        cursor.execute(query)

    def create_tables(self, cursor):
        """Creates all tables in once"""
        self.create_table_article(cursor)
        self.create_table_article_summary(cursor)

    def initialize_database(self):
        """Initialize the database by creating it and the tables with."""
        self.create_database()
        connection = pymysql.connect(host=self.env.HOST_MYSQL, user=self.env.USER_MYSQL,
                                     password=self.env.PWD_MYSQL, database=self.env.DB_MYSQL)
        cursor = connection.cursor()
        self.create_tables(cursor)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all_ids(cursor):
        query = "SELECT id FROM Article"
        cursor.execute(query)
        ids = cursor.fetchall()
        return [id_[0] for id_ in ids]

