# import page
import page_1 as page
import json

# title, author, content = page.parser('http://www.seewww.cn/deyufangfa/edu396984.html')
# title, author, content = page.parser('http://www.jsyzyz.com/Upfiles/Downs/2015-1/201511516354921683.doc', 1)
# title, author, content = page.parser('http://www.jsyzyz.com/Show.asp?id=150571', 1)
#
# print(title)
# print(author)
# print(content)

papers = []

with open('wsszl.json', 'r', encoding='utf-8') as f:
    papers = json.load(f)
    print(len(papers))

for i, paper in enumerate(papers):
    path = "../resource/wsszl/" + str(i) + ".txt"
    file = open(path, 'w', encoding='utf-8')
    file.write(paper['title'])
    file.write('\n')
    file.write(paper['author'])
    file.write('\n')
    file.write(paper['content'])
    file.write('\n')
    file.close()
