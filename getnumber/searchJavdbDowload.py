from bs4 import BeautifulSoup
import re
import requests
import ssl
import time

# 解决请求https报错的问题
ssl._create_default_https_context = ssl._create_unverified_context


def javdbcookie():
    headers = {
        'authority': 'javdb365.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': 'i=z1PQa5TmbOAKoCV1YpHcsvGEmy+FLow0N4PSjS+FGcQZcLJMR7WJbAJaPkxCEHSVVlYTJHkduEBmWr9hQDO6c3lwcx4=; yandexuid=5478701451693998810; yabs-sid=443727641698054835; yuidss=5478701451693998810; ymex=2017031292.yrts.1701671292#2009358810.yrtsi.1693998810; yashr=2012744691712217271; bh=EkAiR29vZ2xlIENocm9tZSI7dj0iMTIzIiwgIk5vdDpBLUJyYW5kIjt2PSI4IiwgIkNocm9taXVtIjt2PSIxMjMiGgUiYXJtIiIQIjExOS4wLjYwNDUuMTk5IioCPzAyCSJOZXh1cyA1IjoHIm1hY09TIkIIIjE0LjEuMCJKBCI2NCJSXCJHb29nbGUgQ2hyb21lIjt2PSIxMTkuMC42MDQ1LjE5OSIsIkNocm9taXVtIjt2PSIxMTkuMC42MDQ1LjE5OSIsIk5vdD9BX0JyYW5kIjt2PSIyNC4wLjAuMCIi; receive-cookie-deprecation=1; bh=Ej4iR29vZ2xlIENocm9tZSI7dj0iMTIzIiwiTm90OkEtQnJhbmQiO3Y9IjgiLCJDaHJvbWl1bSI7dj0iMTIzIhoFImFybSIiECIxMjMuMC42MzEyLjEyMiIqAj8wMgkiTmV4dXMgNSI6ByJtYWNPUyJCCCIxNC40LjEiSgQiNjQiUlsiR29vZ2xlIENocm9tZSI7dj0iMTIzLjAuNjMxMi4xMjIiLCJOb3Q6QS1CcmFuZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMjMuMC42MzEyLjEyMiIi',
        'Referer': 'https://javdb365.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': 'macOS',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',

    }
    return headers
# https://javdb.com/search?q=test&f=all
def get_Javdb(keyword:str, sb, ifor, max:int, urls):
    headers = {
        'authority':'javdb.com',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie':'_ym_uid=1693998810306887787; list_mode=h; theme=auto; locale=zh; _ym_d=1712217273; _ym_isad=2; over18=1; _rucaptcha_session_id=9c0e5ca591240c1e36a61579d1b5f971; redirect_to=%2Fv%2FAzB61m; cf_clearance=vrxOkDvvyqRLlyL1Pdsrij7.4RvP9CjT9Uzf9aNoXxc-1712223713-1.0.1.1-Y22Bx3f_I7dRXGU3XhX3fhxudvkrKry1CGsEkahAELkjUDtB0aiwioDeT.7BdfxsJDK76sh3tXRzKMqnWHalLw; _jdb_session=CDADGPEZTZiPgY6lVvIJvbvZ60ITEzmC8FPfoVIgOOwVLIQtc%2BFHPPDTvGKZkbBY8r9WixHC9R9B412PMIDvFkDPVmzwJ%2FgZ0d24b6xfCeo6Fm23LU5mdOWuOLcxYWD1RLIdHs4A57oPfI5Dw65r9IIEf%2F1Cn1BFdI9BNJ5RgO9n5eSJeUQm501dfXZRXeMe08hXvaSfe5PzkOOXm5e5PZn59mXV5y%2B8YjYhvaxJZqj5L1tO28dipVrTX%2FIOVRdSPSZ%2FUp5s7EG%2Fv%2FX346qz53e14Up6FYMAX3aNLZVV6Fo%2FO8n%2BJA2XwwLIwy601YrTz7JyM3ygtAnYMXxX3oMWqjF0YkcwnLx84PpAVPlYYnzB2xAGAAzq9Q9A4kPq23zTBV%2FK270VymZ2CGidbeInOBD4--XFHJtyFA1vkebwHi--Fx1hXxiPryyMxoidLZL1sQ%3D%3D',
        'Referer':'https://javdb.com/',
        'Sec-Ch-Ua':'"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile':'?1',
        'Sec-Ch-Ua-Platform':'macOS',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',

    }
    # keyword = 'STARS-931'
    for i in range(1, max+1):
        if urls:
            page_url = urls + "?f=download&page={0}".format(i)
        else:
            page_url = 'https://javdb.com/search?f={0}&page={1}&q={2}&sb={3}'.format(ifor,i,keyword,sb)
        # page_url = "https://javdb.com/rankings/movies?p=monthly&t=western"
        print(page_url)

        response = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        movielist = []
        try:
            div = soup.find('div', {'class': 'movie-list h cols-4 vcols-8'})
            alist = div.find_all('a',{'class':'box'})

            for a in alist:

                url = 'https://javdb.com' + a['href']
                magnet = getDetailedInfo(url, headers)
                if magnet:
                    movielist.append(magnet)
            # movielist.append("关键字q:{0},第{1}页,搜索权重{2}".format(keyword,i,sb))
            writeFile(movielist)
        except Exception as e:
            print(e)
            print("That is the end!")
            writeFile(movielist)


def getDetailedInfo(url,headers):
    response = requests.get(url, headers=headers)
    time.sleep(0.3)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        div = soup.find('div', {'id': 'magnets-content'})
        a_list = div.find_all('a')
        pattern = r"无码流出"
        pattern2 = r"-UC"
        pattern3 = r"-C"
        pattern4 = r"无码破解"
        for _ in a_list:
            if _['href']:
                strs = _['href']
                if re.search(pattern4,strs):
                    return strs
                elif re.search(pattern,strs):
                    return strs
                elif re.search(pattern3,strs):
                    return strs
                elif re.search(pattern2,strs):
                    return strs
        if a_list[0]:
            return a_list[0]['href']
        else:
            return ''
    except Exception as e:
        print(e)

def writeFile(Javdblist):
    for javd in Javdblist:
        print(javd)
        if javd:
            with open(file_pathb, 'a+') as file:
                file.seek(0)
                existing_b = file.read().splitlines()
                if javd not in existing_b:
                    file.write(javd + '\n')

if __name__ == '__main__':
    file_pathb = "/Users/dension/job/avcd/Movie_Data_Capture/getnumber/xtl.txt"
    # sb = 1 按照时间
    url = None

    Javdblist = get_Javdb(keyword='无码',sb=1,ifor='download',max=20, urls=url)

