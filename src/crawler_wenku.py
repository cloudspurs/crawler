import html_base.get_html_content as html
import page.page_wenku as page

url = 'http://www.jingpinwenku.com/list/%E5%BE%B7%E8%82%B2%E6%A1%88%E4%BE%8B'

content = html.get_html_content(url, html_encoding='utf-8')

html_div = content.find('div', 'page-list')
links = html_div.find_all('a')

for i, link in enumerate(links):
    print(i)
    article = page.page(link['href'])
    path = "../resource/wenku_deyuanli/" + str(i) + ".txt"
    with open(path, 'w', encoding='utf-8') as file:
        file.write(article)
        file.close()
