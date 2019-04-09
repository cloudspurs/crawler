import link
import page_1 as page
import json

# url = 'http://www.seewww.cn/deyulunwen/index.html'
# links = link.get_links(url, 15)
# url = 'http://www.seewww.cn/deyufangfa/index.html'
# links = link.get_links(url, 10)

# 德育案例 22
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=93'
# 班主任论坛 13
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=81'
# 我的教育故事 1
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=275'
# 魏书生专栏 9
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=82'
# 校长荐读 21
url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=215'
# 班主任札记 455
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=213'
# 教育思考 373
# url = 'http://www.jsyzyz.com/List_L.asp?cid=3&lid=59'
links = link.get_links(url, 21)
print('article links: ', len(links))

papers = []

for i, link in enumerate(links):
    # if link.find('Upfiles'):
    #     continue

    print('extract paper', i)

    title, author, content = page.parser(link, i)
    if title is not None and author is not None and content is not None:
        paper = {'title': title, 'author': author, 'content': content}
        papers.append(paper)

# json = json.dumps(papers, indent=4)

with open('../resource/wsszl.json', 'w', encoding='utf-8') as f:
    json.dump(papers, f, indent=4, ensure_ascii=False)
    f.close()

# for i, paper in enumerate(papers):
#     print('write paper', i)
#
#     path = "../resource/wsszl/" + str(i) + ".txt"
#     file = open(path, 'w', encoding='utf-8')
#     file.write(paper['title'])
#     file.write('\n')
#     file.write(paper['author'])
#     file.write('\n')
#     file.write(paper['content'])
#     file.close()

# print(json)

print('case number: ', len(papers))
print('end')
