import urllib3
import bs4
from json import dumps

from CONST import HEADERS, DEFAULT_DOWNLOAD_PATH



def isValid(url):
    if url.startswith('https://knowyourmeme.com/videos/'):
        http = urllib3.PoolManager()
        response = http.request('GET', url, headers=HEADERS)

        return response.status == 200
    return False


class VideoPage():
    """Creates objects to store basic details of a video and that video"""
    
    def __init__(self, url):
        # Contains all basic information about the video
        self.basic_info_dict = {}

        if isValid(url):
            self.basic_info_dict['Original url'] = url

            # Get name and id of video from url
            id_name = url.split('/')[-1].split('-')
            self.basic_info_dict['Id'] = id_name[0]
            self.basic_info_dict['Name'] = ' '.join(id_name[1:])

            # Get soup
            http = urllib3.PoolManager()
            response = http.request('GET', url, headers=HEADERS)
            soup = bs4.BeautifulSoup(response.data, 'html.parser')
            # Get direct video url
            # try:
            dir_url = soup.find("iframe", attrs={"class": "embedly-embed"})
            print(dir_url)  
            # Returns where the document is embedded but I have no idea how to then search inside this document to get the direct url

            #     self.basic_info_dict['Direct url'] = dir_url
            # except:
            #     print('No direct video url could be found')
        else:
            print('Not a valid url')

    def pprint(self):
        """Pretty print of self.basic_info_dict"""
        print(dumps(self.basic_info_dict, indent=3))
   

if __name__ == '__main__':
    western_animation = VideoPage('https://knowyourmeme.com/videos/225020-western-animation')
    western_animation.pprint()

