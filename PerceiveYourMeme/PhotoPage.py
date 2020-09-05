import urllib3
import bs4
from CONST import HEADERS, DEFAULT_DOWNLOAD_PATH

def isValid(url):
    if 'https://knowyourmeme.com/photos/' in url:
        http = urllib3.PoolManager()
        response = http.request('GET', url, headers=HEADERS)
        if response.status == 200:
            return True
        else:
            return False

    else:
        return False

class PhotoPage():
    # An object to store basic detail of a photo and that photo
    def __init__(self, url):
        if isValid(url):
            basic_info_dict = {}
            # Store Photo url
            basic_info_dict['Photo url'] = url

            # Name photo
            id_name = url.split('/')[-1].replace('-', ' ')
            id_name = id_name.split(' ')
            basic_info_dict['Id'] = id_name[0]
            basic_info_dict['Name'] = ' '.join(id_name[1:])

            # Get the html doccument. This can be slow due to the internet
            http = urllib3.PoolManager()
            response = http.request('GET', url, headers=HEADERS)
            soup = bs4.BeautifulSoup(response.data, 'html.parser')

            # Get direct url of photo
            self.dir_photo_url = soup.find('textarea', attrs={"class":"photo_embed"}).text.replace(' ','').replace('!','')

            # Store url to basic_info_dict
            basic_info_dict['Direct photo url'] = self.dir_photo_url

            # Store basic information
            self.basic_info_dict = basic_info_dict
        else:
            print('Not a valid url')
            self.basic_info_dict = {}
            self.dir_photo_url = None


    def pprint(self):
        # Pretty print of basic_info_dict
        from json import dumps
        print(dumps(self.basic_info_dict, indent=3))


    def download_photo(self, custom_path = DEFAULT_DOWNLOAD_PATH):
        # Download photo
        # then name them corresponding to self.basic_info_dict['Name']
        # Use attributes self.dir_photo_url
        if type(self.dir_photo_url) == type(' '):
            http = urllib3.PoolManager()
            response = http.request('GET', self.dir_photo_url, headers=HEADERS)
            file_type = self.dir_photo_url.split('.')[-1].split('?')[0]
            fname_path = DEFAULT_DOWNLOAD_PATH + self.basic_info_dict['Name']
            with open(fname_path+'.'+file_type, 'wb') as f:
                f.write(response.data)

        else:
            print('Dir photo url is missing or invalid')


if __name__ == '__main__':
    UzakiTsuki = PhotoPage('https://knowyourmeme.com/photos/1891689-uzaki-chan-wants-to-hang-out')
    UzakiTsuki.pprint()
    UzakiTsuki.download_photo()
