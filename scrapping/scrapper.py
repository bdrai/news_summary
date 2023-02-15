import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse
from article import Article

CATEGORIES = ["middle-east", "israel", "international"]


def scrap_list_articles(category, page_number):
    if category not in CATEGORIES:
        raise ValueError("This category does not exist in the website.")
    if page_number == 1:
        url = f"https://www.i24news.tv/en/news/{category}"
    else:
        url = f"https://www.i24news.tv/en/news/{category}?page={page_number}"
    html = None
    while not html:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        html = soup.find("div", id="root").find("div", class_="top-level-container")
    return html.find_all("div", class_="column col-12")


def scrap_article_metadata(article_html):
    article_url = article_html["href"]
    article_subcategory = article_html.find("div", class_="article-category").find("div",
                                                                                   class_="widget-typography-tag").text
    article_title = article_html.find("h3", class_="widget-typography-title size-default").text
    article_date = parse(article_html.find("time")["datetime"])
    article_image = article_html.find("div", class_="lazyImageContainer").find("img")["data-observed-item-id"]
    return article_url, article_subcategory, article_title, article_date, article_image


def scrap_article_content(article_url):
    div = None
    while not div:
        page = requests.get(article_url)
        soup = BeautifulSoup(page.content, "html.parser")
        div = soup.find("div", id="article")
    div = div.find("div", class_="columns")
    subtitle = div.find("p", class_="content-excerpt").text

    paragraphs_html = div.find("div", class_="components").find_all("p", attrs={'data-is': "component-paragraph"})
    paragraphs = "\n".join([p.text for p in paragraphs_html])

    return subtitle, paragraphs


def main_scrapper(category, page_number=1):
    articles = []
    print(f" ############### Page n°{page_number} ###############")
    articles_div = scrap_list_articles(category, page_number)
    for index, article_div in enumerate(articles_div):
        if page_number == 1 and index == 0:
            article_html = article_div.find("div", class_="hide-sm").find("a", class_="article-list-horizontal")
        else:
            article_html = article_div.find("a", class_="article-list-horizontal")
        article_url, article_subcategory, article_title, article_date, article_image = scrap_article_metadata(
            article_html)
        article_subtitle, article_paragraphs = scrap_article_content(article_url)
        article = Article(article_url, category, article_subcategory,
                          article_title, article_subtitle, article_date,
                          article_image, article_paragraphs)
        print(article_url)
        articles.append(article)
    return articles


if __name__ == '__main__':
    main_scrapper("international", 5)
