import requests
from bs4 import BeautifulSoup as bs4

news_supports = [
    'vnexpress.net',
    'tuoitre.vn',
    'thanhnien.vn',
    'www.tienphong.vn'
]

atr_parser = {
    'vnexpress.net': {
        'title': ['h1', 'title_news_detail']
    },
    'tuoitre.vn': {
        'title': ['h1', 'article-title']
    },
    'thanhnien.vn': {
        'title': ['h1', 'details__headline']
    },
    'www.tienphong.vn': {
        'title': ['h1', 'headline cms-title']
    }

}


def get_atr_by_news(news_site):
    return atr_parser[news_site]


class NewsFX:
    def __init__(self, url=None):
        self.url = url
        self.news_site = None
        self.title = ''
        self.html = ''

    def parser(self):
        self._set_html()
        self._set_title(bs4(self.html, 'lxml'))

    @property
    def get_html(self):
        return self.html

    @property
    def get_title(self):
        return self.title

    def _set_html(self):
        url_news = self.url.split('/')[2]
        self.news_site = url_news
        if url_news not in news_supports:
            raise Exception('Not support this url')
        try:
            req = requests.get(self.url)
            self.html = req.text

        except Exception:
            raise Exception('Error request')

    def _set_title(self, soup):
        atr = get_atr_by_news(self.news_site)
        title = soup.find(atr['title'][0], class_=atr['title'][1])
        self.title = title.text
