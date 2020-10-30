import sys
try:
    sys.path.append('../PerceiveYourMeme')
    import PerceiveYourMeme as pym
except ImportError:
    sys.path.append('PerceiveYourMeme')
    import PerceiveYourMeme as pym

def runner():
    Smudge = pym.MemePage('https://knowyourmeme.com/memes/smudge-the-cat')
    Smudge.pprint()
    Smudge.download_origin_image()

    OneRace = pym.PhotoPage('https://knowyourmeme.com/photos/1894354-nordic-mediterranean')
    OneRace.pprint()
    OneRace.download_photo()

    Mia = pym.NewsPage('https://news.knowyourmeme.com/news/mia-khalifa-is-auctioning-iconic-porn-glasses-to-raise-money-for-beirut')
    Mia.pprint()
    Mia.download_head_img()

    western_animation = pym.VideoPage('https://knowyourmeme.com/videos/225020-western-animation')
    western_animation.pprint()

    ElonMuskEntries = pym.SearchEntry('Elon Musk')
    ElonMuskEntries.search()
    for page in ElonMuskEntries.MemePageList:
        for meme in page:
            meme.pprint()


    ElonMuskImages = pym.SearchImage('Elon Musk')
    ElonMuskImages.search()
    for page in ElonMuskImages.PhotoPageList:
        for photo in page:
            photo.pprint()


    ElonMuskNews = pym.SearchNews('Elon Musk')
    ElonMuskNews.search()
    for page in ElonMuskNews.NewsPageList:
        for news in page:
            news.pprint()


    for meme in pym.get_memes():
        meme.pprint()

    for photo in pym.get_photos():
        photo.pprint()

    for news in pym.get_news():
        news.pprint()

    return True

def test_runner():
    assert runner() == True
