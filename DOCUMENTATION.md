# Documentation

A poor documentation of PerceiveYourMeme. Checkout [`EXAMPLE.py`](EXAMPLE.py) for more examples.

### Contents
- [Import](#Import)
- [MemePage](#MemePage)
- [PhotoPage](#PhotoPage)
- [NewsPage](#NewsPage)
- [SearchEngine](#SearchEngine)
- [SearchEntry](#SearchEntry)
- [SearchImage](#SearchImage)
- [SearchNews](#SearchNews)
- [GetKYM](#GetKYM)

## Import

```Python
import PerceiveYourMeme as pym
```

## MemePage

A MemePage object has:
  - Attributes
    - `basic_info_dict` : a dictionary of keys (Unit, Status, Badge, Year, Tags, Template urls)
    - `org_img_urls` : `basic_info_dict['Template urls']`

  - Methods
    - `pprint()` : Pretty print of `basic_info_dict`
    - `download_origin_image(custom = DEFAULT_DOWNLOAD_PATH)` : download the images via `org_img_urls` then name them corresponding to `basic_info_dict['Name']`. If `DEFAULT_DOWNLOAD_PATH` is empty, images will be stored in the working-on directory.
    - `get_org_img_urls()` and `set_org_img_urls()` : to modify and update `org_img_urls` and `basic_info_dict['Template urls']` at the same time. In some cases (rare), you have to specify these urls manually.

__Example__

```Python
crying_cat = pym.MemePage('https://knowyourmeme.com/memes/crying-cat')
# Creat a MemePage object

print(crying_cat.basic_info_dict)
# Ugly print of basic_info_dict

crying_cat.pprint()
# Pretty print of basic_info_dict

print(crying_cat.get_org_img_urls())
# Print a list of original images urls

crying_cat.download_origin_image()
# Download images
```

## PhotoPage

A PhotoPage object has:
  - Attributes
    - `basic_info_dict` : a dictionary of keys (Photo url, Id, Name, Direct photo url)
    - `dir_photo_url` : `basic_info_dict['Direct photo url']`

  - Methods
    - `pprint()` : Pretty print of `basic_info_dict`
    - `download_photo(custom = DEFAULT_DOWNLOAD_PATH)`: download photo via `dir_photo_url` then name it corresponding to `basic_info_dict['Name']`. If `DEFAULT_DOWNLOAD_PATH` is empty, photo will be stored in the working-on directory.

__Example__

```Python
UzakiTsuki = pym.PhotoPage('https://knowyourmeme.com/photos/1891689-uzaki-chan-wants-to-hang-out')
# Creat a PhotoPage object

UzakiTsuki.pprint()
# Pretty print of basic_info_dict

UzakiTsuki.download_photo()
# Download photo
```

## NewsPage

A NewsPage object has:
  - Attributes
    - `basic_info_dict` : a dictionary of keys (Heading, Timestamp, Author, Head img url)
    - `head_img_url` : `basic_info_dict['Head img url']`

  - Methods
    - `pprint()` : Pretty print of `basic_info_dict`
    - `download_head_img(custom = DEFAULT_DOWNLOAD_PATH)` : download head image via `head_img_url` then name it corresponding to `basic_info_dict['Heading']`. If `DEFAULT_DOWNLOAD_PATH` is empty, image will be stored in the working-on directory.

__Example__

```Python
random_news = pym.NewsPage('https://news.knowyourmeme.com/news/mia-khalifa-is-auctioning-iconic-porn-glasses-to-raise-money-for-beirut')
# Creat a NewsPage object

random_news.pprint()
# Pretty print of basic_info_dict

random_news.download_head_img()
# Download head image
```

## SearchEngine

A SearchEngine object can build SearchEntry, SearchImage, SearchNews depending on the input

Create an engine

```Python
SearchEngine(query, context = 'entries', max_pages = 1, sort = 'relevance')
# context : 'entries' or 'images' or 'news'
# max_pages : a positive number
# query : a string, for example 'Elon Musk'
# sort : 'relevance' or 'views' or 'newest' or 'oldest'
```

An engine has:
  - Attributes
    - `query`
    - `context`
    - `max_pages`
    - `sort`

  - Methods
    - `build()` : return a SearchEntry object or a SearchImage object or a SearchNews object

_Tip_ Use when you need mass search

## SearchEntry

```Python
class SearchEntry():
    def __init__(self, query, max_pages = 1, sort = 'relevance'):
        self.max_pages = max_pages
        self.query = query
        self.sort = sort

    def search(self):
        # Scrap this tag <table class="entry_list">
        # To return 2D list of MemePage objects
        # MemePageList[search_page_index][MemePage_index_in_search_page]
```

Use attribute `MemePageList` of SearchEntry object to get the results

__Example__

```Python
ElonMuskEntries = pym.SearchEntry('Elon Musk')
ElonMuskEntries.search()
for page in ElonMuskEntries.MemePageList:
    for meme in page:
        meme.pprint()
```

## SearchImage

```Python
class SearchImage():
    def __init__(self, query, max_pages = 1, sort = 'relevance'):
        self.max_pages = max_pages
        self.query = query
        self.sort = sort

    def search(self):
        # Scrap this tag <div id="photo_gallery">
        # To return 2D list of PhotoPage objects
        # PhotoPageList[search_page_index][PhotoPage_index_in_search_page]
```

Use attribute `PhotoPageList` of SearchImage object to get the results

## SearchNews

```Python
class SearchNews():
    def __init__(self, query, max_pages = 1, sort = 'relevance'):
        self.max_pages = max_pages
        self.query = query
        self.sort = sort

    def search(self):
        # Srap this tag # <div id="news-posts">
        # To return 2D list of NewsPages objects
        # NewsPageList[search_page_index][NewsPage_index_in_search_page]
```

Use attribute `NewsPageList` of SearchNews object to get the results

## GetKYM

A set of three functions to get stuff from [memes](https://knowyourmeme.com/memes), [photos](https://knowyourmeme.com/photos), [news](https://news.knowyourmeme.com/news)

```Python
def get_memes(directory = '', page_index = 1, sort = ''):
    # directory : '' or 'popular' or 'submissions'
    # page_index : a positive integer
    # sort : '' or 'views' or 'comments'
    # To return a list of MemePage objects
```

```Python
def get_photos(directory = '', page_index = 1):
    # directory : '' or 'trending' or 'most-commented'
    # page_index : a positive integer
    # To return a list of PhotoPage objects
```

```Python
def get_news(page_index = 1):
    # page_index : a positive integer
    # To return a list of NewsPage objects
```

__Example__

```Python
MemePages = pym.get_memes()
```
