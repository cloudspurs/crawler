import json
import html_base.get_html_content as html
import page.page_yzyz as page

domain = 'http://www.jsyzyz.com/'


# 按页爬取案例：先获取一个的所有案例链接，然后把这一页的所有案例爬下来
# url: first page url
# max_page: total number of pages to crawl
def get_link_by_page(url, max_page, output_file):
    case_num = 0

    for i in range(max_page):
        print('page', i)

        soup = html.get_html_content(url)

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
                case_num += 1

                paper = {'title': title, 'author': author, 'content': content}
                # papers.append(paper)
                path = output_file + '.json'
                with open(path, 'a', encoding='utf-8') as file:
                    file.write(json.dumps(paper, ensure_ascii=False) + '\n')

                # path = "../resource/" + output_file + "/" + str(case_num) + ".txt"
                # with open(path, 'w', encoding='utf-8') as file:
                #     file.write(paper['title'])
                #     file.write('\n')
                #     file.write(paper['author'])
                #     file.write('\n')
                #     file.write(paper['content'])
                #     file.write('\n')
                #     file.close()

        # last page has no next page
        if i < max_page-1:
            # get next page url
            url = soup.find('a', text='下一页')['href']
            url = domain + url

    print('case number', case_num)


###################################################################################
# main function

# 德育案例 22
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=93'
# 案例研究 13
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=61'
# 班主任论坛 13
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=81'

# 我的教育故事 1
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=275'
# 魏书生专栏 9
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=82'
# 校长荐读 21
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=215'
# 班主任札记 455
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=213'
url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=213&scount=13622&page=163'
# 教育思考 373
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=59'
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=59&scount=11190&page=193'

get_link_by_page(url, 292, 'bzrzj')
