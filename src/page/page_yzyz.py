import sys
sys.path.append('../')

import html_base.get_html_content as html


# get articles' content
# url: article url
def parser(article_url):
    soup = html.get_html_content(article_url, page_encoding='gb18030')
    try:
        if soup is None:
            return None, None, None

        if soup.find('html') is None:
            print('not html page', article_url)
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
    except:
        title = None
        author = None
        content = None

    return title, author, content
