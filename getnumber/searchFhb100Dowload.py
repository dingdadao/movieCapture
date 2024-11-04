from bs4 import BeautifulSoup
import re
import requests
import ssl
import time

# 解决请求https报错的问题
ssl._create_default_https_context = ssl._create_unverified_context



"""


"""
def get_Javdb(q:str, max:int, urls):
    # keyword = 'STARS-931'
    sv_list = []
    for i in range(0, max):

        if urls:
            page_url = urls + "&page={0}".format(i+1)

        else:
            page_url= "https://www.fhb100.com/zh-cn/rsearch/go/?query={0}&page={1}".format(q, i)

        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)

        try:
            divs = soup.find_all('div', {'class': 'h-100 card'})

            for div in divs:
                alist = div.find_all('a')
                a = alist[0]['href']
                if a:
                    urla = "https://www.fhb100.com" + a
                    a = getDetailedInfo(urla)
                    sv_list.append(a)
            writeFile(sv_list)
            print(sv_list)

        except Exception as e:
            print("--------",e)
    time.sleep(15)

def getDetailedInfo(url):
    response = requests.get(url)
    time.sleep(0.3)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        div = soup.find('div', {'id': 'detail-main'})
        div = div.find_all('div',{'class': 'col-md-8 col-12'} )
        a = div[0].find('a')
        if a:
            return a["href"]
        else:
            print(url)
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
    # url ="https://www.fhb100.com/zh-cn/videos/hot/"
    # url="https://www.fhb100.com/zh-cn/rsearch/go/?query=%E6%AF%8D%E4%B9%B3"
    url = None
    query = 'ADN'


    Javdblist = get_Javdb(q=query, max=26, urls=url)

