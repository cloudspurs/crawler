import html_base.get_html_content as html
import page.page_wenku as page


def get_recommend_links(start_url):
    content = html.get_html_content(start_url, page_encoding='utf-8')
    div_recommend = content.find('div', 'page-recommend')
    all_a = div_recommend.find_all('a')
    home_recommend_links = []
    for a in all_a:
        home_recommend_links.append(a['href'])
    return home_recommend_links


def get_hot_links(content):
    div_hot = content.find('div', 'page-hot')
    all_a = div_hot.find_all('a')
    home_hot_links = []
    for a in all_a:
        home_hot_links.append(a['href'])
    return home_hot_links


def get_article_links(content):
    div_page = content.find('div', 'page-list')
    all_a = div_page.find_all('a')
    home_page_links = []
    for a in all_a:
        home_page_links.append(a['href'])
    return home_page_links


def get_article(link):
    try:
        article = page.page(link)
    except:
        print(link)
    return article


def get_home_article(home_links, all_home_url, all_article_url, path, i):
    for home_link in home_links:
        if home_link in all_home_url:
            continue
        home_page = html.get_html_content(home_link)
        article_links = get_article_links(home_page) + get_hot_links(home_page)
        for article_link in article_links:
            if article_link in all_article_url:
                continue
            else:
                all_article_url.append(article_link)
                article = get_article(article_link)
                result(article, path, str(i))
                print(i)
                i += 1
    return i


def result(article, path, i):
    try:
        path = "../resource/" + path + "/" + i + ".txt"
        with open(path, 'w', encoding='utf-8') as file:
            file.write(article)
            file.close()
    except TypeError as e:
        print(str(e))


if __name__ == "__main__":
    all_article_url = []
    all_home_url = []

    start_url = 'http://www.jingpinwenku.com/list/%E5%BE%B7%E8%82%B2%E6%A1%88%E4%BE%8B'

    home_links = get_recommend_links(start_url)

    i = 0
    i = get_home_article(home_links, all_home_url, all_article_url, 'wenku', i)

    try:
        for home_link in home_links:
            recommend_links = get_recommend_links(home_link)
            i = get_home_article(recommend_links, all_home_url, all_article_url, 'wenku', i)

            for recommend_link in recommend_links:
                srls = get_recommend_links(recommend_link)
                i = get_home_article(srls, all_home_url, all_article_url, 'wenku', i)

                for srl in srls:
                    frls = get_recommend_links(srl)
                    i = get_home_article(frls, all_home_url, all_article_url, 'wenku', i)

    except Exception as e:
        print(str(e))



