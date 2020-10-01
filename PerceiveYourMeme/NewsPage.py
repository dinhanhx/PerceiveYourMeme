import urllib3
import bs4
from .CONST import HEADERS, DEFAULT_DOWNLOAD_PATH

def isValid(url):
    if 'https://news.knowyourmeme.com/news' in url:
        http = urllib3.PoolManager()
        response = http.request('GET', url, headers=HEADERS)
        if response.status == 200:
            return True
        else:
            return False

    else:
        return False

class NewsPage():
    # An object to store a news articles
    def __init__(self, url):
        if isValid(url):
            self.basic_info_dict = {}
            # Store News url
            self.basic_info_dict['News url'] = url

            # Get the html document. This can be slow due to the internet
            http = urllib3.PoolManager()
            response = http.request('GET', url, headers=HEADERS)
            soup = bs4.BeautifulSoup(response.data, 'html.parser')

            try:
                # Get the super_header information
                super_header = soup.find('div', attrs={'id':'super-header'})
                self.basic_info_dict['Heading'] = super_header.find('h1').text[1:-1]
                self.basic_info_dict['Timestamp'] = super_header.find('span', attrs={'class':'header-timestamp'}).text[1:-1]
                self.basic_info_dict['Author'] = super_header.find('p', attrs={'class':'header-timestamp'}).find('a').text

                # Get the heading img
                self.head_img_url = soup.find('div', attrs={'id':'maru'}).find('img', attrs={'class':'news-post-header-image'})['data-src']

                # Store url to basic_info_dict
                self.basic_info_dict['Head image url'] = self.head_img_url
            except:
                self.basic_info_dict['Heading'] = ''
                self.basic_info_dict['Timestamp'] = ''
                self.basic_info_dict['Author'] = ''
                self.head_img_url = ''
                self.basic_info_dict['Head image url'] = ''

        else:
            print('Not a valid url')
            self.basic_info_dict = {}
            self.head_img_url = None


    def pprint(self):
        # Pretty print of basic_info_dict
        from json import dumps
        print(dumps(self.basic_info_dict, indent=3))

    def download_head_img(self, custom_path = DEFAULT_DOWNLOAD_PATH):
        # Download photo
        # then name them corresponding to self.basic_info_dict['Head']
        # Use attributes self.head_img_url
        if type(self.head_img_url) == type(' '):
            http = urllib3.PoolManager()
            response = http.request('GET', self.head_img_url, headers=HEADERS)
            if response.status == 200:
                file_type = response.headers['Content-Type'].split('/')[-1]
                fname_path = DEFAULT_DOWNLOAD_PATH + self.basic_info_dict['Heading']
                with open(fname_path+'.'+file_type, 'wb') as f:
                    f.write(response.data)

                return True

            else:
                print('Head img url is missing or invalid')
                return False

        else:
            print('Head img url is missing or invalid')
            return False

if __name__ == '__main__':
    random_news = NewsPage('https://news.knowyourmeme.com/news/mia-khalifa-is-auctioning-iconic-porn-glasses-to-raise-money-for-beirut')
    random_news.pprint()
    # random_news.download_head_img()
