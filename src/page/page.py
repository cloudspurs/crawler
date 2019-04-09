import requests
from bs4 import BeautifulSoup


# get articles' content
def parser(article_url):
    html = requests.get(article_url)
    soup = BeautifulSoup(html.text.encode('iso-8859-1').decode('gb18030', errors='ignore'), 'html_base.parser')

    title = soup.find('p', 'page_title').string.strip()

    author = ''
    subtitle = soup.find('p', 'page_time')
    if len(subtitle.contents) > 2:
        author = subtitle.contents[2]
        author = author[0:len(author) - 20].strip()
    # print(subtitle.contents)

    content = ''
    p_or_div = soup.select('#mcontent')[0].div.find_all(['p', 'div', 'h3'])
    for element in p_or_div:
        for text in element.stripped_strings:
            content += process(text)
        content += '\n'

    if len(content) < 500:
        elements = soup.select('#mcontent')[0].div
        # print(elements.contents)
        content += elements.contents[6]

    if len(content) < 500:
        print('Less 500 words: ' + article_url)
        title = ''

    if title == '':
        print('Title is null: ' + article_url)

    if author == '':
        print('Author is null: ' + article_url)

    return title, author, content


# remove useless text, add line break
def process(text):
    if text.find('中国德育网') < 0:
        return text
    else:
        return ''
