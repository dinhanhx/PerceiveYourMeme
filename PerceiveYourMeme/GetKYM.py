# This file contains of functions
# that are dedicated to get memes, images, news
# from hashes in CONST.py

import urllib3
import bs4
try:
    from .CONST import *
    from .NewsPage import NewsPage
    from .PhotoPage import PhotoPage
    from .MemePage import MemePage
except ImportError:
    from CONST import *
    from NewsPage import NewsPage
    from PhotoPage import PhotoPage
    from MemePage import MemePage

def get_soup(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url, headers=HEADERS)
    soup = bs4.BeautifulSoup(response.data, 'html.parser')
    return soup

def get_memes(directory = '', page_index = 1, sort = ''):
    # directory : '' or 'popular' or 'submissions'
    # page_index : a positive integer
    # sort : '' or 'views' or 'comments'
    # To return a list of MemePage objects
    url = ''

    if page_index < 1:
        page_index = 1

    if directory == '':
        url = KYM_HASH['memes'] + str(page_index) + MEMES_SORT_HASH[sort]
    else:
        if directory in ['popular', 'submissions']:
            url = MEMES_HASH[directory] + str(page_index) + MEMES_SORT_HASH[sort]
        else:
            url = KYM_HASH['memes'] + str(page_index) + MEMES_SORT_HASH[sort]


    soup = get_soup(url)

    tag_a_list = soup.find('table', attrs={'class':'entry_list'}).find_all('a', attrs={'class':'photo'})
    url_list = [KYM+tag_a['href'] for tag_a in tag_a_list]

    return [MemePage(u_r_l) for u_r_l in url_list]

def get_photos(directory = '', page_index = 1):
    # directory : '' or 'trending' or 'most-commented'
    # page_index : a positive integer
    # To return a list of PhotoPage objects
    url = ''

    if page_index < 1:
        page_index = 1

    if directory == '':
        url = KYM_HASH['photos'] + str(page_index)
    else:
        if directory in ['trending', 'most-commented']:
            url = PHOTOS_HASH[directory] + str(page_index)
        else:
            url = KYM_HASH['photos'] + str(page_index)


    soup = get_soup(url)

    tag_a_list = soup.find('div', attrs={'id':'photo_gallery'}).find_all('a', attrs={'class':'photo'})
    url_list = [KYM+tag_a['href'] for tag_a in tag_a_list]

    return [PhotoPage(u_r_l) for u_r_l in url_list]

def get_news(page_index = 1):
    # page_index : a positive integer
    # To return a list of NewsPage objects
    if page_index < 1:
        page_index = 1

    url = KYM_HASH['news'] + str(page_index)

    soup = get_soup(url)

    url_list = ['https:'+h1.find('a')['href'] for h1 in soup.find('div', attrs = {'id': 'maru'}).find_all('div')[1].find_all('h1')]
    url_list = [u_r_l.replace(':443', '') for u_r_l in url_list]

    return [NewsPage(u_r_l) for u_r_l in url_list]
