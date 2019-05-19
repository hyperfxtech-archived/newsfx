import requests
from bs4 import BeautifulSoup as bs4
from PIL import Image
from io import BytesIO


news_supports = [
    'vnexpress.net',
    'tuoitre.vn',
    'thanhnien.vn',
    'www.tienphong.vn'
]

atr_parser = {
    'vnexpress.net': {
        'title': ['h1', 'title_news_detail'],
        'public_date' :['span','time left'],
        'summary' : ['p','description'],
        'body': ['p','Normal'],
        'author' :['strong',''],
        'top-image':['meta','og:image']
    },
    'tuoitre.vn': {
        'title': ['h1', 'article-title'],
        'public_date' :['div','date-time'],
        'summary' : ['h2','sapo'],
        'body': ['p',''],
        'author' :['div','author'],
        'top-image':['meta','og:image']
    },
    'thanhnien.vn': {
        'title': ['h1', 'details__headline'],
        'public_date' :['time',''],
        'summary' : ['div','sapo'],
        'body': ['p',''],
        'author' :['div','details__author__meta'],
        'top-image':['meta','og:image']
    },
    'www.tienphong.vn': {
        'title': ['h1', 'headline cms-title'],
        'top-image':['meta','og:image']
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
        self.public_date = ''
        self.summary = ''
        self.body = ''
        self.author = ''
        self.image = ''

    def parser(self):
        self._set_html()
        self._set_title(bs4(self.html, 'lxml'))
        self._set_public_date(bs4(self.html, 'lxml'))
        self._set_summary(bs4(self.html, 'lxml'))
        self._set_body(bs4(self.html,'lxml'))
        self._set_author(bs4(self.html,'lxml'))
        self._set_top_image_link(bs4(self.html,'lxml'))


    @property
    def get_html(self):
        return self.html

    @property
    def get_title(self):
        return self.title

    @property
    def get_public_date(self):
        return self.public_date

    @property
    def get_summary(self):
        return self.summary

    @property
    def get_content(self): 
        return self.body
    
    @property
    def get_summary(self):
        return self.summary

    @property
    def get_author(self):
        return self.author

    @property
    def get_top_image_link(self):
        return self.image

    def save_top_image_link(self,name):
        response = requests.get(self.image)
        img = Image.open(BytesIO(response.content))
        img.save(name)

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

    def _set_body(self, soup):
        atr = get_atr_by_news(self.news_site)
        body = soup.findAll(atr['body'][0],class_=atr['body'][1])
        for contend in body[:] :
            self.body += ""+contend.text

    def _set_title(self, soup):
        atr = get_atr_by_news(self.news_site)
        _title = soup.find(atr['title'][0], class_=atr['title'][1])
        
        self.title = _title.text

    def _set_public_date(self,soup):
        atr = get_atr_by_news(self.news_site)
        public = soup.find(atr['public_date'][0], class_=atr['public_date'][1])
        self.public_date = public.text
    
    def _set_summary(self,soup):
        atr = get_atr_by_news(self.news_site)
        summ = soup.find(atr['summary'][0], class_=atr['summary'][1])
        self.summary = summ.text
    
    def _set_author(self,soup):
        atr = get_atr_by_news(self.news_site)
        author = soup.find(atr['author'][0], class_=atr['author'][1])

        self.author = author.text.strip()

    def _set_top_image_link(self,soup):
        atr = get_atr_by_news(self.news_site)
        image = soup.find(atr['top-image'][0], property=atr['top-image'][1])
        self.image = image['content']
