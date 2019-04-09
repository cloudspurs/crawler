import requests
from bs4 import BeautifulSoup

domain = 'http://www.jsyzyz.com/'


# get all articles links
def get_links(url, max_page_num):
    links = []

    for i in range(0, max_page_num):
        html = requests.get(url)
        try:
            soup = BeautifulSoup(html.text.encode('iso-8859-1', errors='ignore').decode('gb18030', errors='ignore'), 'html_base.parser')

            # lis = soup.select('.page_lborder')[0].select('li')
            # for li in lis:
            #     links.append(li.a['href'])
            # url = soup.find('a', text='下一页')['href']

            tds = soup.select(".black3")
            for td in tds:
                # print(domain + td.a['href'])
                links.append(domain + td.a['href'])

            if i < max_page_num-1:
                url = soup.find('a', text='下一页')['href']
                url = domain + url

        except Exception as e:
            print(repr(e))
            print(url)

    return links
