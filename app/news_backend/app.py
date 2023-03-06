
import json
import pymysql
import requests

from flask import Flask, render_template, jsonify

import sys
sys.path.append('../..')
from env import Env

app = Flask(__name__)


@app.route("/get_categories", methods=["GET"])
def get_categories():
    env = Env()
    connection = pymysql.connect(host=env.HOST_MYSQL, user=env.USER_MYSQL, password=env.PWD_MYSQL, database=env.DB_MYSQL,cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(f"SELECT DISTINCT category FROM Article")
    r = cursor.fetchall()
    return jsonify(r)

@app.route("/get_article_id/<id>", methods=["GET"])
def get_article_by_id(id):
    env = Env()
    connection = pymysql.connect(host=env.HOST_MYSQL, user=env.USER_MYSQL, password=env.PWD_MYSQL, database=env.DB_MYSQL,cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, url, category, image, title, subtitle FROM Article WHERE id={id}")
    r = cursor.fetchall()
    return jsonify(r[0])


@app.route("/get_articles_categories/<category>", methods=["GET"])
def get_articles_by_categories(category):
    env = Env()
    connection = pymysql.connect(host=env.HOST_MYSQL, user=env.USER_MYSQL, password=env.PWD_MYSQL, database=env.DB_MYSQL,cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, url, category, image, title, subtitle FROM Article WHERE category='{category}' ORDER BY date DESC;")
    r = cursor.fetchall()
    return jsonify(r)

@app.route("/get_articles_limit/<limit>", methods=["GET"])
def get_articles_limit(limit):
    env = Env()
    connection = pymysql.connect(host=env.HOST_MYSQL, user=env.USER_MYSQL, password=env.PWD_MYSQL, database=env.DB_MYSQL,cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, url, category, image, title, subtitle FROM Article ORDER BY date DESC LIMIT {limit};")
    r = cursor.fetchall()
    return jsonify(r)


if __name__ == '__main__':
    app.run(debug=True)