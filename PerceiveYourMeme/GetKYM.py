# This file contains of functions
# that are dedicated to get memes, images, news
# from hashes in CONST.py

import urllib3
import bs4
from .CONST import *

def get_memes(directory = None, page_index = 1, sort = ''):
    # directory : None or 'popular' or 'submissions'
    # page_index : a positive integer
    url = ''

    if page_index < 1:
        page_index = 1

    if directory is None:
        url = KYM_HASH['memes'] + str(page_index) + MEMES_SORT_HASH[sort]
    else:
        if directory in ['popular', 'submissions']:
            url = MEMES_HASH[directory] + str(page_index) + MEMES_SORT_HASH[sort]
        else:
            url = KYM_HASH['memes'] + str(page_index) + MEMES_SORT_HASH[sort]


    pass

def get_photos(directory = None, page_index = 1):
    # directory : None or 'trending' or 'most-commented'
    # page_index : a positive integer
    url = ''

    if page_index < 1:
        page_index = 1

    if directory is None:
        url = KYM_HASH['photos'] + str(page_index)
    else:
        if directory in ['trending', 'most-commented']:
            url = PHOTOS_HASH[directory] + str(page_index)
        else:
            url = KYM_HASH['photos'] + str(page_index)


    pass

def get_news(page_index = 1):
    # page_index : a positive integer
    if page_index < 1:
        page_index = 1

    url = KYM_HASH['news'] + str(page_index)
    pass
