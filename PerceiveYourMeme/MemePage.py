# TODO
# 1. Refactor __init__()
# 2. Add checking url

import urllib3
import bs4
from CONST import HEADERS, DEFAULT_DOWNLOAD_PATH

class MemePage():
    # An object to store basic information and template of a meme
    def __init__(self, url):
        basic_info_dict = {}
        # Store Meme url
        basic_info_dict['Meme url'] = url

        # Name meme
        basic_info_dict['Name'] = url.split('/')[-1].replace('-', ' ')

        # Get the html document. This can be slow due to the internet
        http = urllib3.PoolManager()
        response = http.request('GET', url, headers=HEADERS)
        entry_body = bs4.BeautifulSoup(response.data, 'html.parser').find('div', attrs={"class": "c", "id": "entry_body"})

        # Get basic information and entry tags from entry body
        basic_info = [ele for ele in entry_body.find('dl').text.split('\n') if ele != '']
        entry_tags = [ele for ele in
                    entry_body.find('dl', attrs={"id":"entry_tags"}).text.split('\n') if ele != '']

        # Then store them
        basic_info_dict['Unit'] = basic_info[0]
        basic_info_dict['Status'] = basic_info[2]
        basic_info_dict['Type'] = basic_info[4]
        basic_info_dict['Year'] = basic_info[6]

        basic_info_dict['Tags'] = entry_tags[1]

        # Get url of template
        self.org_img_urls = [ele['data-src'] for ele in entry_body.find('center').find_all('img')]

        # Store url to basic_info_dict
        basic_info_dict['Template urls'] = self.org_img_urls

        # Store basic information
        self.basic_info_dict = basic_info_dict


    def pprint(self):
        # Pretty print of basic_info_dict
        from json import dumps
        print(dumps(self.basic_info_dict, indent=3))


    def download_origin_image(self, custom_path = DEFAULT_DOWNLOAD_PATH):
        # Download images
        # then name them corresponding to self.basic_info_dict['Name']
        # Use attributes self.org_img_urls
        http = urllib3.PoolManager()
        i = 0
        for org_img_url in self.org_img_urls:
            response = http.request('GET', org_img_url, HEADERS)
            file_type = org_img_url.split('.')[-1].split('?')[0]
            fname_path = DEFAULT_DOWNLOAD_PATH + self.basic_info_dict['Name'] + str(i)
            with open(fname_path+'.'+file_type, 'wb') as f:
                f.write(response.data)

            i += 1


if __name__ == '__main__':
    crying_cat = MemePage('https://knowyourmeme.com/memes/crying-cat')
    crying_cat.pprint()
    # crying_cat.download_origin_image()