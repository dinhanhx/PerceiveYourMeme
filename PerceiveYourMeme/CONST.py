# KYM : Known Your Meme

KYM_HASH = {'memes':'https://knowyourmeme.com/memes/page/',
            'photos':'https://knowyourmeme.com/photos/page/',
            'news':'https://knowyourmeme.com/news/page/'}
# KYM_HASH : a set of directories
# append a positive integer to get the corresponding page number
# For example, https://knowyourmeme.com/memes/page/1 will be the page.

MEMES_HASH = {'popular':'https://knowyourmeme.com/memes/popular/page/',
                'submissions':'https://knowyourmeme.com/memes/submissions/page/'}
# MEMES_HASH : a set of directories
# append a positive integer to get the corresponding page number
# For example, https://knowyourmeme.com/memes/popular/page/1 will be the page.

MEMES_SORT_HASH = {'views':'?sort=views', 'comments':'?sort=comments'}
# MEMES_SORT_HASH : a set of sorting methods
# append sort method to MEMES_HASH or KYM_HASH['memes'] to get sort
# For example, https://knowyourmeme.com/memes/popular/page/1?sort=views

PHOTOS_HASH = {'trending':'https://knowyourmeme.com/photos/trending/page/',
                'most-commented':'https://knowyourmeme.com/photos/most-commented/page/'}
# MEMES_HASH : a set of directories
# append a positive integer to get the corresponding page number
# For example, https://knowyourmeme.com/memes/trending/page/1 will be the page.
