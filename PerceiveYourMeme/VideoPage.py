import urllib3
import bs4
from json import dumps

from .CONST import HEADERS, DEFAULT_DOWNLOAD_PATH


def isValid(url):
    if url.startswith('https://knowyourmeme.com/videos/'):
        http = urllib3.PoolManager()
        response = http.request('GET', url, headers=HEADERS)
        if response.status == 200:
            return True
        else:
            return False

    else:
        return False


class VideoPage():
    """Creates objects to store basic details of a video and that video"""
    
    def __init__(self, url):
        # Contains all basic information about the video
        self.basic_info_dict = {}

        if isValid(url):
            self.basic_info_dict['Video url'] = url

            # Get name and id of video from url
            id_name = url.split('/')[-1].split('-')
            self.basic_info_dict['Id'] = id_name[0]
            self.basic_info_dict['Name'] = ' '.join(id_name[1:])  
        else:
            print('Not a valid url')

    def pprint(self):
        """Pretty print of self.basic_info_dict"""
        print(dumps(self.basic_info_dict, indent=3))
            