import requests
from requests import exceptions
from bs4 import BeautifulSoup

import page_1 as page

domain = 'http://www.jsyzyz.com/'


# 按页爬取案例：先获取一个的所有案例链接，然后把这一页的所有案例爬下来
# url: first page url
# max_page: total number of pages to crawl
def get_link_by_page(url, max_page):
    for i in range(max_page):
        print('page', i)

        try:
            html = requests.get(url, timeout=5)
        except exceptions.Timeout as e:
            print('Timeout', str(e))
            continue
        except exceptions.HTTPError as e:
            print('Http error', str(e))
            continue

        # str -decode-> str(unicode) -encode-> str
        # 源文件 -> encode -> decode
        # 源文件编码: iso-8859-1(html_base.encoding), 网页编码: gb18030
        soup = BeautifulSoup(html.text.encode(html.encoding, errors='ignore').decode('gb18030', errors='ignore'),
                             'html_base.parser')

        # get all links
        links = []
        tds = soup.select(".black3")
        if tds is not None:
            for td in tds:
                href = td.a['href']
                if href is not None:
                    links.append(domain + td.a['href'])

        for j, link in enumerate(links):
            print('page', i, 'article', j)

            title, author, content = page.parser(link)

            if (title is not None) and (author is not None) and (content is not None):
                paper = {'title': title, 'author': author, 'content': content}
                # papers.append(paper)

                path = "../resource/jysk/" + str((150 + i) * 30 + j) + ".txt"
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(paper['title'])
                    file.write('\n')
                    file.write(paper['author'])
                    file.write('\n')
                    file.write(paper['content'])
                    file.write('\n')
                    file.close()

        # last page has no next page
        if i < max_page:
            # get next page url
            url = soup.find('a', text='下一页')['href']
            url = domain + url


###################################################################################
# main function

# 校长荐读 21
# real_url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=215'
# 班主任札记 455 215+98=313
# real_url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=213'
# real_url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=213&scount=13622&page=313'
# 教育思考 373 150
# real_url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=59'
real_url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=59&scount=11190&page=150'

get_link_by_page(real_url, 223)
