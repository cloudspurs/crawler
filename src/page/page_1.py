import requests
from requests import exceptions
from bs4 import BeautifulSoup


# get articles' content
# url: article url
def parser(article_url):
    try:
        html = requests.get(article_url, timeout=5)
    except exceptions.Timeout as e:
        print('Timeout', str(e))
        return None, None, None
    except exceptions.HTTPError as e:
        print('Http error', str(e))
        return None, None, None

    if html.status_code != 200:
        print('internal error', article_url)
        return None, None, None

    # try:
    soup = BeautifulSoup(html.text.encode('iso-8859-1', errors='ignore').decode('gb18030', errors='ignore'),
                         'html_base.parser')

    if soup.find('html_base') is None:
        print('not html_base page', article_url)
        return None, None, None

    title = soup.find('td', 'lblue3')
    if title is not None and title.string is not None:
        title = title.string.strip()
    else:
        title = None

    author = soup.find('td', 'grey4')
    if author is not None and author.string is not None:
        author = author.string.strip()
        ai1 = author.find('浏览')
        ai2 = author.find('时间')
        author = author[:ai1] + author[ai2:]
    else:
        author = None

    content = ''
    content_element = soup.find('td', 'black3')
    if content_element is not None:
        content_element = content_element.find_all(['p', 'div'])
        if content_element is not None:
            for element in content_element:
                for text in element.stripped_strings:
                    content += text
                content += '\n'

    if title is None or author is None or content is None:
        print('extract empty', article_url)

    # print(title)
    # print(author)
    # print(content)

    return title, author, content
