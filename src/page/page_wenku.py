import sys
sys.path.append('../')

import html_base.get_html_content as html


def page(url):
    try:
        content = html.get_html_content(url)

        output = ''
        div = content.find('div', 'article')
        ps = div.find_all(['p'])

        for p in ps:
            for text in p.stripped_strings:
                output += text
            output += '\n'
    except:
        output = None

    return output


if __name__ == '__main__':
    # u = 'http://www.jingpinwenku.com/view/4e0be30d201e6a2d.html'
    u = 'http://www.jingpinwenku.com/view/47024aab3baca8d9.html'
    print(page(u))
