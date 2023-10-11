import re
import time

import requests

from bs4 import BeautifulSoup
def write_unique_strings_to_file(strings):
    print(strings)
    file_path = "/getnumber/nub.txt"
    with open(file_path, 'a+') as file:
        file.seek(0)
        existing_strings = file.read().splitlines()
        if strings not in existing_strings:
            file.write(strings + '\n')


def get_nub(movielist:list):
    for _ in movielist:
        html = requests.get(_)
        soup = BeautifulSoup(html.text, 'html.parser')
        body = soup.find('body')
        pattern = r'[A-Za-z0-9-]{2,6}[ -]\d{3,4}'
        for i in body.find_all("p"):
            match = re.search(pattern, str(i))
            if match:
                write_unique_strings_to_file(match.group())




def get_html():
    # "/jipinfanhao/index_2.html"
    url = "https://www.xxfanhao.net/jipinfanhao/"

    for i in range(151,200):
        if i != 1:
            time.sleep(3.5)
            url = "https://www.xxfanhao.net/jipinfanhao/index_{0}.html".format(i)

        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        body = soup.find('body')
        div = body.find('div', {'class': 'wrap mt120'})
        a_list = div.find_all('a')

        for _ in a_list:
            movielist = []
            try:
                if _['href']:
                    strs = _['href']
                    strslist = strs.split(".")
                    if strslist[1] == "html":
                        nublist = strs.split("/")
                        nub = nublist[2].split(".")
                        if nub[0].isdigit():
                            movielist.append("https://www.xxfanhao.net"+strs)
            except:
                pass
            if movielist:
                get_nub(movielist)

    # return movielist

if __name__ == '__main__':
    get_html()