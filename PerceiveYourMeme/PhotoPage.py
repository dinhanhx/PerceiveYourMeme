import urllib3
import bs4
import os
from json import dumps
try:
    from .CONST import HEADERS, DEFAULT_DOWNLOAD_PATH
except ImportError:
    from CONST import HEADERS, DEFAULT_DOWNLOAD_PATH


def isValid(url):
    """Checks if given url is a valid know your meme photo url"""

    if 'https://knowyourmeme.com/photos/' in url:
        http = urllib3.PoolManager()
        response = http.request('GET', url, headers=HEADERS)
        return response.status == 200, response
    return False, None


class PhotoPage():
    """Creates an object which stores basic details of a photo and the photo itself"""
    
    def __init__(self, url):
        self.basic_info_dict = {}

        valid, response = isValid(url)
        if valid:
            # Store Photo url
            self.basic_info_dict['Original url'] = url

            # Get name and id of photo
            id_name = url.split('/')[-1].split('-')
            self.basic_info_dict['Id'] = id_name[0]
            self.basic_info_dict['Name'] = ' '.join(id_name[1:])

            # Get soup. Can be slow due to internet speeds
            soup = bs4.BeautifulSoup(response.data, 'html.parser')

            # Get direct url of photo
            try:
                photo = soup.find('textarea', attrs={"class": "photo_embed"})
                photo = photo.text.replace(' ', '').replace('!', '')
                self.basic_info_dict['Direct photo url'] = photo

            except AttributeError:
                print("No direct url for this photo was found")
                self.basic_info_dict['Direct photo url'] = None
        else:
            print('Not a valid url')

    def pprint(self):
        """Pretty print of basic_info_dict"""

        print(dumps(self.basic_info_dict, indent=3))

    def download_photo(self, custom_path=DEFAULT_DOWNLOAD_PATH):
        """Download photo from given url custom_path/Photo name 
        If no name is available, the photo is named after its ID instead
        """
        
        if self.basic_info_dict['Direct photo url']:
            http = urllib3.PoolManager()
            response = http.request('GET', self.basic_info_dict['Direct photo url'], headers=HEADERS)
            if response.status == 200:
                file_type = response.headers['Content-Type'].split('/')[-1]

                if self.basic_info_dict['Name']:
                    fname_path = os.path.join(custom_path,
                                              self.basic_info_dict['Name'].replace(" ", "_"))
                else:
                    fname_path = os.path.join(custom_path,
                                              self.basic_info_dict['Id'])

                photo_path = ''.join([fname_path, '.', file_type])
                with open(photo_path, 'wb') as f:
                    f.write(response.data)
                    print(f"Photo downloaded to {photo_path}")
        else:
            print('Dir photo url is missing or invalid')


if __name__ == '__main__':
    ur = 'https://knowyourmeme.com/photos/1891689-uzaki-chan-wants-to-hang-out'
    UzakiTsuki = PhotoPage(ur)
    UzakiTsuki.pprint()
    # UzakiTsuki.download_photo()
