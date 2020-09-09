import urllib3
import bs4
from CONST import HEADERS
from MemePage import MemePage
from PhotoPage import PhotoPage
from NewsPage import NewsPage

def url_maker(context, page_index, query, sort):
    return 'https://knowyourmeme.com/search?context=' + context + '&page=' + str(page_index) + '&q=' + query + '&sort=' + sort

class SearchEntry():
    def __init__(self, max_pages = 1, query, sort = 'relevance'):
        self.max_pages = max_pages
        self.query = query
        self.sort = sort

    def search(self):
        # Scrap this tag <table class="entry_list">
        # To return 2D list of MemePage objects
        # MemePageList[search_page_index][MemePage_index_in_search_page]
        pass

class SearchImage():
    def __init__(self, max_pages = 1, query, sort = 'relevance'):
        self.max_pages = max_pages
        self.query = query
        self.sort = sort

    def search(self):
        # Scrap this tag <div id="photo_gallery">
        # To return 2D list of PhotoPage objects
        # PhotoPageList[search_page_index][PhotoPage_index_in_search_page]
        pass

class SearchNews():
    def __init__(self, max_pages = 1, query, sort = 'relevance'):
        self.max_pages = max_pages
        self.query = query
        self.sort = sort

    def search(self):
        # Srap this tag # <div id="news-posts">
        # To return 2D list of NewsPages objects
        # NewsPageList[search_page_index][NewsPage_index_in_search_page]
        pass

class SearchEngine():
    # A class to search for MemePage, PhotoPage, VideoPage
    def __init__(self, context = 'entries', max_pages = 1, query, sort = 'relevance'):
        # context : 'entries' or 'images' or 'news'
        # max_pages : a positive number
        # query : a string, for example 'Elon Musk'
        # sort : 'relevance' or 'views' or 'newest' or 'oldest'

        if max_pages < 1:
            self.max_pages = 1
        else:
            self.max_pages = max_pages

        if context is not in ['entries', 'images', 'news']:
            self.context = 'entries'
        else:
            self.context = context

        if sort is not in ['relevance', 'views', 'newest', 'oldest']:
            self.sort = 'relevance'
        else:
            self.sort = sort

        if type(query) == type('') && query != '':
            # Format query to have the valid format
            self.query = query.replace(' ', '+', -1)
        else:
            print('Query is not a string')
            self.query = ''


    def build(self):
        # Build object SearchEntry, SearchImage, SearchNews
        if self.query = '':
            print('No object is build')
            return None
        else:
            if self.context == 'entries':
                return SearchEntry(context=self.context, max_pages=self.max_pages, query=self.query, sort=self.sort)

            if self.context == 'images':
                return SearchImage(context=self.context, max_pages=self.max_pages, query=self.query, sort=self.sort)

            if self.context == 'news':
                return SearchNews(context=self.context, max_pages=self.max_pages, query=self.query, sort=self.sort)
