import requests
from bs4 import BeautifulSoup
import json

class WebCrawler:
    def __init__(self, config):
        self.config = config
        self.sources = config['news_sources']
        self.country = config['country']

    def fetch_articles(self):
        articles = []
        for source in self.sources:
            response = requests.get(source['url'])
            if response.status_code == 200:
                articles.extend(self.parse_articles(response.text, source['parser']))
        return articles

    def parse_articles(self, html_content, parser):
        soup = BeautifulSoup(html_content, parser)
        articles = []
        for item in soup.find_all('article'):
            title = item.find('h1').get_text()
            content = item.find('p').get_text()
            articles.append({'title': title, 'content': content})
        return articles

    def run(self):
        articles = self.fetch_articles()
        for article in articles:
            self.save_article(article)

    def save_article(self, article):
        with open('articles.txt', 'a') as file:
            file.write(f"Title: {article['title']}\n")
            file.write(f"Content: {article['content']}\n\n")

def load_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

if __name__ == "__main__":
    config = load_config('config.json')
    crawler = WebCrawler(config)
    crawler.run()