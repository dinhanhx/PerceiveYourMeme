import urllib3
import bs4
try:
    from .CONST import HEADERS, DEFAULT_DOWNLOAD_PATH
except ImportError:
    from CONST import HEADERS, DEFAULT_DOWNLOAD_PATH


def isValid(url):
    if 'https://knowyourmeme.com/memes/' in url:
        http = urllib3.PoolManager()
        response = http.request('GET', url, headers=HEADERS)
        return response.status == 200

    else:
        return False


class MemePage():
    # An object to store basic information and template of a meme
    def __init__(self, url):
        if isValid(url):
            self.basic_info_dict = {}
            # Store Meme url
            self.basic_info_dict['Meme url'] = url

            # Name meme
            self.basic_info_dict['Name'] = url.split('/')[-1].replace('-', ' ')

            # Get the html document. This can be slow due to the internet
            http = urllib3.PoolManager()
            response = http.request('GET', url, headers=HEADERS)
            soup = bs4.BeautifulSoup(response.data, 'html.parser')
            try:
                entry_body = soup.find('div',
                                       attrs={"class": "c",
                                              "id": "entry_body"})

                # Get basic information and entry tags from entry body
                dl = entry_body.find('dl').text.split('\n')
                basic_info = [ele for ele in dl if ele != '']

                dl_entry = entry_body.find('dl',
                                           attrs={"id": "entry_tags"})
                dl_entry = dl_entry.text.split('\n')
                entry_tags = [ele for ele in dl_entry if ele != '']

                # Then store them
                self.basic_info_dict['Unit'] = basic_info[0]
                self.basic_info_dict['Status'] = basic_info[2]
                self.basic_info_dict['Type'] = basic_info[4]

                # NSFW stuff handler
                if basic_info[6] == 'NSFW':
                    self.basic_info_dict['Badge'] = basic_info[6]
                    self.basic_info_dict['Year'] = basic_info[8]
                else:
                    self.basic_info_dict['Badge'] = 'SFW'
                    self.basic_info_dict['Year'] = basic_info[6]

                self.basic_info_dict['Tags'] = entry_tags[1]

                # Get url of template
                self.org_img_urls = []
                if entry_body.find('center') is not None:
                    imgs = entry_body.find('center').find_all('img')
                    self.org_img_urls = [ele['data-src'] for ele in imgs]

                # Store url to basic_info_dict
                self.basic_info_dict['Template urls'] = self.org_img_urls
            except:
                self.basic_info_dict['Unit'] = ''
                self.basic_info_dict['Status'] = ''
                self.basic_info_dict['Type'] = ''
                self.basic_info_dict['Badge'] = ''
                self.basic_info_dict['Year'] = ''
                self.basic_info_dict['Tags'] = ''
                self.basic_info_dict['Template urls'] = []
                self.org_img_urls = []

        else:
            print('Not a valid url')
            self.basic_info_dict = {}
            self.org_img_urls = []

    def pprint(self):
        # Pretty print of basic_info_dict
        from json import dumps
        print(dumps(self.basic_info_dict, indent=3))

    def download_origin_image(self, custom_path=DEFAULT_DOWNLOAD_PATH):
        # Download images
        # then name them corresponding to self.basic_info_dict['Name']
        # Use attributes self.org_img_urls
        if len(self.org_img_urls) > 0:
            http = urllib3.PoolManager()
            i = 0
            for org_img_url in self.org_img_urls:
                response = http.request('GET', org_img_url, HEADERS)
                file_type = response.headers['Content-Type'].split('/')[-1]
                fname_path = (DEFAULT_DOWNLOAD_PATH +
                              self.basic_info_dict['Name'] +
                              ' ' +
                              str(i))
                with open(fname_path+'.'+file_type, 'wb') as f:
                    f.write(response.data)

                i += 1

            return True

        else:
            print('Org img urls are blank')
            return False
            # If this message shows up,
            # it means that YOU have to add these url manually
            # Use method set_org_img_urls()

    def set_org_img_urls(self, url_list):
        # To change and update
        # attributes self.org_img_urls
        self.org_img_urls = url_list
        self.basic_info_dict['Template urls'] = self.org_img_urls

    def get_org_img_urls(self):
        return self.org_img_urls


if __name__ == '__main__':
    crying_cat = MemePage('https://knowyourmeme.com/memes/crying-cat')
    crying_cat.pprint()
    # crying_cat.download_origin_image()
