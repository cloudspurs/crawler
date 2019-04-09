import requests
from requests import exceptions

import chardet

from bs4 import BeautifulSoup


# get html_base content
def get_html_content(url, timeout=5, html_encoding=None):
    try:
        html = requests.get(url, timeout=timeout)
        # print(html_base.encoding)
        # print(html_base.headers)
        # print(chardet.detect(html_base.content))
    except exceptions.Timeout as e:
        print('Timeout', url, str(e))
        return None
    except exceptions.HTTPError as e:
        print('Http error', url, str(e))
        return None
    else:
        if html_encoding is None:
            html_encoding = chardet.detect(html.content)['encoding']
            # print(html_encoding)

        try:
            content = BeautifulSoup(
                html.text.encode(html.encoding, errors='ignore').decode(html_encoding, errors='ignore'),
                'html.parser')

        except UnicodeEncodeError as e:
            print(UnicodeEncodeError, url, str(e))
            content = None

        return content


if __name__ == '__main__':
    domain = 'http://www.jsyzyz.com/'
    u = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=213&scount=13622&page=1'

    for i in range(455):
        c = get_html_content(u)

        # last page has no next page
        if i < 455 and c is not None:
            # get next page url
            u = c.find('a', text='下一页')['href']
            u = domain + u
            print(u)

