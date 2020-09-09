import urllib3
import bs4
from CONST import HEADERS, KYM
from MemePage import MemePage
from PhotoPage import PhotoPage
from NewsPage import NewsPage

def url_maker(context, page_index, query, sort):
    return KYM+'/search?context=' + context + '&page=' + str(page_index) + '&q=' + query + '&sort=' + sort

class SearchEntry():
    def __init__(self, query, max_pages = 1, sort = 'relevance'):
        self.max_pages = max_pages
        self.query = query
        self.sort = sort

    def search(self):
        # Scrap this tag <table class="entry_list">
        # To return 2D list of MemePage objects
        # MemePageList[search_page_index][MemePage_index_in_search_page]

        http = urllib3.PoolManager()

        MemePageList = []

        for page_index in range(1, self.max_pages+1):
            url = url_maker('entries', page_index, self.query, self.sort)
            response = http.request('GET', url, headers=HEADERS)
            soup = bs4.BeautifulSoup(response.data, 'html.parser')

            if 'Sorry' in soup.find('div', attrs={'class': 'entries'}).find('h3').text:
                break

            tag_a_list = soup.find('table', attrs={'class':'entry_list'}).find_all('a', attrs={'class':'photo'})
            url_list = [KYM+tag_a['href'] for tag_a in tag_a_list]
            MemePageList.append([MemePage(u_r_l) for u_r_l in url_list])

        self.MemePageList = MemePageList


class SearchImage():
    def __init__(self, query, max_pages = 1, sort = 'relevance'):
        self.max_pages = max_pages
        self.query = query
        self.sort = sort

    def search(self):
        # Scrap this tag <div id="photo_gallery">
        # To return 2D list of PhotoPage objects
        # PhotoPageList[search_page_index][PhotoPage_index_in_search_page]

        # If use this to get multiple images, name of PhotoPage onject will be blank

        http = urllib3.PoolManager()

        PhotoPageList = []

        for page_index in range(1, self.max_pages+1):
            url = url_maker('images', page_index, self.query, self.sort)
            response = http.request('GET', url, headers=HEADERS)
            soup = bs4.BeautifulSoup(response.data, 'html.parser')

            if 'Sorry' in soup.find('div', attrs={'class': 'entries'}).find('h3').text:
                break

            tag_a_list = soup.find('div', attrs={'id':'photo_gallery'}).find_all('a', attrs={'class':'photo'})
            url_list = [KYM+tag_a['href'] for tag_a in tag_a_list]
            PhotoPageList.append([PhotoPage(u_r_l) for u_r_l in url_list])

        self.PhotoPageList = PhotoPageList


class SearchNews():
    def __init__(self, query, max_pages = 1, sort = 'relevance'):
        self.max_pages = max_pages
        self.query = query
        self.sort = sort

    def search(self):
        # Srap this tag # <div id="news-posts">
        # To return 2D list of NewsPages objects
        # NewsPageList[search_page_index][NewsPage_index_in_search_page]

        http = urllib3.PoolManager()

        NewsPageList = []

        for page_index in range(1, self.max_pages+1):
            url = url_maker('news', page_index, self.query, self.sort)
            response = http.request('GET', url, headers=HEADERS)
            soup = bs4.BeautifulSoup(response.data, 'html.parser')

            if 'Sorry' in soup.find('div', attrs={'class': 'entries'}).find('h3').text:
                break

            url_list = ['https:'+h1.find('a')['href'] for h1 in soup.find('div', attrs={"id":"entries"}).find_all('div')[1].find_all('h1')]
            url_list = [u_r_l.replace(':443', '') for u_r_l in url_list]
            print(url_list)
            NewsPageList.append([NewsPage(u_r_l) for u_r_l in url_list])

        self.NewsPageList = NewsPageList


class SearchEngine():
    # A class to search for MemePage, PhotoPage, VideoPage
    def __init__(self, query, context = 'entries', max_pages = 1, sort = 'relevance'):
        # context : 'entries' or 'images' or 'news'
        # max_pages : a positive number
        # query : a string, for example 'Elon Musk'
        # sort : 'relevance' or 'views' or 'newest' or 'oldest'

        if max_pages < 1:
            self.max_pages = 1
        else:
            self.max_pages = max_pages

        if context not in ['entries', 'images', 'news']:
            self.context = 'entries'
        else:
            self.context = context

        if sort not in ['relevance', 'views', 'newest', 'oldest']:
            self.sort = 'relevance'
        else:
            self.sort = sort

        if type(query) == type('') and query != '':
            # Format query to have the valid format
            self.query = query.replace(' ', '+', -1)
        else:
            print('Query is not a string')
            self.query = ''


    def build(self):
        # Build object SearchEntry, SearchImage, SearchNews
        if self.query == '':
            print('No object is build')
            return None
        else:
            if self.context == 'entries':
                return SearchEntry(query=self.query, max_pages=self.max_pages, sort=self.sort)

            if self.context == 'images':
                return SearchImage(query=self.query, max_pages=self.max_pages, sort=self.sort)

            if self.context == 'news':
                return SearchNews(query=self.query, max_pages=self.max_pages, sort=self.sort)
