import sys
sys.path.append('../')

import html_base.get_html_content as html


def page(url):
    content = html.get_html_content(url)

    output = ''
    try:
        div = content.find('div', 'article')
        ps = div.find_all(['p'])

        for p in ps:
            for text in p.stripped_strings:
                output += text
            output += '\n'

            # elements = p.find_all(['span', 'br'], recursive=False)
            #
            # for element in elements:
            #     if temp != '':
            #         output += temp + '\n'
            #
            #     if element.name == 'br':
            #         temp = ''
            #         continue
            #     else:
            #         for text in element.stripped_strings:
            #             temp += text

    except:
        output = None

    return output


if __name__ == '__main__':
    # url = 'http://www.jingpinwenku.com/view/4e0be30d201e6a2d.html'
    url = 'http://www.jingpinwenku.com/view/47024aab3baca8d9.html'
    print(page(url))
