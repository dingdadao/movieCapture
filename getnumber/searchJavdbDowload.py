from bs4 import BeautifulSoup
import re
import requests
import ssl
import time

# 解决请求https报错的问题
ssl._create_default_https_context = ssl._create_unverified_context


def javdbcookie():
    headers = {
        'authority': 'javdb366.com',
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


"""


"""
def get_Javdb(keyword:str, sb, ifor, max:int, urls):
    headers = {
        'authority':'javdb366.com',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie':'i=z1PQa5TmbOAKoCV1YpHcsvGEmy+FLow0N4PSjS+FGcQZcLJMR7WJbAJaPkxCEHSVVlYTJHkduEBmWr9hQDO6c3lwcx4=; yandexuid=5478701451693998810; yabs-sid=443727641698054835; yuidss=5478701451693998810; ymex=2017031292.yrts.1701671292#2009358810.yrtsi.1693998810; yashr=2012744691712217271; receive-cookie-deprecation=1; bh=EkEiQ2hyb21pdW0iO3Y9IjEyNCIsICJHb29nbGUgQ2hyb21lIjt2PSIxMjQiLCAiTm90LUEuQnJhbmQiO3Y9Ijk5IhoFImFybSIiECIxMjQuMC42MzY3LjExOSIqAj8wMgkiTmV4dXMgNSI6ByJtYWNPUyJCCCIxNC40LjEiSgQiNjQiUlwiQ2hyb21pdW0iO3Y9IjEyNC4wLjYzNjcuMTE5IiwiR29vZ2xlIENocm9tZSI7dj0iMTI0LjAuNjM2Ny4xMTkiLCJOb3QtQS5CcmFuZCI7dj0iOTkuMC4wLjAiIg==; bh=Ej8iQ2hyb21pdW0iO3Y9IjEyNCIsIkdvb2dsZSBDaHJvbWUiO3Y9IjEyNCIsIk5vdC1BLkJyYW5kIjt2PSI5OSIaBSJhcm0iIhAiMTI0LjAuNjM2Ny4xMTkiKgI/MDIJIk5leHVzIDUiOgcibWFjT1MiQggiMTQuNC4xIkoEIjY0IlJcIkNocm9taXVtIjt2PSIxMjQuMC42MzY3LjExOSIsIkdvb2dsZSBDaHJvbWUiO3Y9IjEyNC4wLjYzNjcuMTE5IiwiTm90LUEuQnJhbmQiO3Y9Ijk5LjAuMC4wIiI=',
        'Referer':'https://javdb366.com/',
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

    for i in range(0, max):
        if urls:
            page_url = urls + "?f=download&page={0}".format(i+1)
        else:
            page_url = 'https://javdb366.com/search?f={0}&page={1}&q={2}&sb={3}'.format(ifor,i,keyword,sb)
        # page_url = "https://javdb.com/rankings/movies?p=monthly&t=western"
        # print(page_url)

        response = requests.get(page_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        movielist = []
        try:

            div = soup.find('div', {'class': 'movie-list h cols-4 vcols-8'})
            alist = div.find_all('a',{'class':'box'})

            for a in alist:

                url = 'https://javdb366.com' + a['href']
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
    # sb = 1 按照时间  ?f=download
    # https://javdb366.com/series/qJ4D
    # https://javdb366.com/video_codes/WAWA
    # url = "https://javdb366.com/video_codes/LUXU"
    # "https://javdb366.com/directors/pWB"3
    # "https://javdb366.com/directors/YnK"2
    # "https://javdb366.com/directors/4Dd6"1
    # "https://javdb366.com/video_codes/NSSTH"1

    url ="https://javdb366.com/series/4d0J"
    # url=None


    Javdblist = get_Javdb(keyword='sdnt',sb=1, ifor='download', max=2, urls=url)

