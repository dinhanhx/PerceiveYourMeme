import urllib3
import bs4
from CONST import HEADERS

def url_maker(context, page_index, query, sort):
    return 'https://knowyourmeme.com/search?context=' + context + '&page=' + str(page_index) + '&q=' + query + '&sort=' + sort

class SearchEntry():
    def __init__(self, max_pages = 1, query, sort = 'relevance'):
        pass

class SearchImage():
    def __init__(self, max_pages = 1, query, sort = 'relevance'):
        pass

class SearchNews():
    def __init__(self, max_pages = 1, query, sort = 'relevance'):
        pass

class SearchEngine():
    # A class to search for MemePage, PhotoPage, VideoPage
    def __init__(self, context = 'entries', max_pages = 1, query, sort = 'relevance'):
        # context : 'entries' or 'images' or 'news'
        # max_pages : a positive number
        # query : a string, for example 'Elon Musk'
        # sort : 'relevance' or 'views' or 'newest' or 'oldest'

        if max_pages < 1:
            max_pages = 1

        if context is not in ['entries', 'images', 'news']:
            context = 'entries'

        if sort is not in ['relevance', 'views', 'newest', 'oldest']:
            sort = 'relevance'

        if type(query) == type(' '):
            # Format query to have the valid format
            query = query.replace(' ', '+', -1)

            if context == 'entries':
                return SearchEntry(max_pages=max_pages, query=query, sort=sort)

            if context == 'images':
                return SearchImage(max_pages=max_pages, query=query, sort=sort)

            if context == 'news':
                return SearchNews(max_pages=max_pages, query=query, sort=sort)


        else:
            print('Query is not a string')
