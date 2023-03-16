import nltk
import numpy as np
import pandas as pd
import pymysql.cursors
from env import Env
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from summary import ArticleSummary

MODEL_DIR = "Models/t5-small-summarization-fine-tuned/checkpoint-360"
MAX_INPUT_LENGTH = 1024

tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)


def generate_summary(article):
    inputs = ["summarize: " + article]
    inputs = tokenizer(inputs, max_length=MAX_INPUT_LENGTH, truncation=True, return_tensors="pt")
    output = model.generate(**inputs, do_sample=True, min_length=5, max_length=512)
    decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    summary = nltk.sent_tokenize(decoded_output.strip())[0]
    return summary


def main():
    env = Env()
    connection = pymysql.connect(host=env.HOST_MYSQL, user=env.USER_MYSQL, password=env.PWD_MYSQL,
                                 database=env.DB_MYSQL, autocommit=True,
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute("SELECT id, paragraphs from Article;")
    df = pd.DataFrame(cursor.fetchall())

    print("Generating summaries...")
    df["summary"] = df["paragraphs"].apply(lambda article: generate_summary(article))
    print("...summaries were correctly generated.")

    df_summary = df[['id', 'summary']]

    print("Saving summaries into the database...")
    for id_, summary in df_summary.values:
        article_summary = ArticleSummary(id_, summary)
        article_summary.save_in_db(cursor)
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
