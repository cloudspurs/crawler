import requests
from requests import exceptions

from bs4 import BeautifulSoup
import chardet
import time


# get html page content
def get_html_content(url, timeout=5, file_encoding=None, page_encoding=None):
    try:
        page = requests.get(url, timeout=timeout)
    except exceptions.Timeout as e:
        print('Timeout', url, str(e))
        return None
    except exceptions.HTTPError as e:
        print('Http error', url, str(e))
        return None
    except Exception as e:
        print('Connect error', url, str(e))
        return None
    else:
        if file_encoding is None:
            file_encoding = page.encoding if page.encoding is not None else 'iso-8859-1'

        if page_encoding is None:
            page_encoding = chardet.detect(page.content)['encoding']

        try:
            # str -decode-> str(unicode) -encode-> str
            # 源文件 -> encode -> decode
            # 源文件编码: page.encoding, 网页编码: page_encoding
            content = BeautifulSoup(
                page.text.encode(file_encoding, errors='ignore').decode(page_encoding, errors='ignore'),
                'lxml')

        except UnicodeEncodeError as e:
            print(UnicodeEncodeError, url, str(e))
            content = None

        return content


if __name__ == '__main__':
    domain = 'http://www.jsyzyz.com/'
    u = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=213&scount=13622&page=1'

    time_1 = time.time()
    max = 10
    for i in range(max):
        c = get_html_content(u)

        # last page has no next page
        if i < max and c is not None:
            # get next page url
            u = c.find('a', text='下一页')['href']
            u = domain + u
            print(u)

    time_2 = time.time()
    print(time_2-time_1)
