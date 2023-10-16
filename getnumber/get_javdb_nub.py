from bs4 import BeautifulSoup
import re
import requests
import ssl
import time

#
# 解决请求https报错的问题
ssl._create_default_https_context = ssl._create_unverified_context



# https://javdb.com/search?q=test&f=all
def get_Javdb(keyword:str):
    headers = {
        'authority':'javdb.com',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie':'list_mode=h; theme=auto; locale=zh; _ym_uid=1693998810306887787; _ym_d=1693998810; _ym_isad=2; over18=1; cf_clearance=JHafX.GsDZwjorK0sJUGEyjBpG.kM6Rw1mWLRULCDnQ-1694054810-0-1-259c7f4f.5c5e812c.729d20af-0.2.1694054810; _jdb_session=rm8R6D9OS3Dm8tlL%2FdyyKP%2BouFfilRYa1a3q0hdt8mu1cQJTaSRrmWGubl18iLMRk3uKTe7o9EmakjcPWNTJxx%2F5nb2vASfDoJVy3BDbb%2Fx%2BfWoUCy9XU%2Be%2B9w13w9JtagzQjpvnkmMEMKmwgzeWLvUmlLgmO10FZ%2FpgPvTlw2NpOdC5bPvdrk5tTBE6BZyIWVz7%2BsFrhVWnGdkQj8iQgZfv4ocKfmskXh06OHs8KrQwuDW89nK8%2FqEOXYBSdaNpeslRmoyh8IlYUvrBBrV7UjpS5r29nSZgAA%2FTFybxaQLhMtHSjAhGRBXb--CAMgWzzjVMYqYEcC--vKuyThE4ti%2BnigZI4CyUTA%3D%3D',
        'Referer':'https://javdb.com/',
        'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'Sec-Ch-Ua-Mobile':'?1',
        'Sec-Ch-Ua-Platform':'Android',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',

    }
    # keyword = 'STARS-931'
    page_url = f'https://javdb.com/search?q={keyword}&f=all'

    response = requests.get(page_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    movielist = []
    try:
        body = soup.find('body', {'data-lang': 'zh'})
        section = body.find('section', {'class': 'section'})
        itemdiv = section.find_all('a', {'class': 'box'})
        for item in itemdiv:
            link = str(item['href'])
            if link:
                url =   "https://javdb.com" + link
                req = requests.get(url, headers=headers)
                soups = BeautifulSoup(req.text, 'html.parser')
                nub = getDetailedInfo(soups)
                if nub:
                    movielist.append(nub)
    except:
        print("That is the end!")
        return movielist

    return movielist


def getDetailedInfo(soup):
    body = soup.find('body', {'data-lang': 'zh'})
    container = body.find('div', {'class': 'item columns is-desktop odd'})
    a_list = container.find_all('a')
    pattern = r"无码流出"
    for _ in a_list:
        if _['href']:
            strs = _['href']
            if re.search(pattern,strs):
                return strs
    if a_list[0]:
        return a_list[0]['href']
    else:
        return ''

# def testar(magnet:str):
#     import json
#     from urllib.request import urlopen
#     jsonreq = json.dumps({'jsonrpc': '2.0',
#                           'method': 'aria2.addUri',
#                           "id": "QXJpYU5nXzE2OTQwNTM2MjlfMC4zMzI4NTkyMTM1NTQ4NDE4",
#                           'params': ["token:nidaye00",[magnet],{}],
#                           }).encode()
#     print(jsonreq)
#     c = urlopen('http://118.249.215.174:6800/jsonrpc', jsonreq)
#     return c











if __name__ == '__main__':
    # get_Javdb("p")
    #遍历数据
    # get_Nub()
    # get_github_Nub()

    file_patha = "/Users/dension/job/avcd/Movie_Data_Capture/getnumber/nub.txt"
    file_pathb = "/Users/dension/job/avcd/Movie_Data_Capture/getnumber/xtl.txt"

    with open(file_patha, 'r+') as files:
        files.seek(0)
        existing_strings = files.read().splitlines()
        try:
            for _ in existing_strings:
                time.sleep(6.5)
                Javdblist = get_Javdb(_)
                for javd in Javdblist:
                    print(javd)
                    if javd:
                        with open(file_pathb, 'a+') as file:
                            file.seek(0)
                            existing_b = file.read().splitlines()
                            if javd not in existing_b:
                                file.write(javd + '\n')

                existing_strings.remove(_)
                with open(file_patha, 'w') as filet:
                    for line in existing_strings:
                        filet.write(line + '\n')
        except:
            print("异常了")
            with open(file_patha, 'w') as filet:
                for line in existing_strings:
                    filet.write(line + '\n')




