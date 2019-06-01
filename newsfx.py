import requests
from bs4 import BeautifulSoup as bs4
from PIL import Image
from io import BytesIO
import re


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
        'top-image':['meta','og:image'],
        'list-images':['img','']
    },
    'tuoitre.vn': {
        'title': ['h1', 'article-title'],
        'public_date' :['div','date-time'],
        'summary' : ['h2','sapo'],
        'body': ['p',''],
        'author' :['div','author'],
        'top-image':['meta','og:image'],
        'list-images':['img','']
    },
    'thanhnien.vn': {
        'title': ['h1', 'details__headline'],
        'public_date' :['time',''],
        'summary' : ['div','sapo'],
        'body': ['div','cms-body'],
        'author' :['div','details__author__meta'],
        'top-image':['meta','og:image'],
        'list-images':['img','']
    },
    'www.tienphong.vn': {
        'title': ['h1', 'headline cms-title'],
        'top-image':['meta','og:image']
    }

}

Special_characters = [
        ',','.','/','<','>','?',';',':','\'','"','[','{',']','}'
        ,'`','~','!','@','#','$','%','^','&','*','(',')','-',
        '_','+','=','\n'
]

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
        self.list_images = list()

    def parser(self):
        self._set_html()
        self.soup = bs4(self.html, 'lxml')
        self._set_title(self.soup)
        self._set_public_date(self.soup)
        self._set_summary(self.soup)
        self._set_body(self.soup)
        self._set_author(self.soup)
        self._set_top_image_link(self.soup)
        self._set_list_image_link(self.soup)


    @property
    def get_html(self):
        return self.html

    @property
    def get_title(self):
        return re.sub(r"\W"," ",self.title, flags = re.I)  

    @property
    def get_public_date(self):
        return self.public_date

    @property
    def get_summary(self):
        return re.sub(r"\W"," ",self.summary, flags = re.I)  

    @property
    def get_content(self):
        return re.sub(r"\W"," ",self.body, flags = re.I)  

    @property
    def get_author(self):
        return self.author

    @property
    def get_top_image_link(self):
        return self.image

    @property
    def get_list_image(self):
        return self.list_images

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
        contents = ''
        for content in body :
            contents = contents + content.text
        self.body = contents 

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
    
    def _set_list_image_link(self,soup):
        atr = get_atr_by_news(self.news_site)
        images = soup.findAll(atr['list-images'][0], class_=atr['list-images'][1])
        print(images)
        for img in images:
            self.list_images.append(img['src'])

