import os
import ssl
import requests
from bs4 import BeautifulSoup
import re
import json
import time

#driver = Chrome('./chromedriver')

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
ss = requests.session()

resource_path = r'D:\專題\taiwan'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

for url in ["https://okgo.tw/buty/taipei.html","https://okgo.tw/buty/keelung.html",
            "https://okgo.tw/buty/taoyuan.html","https://okgo.tw/buty/hsinchu.html","https://okgo.tw/buty/yilan.html"]:
    short_url = url.split("https://okgo.tw/")[1]
    res = ss.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    article_title_html = soup.select('li[style="height:auto !important;overflow:auto;"]')

    def cleancontent(m):
        m = re.sub(r'<a.*?(">)', '', m)
        m = re.sub(r'</a>', '', m)
        m = re.sub(r'<br>', '', m)
        m = re.sub(r'</br>', '', m)
        m = re.sub(r'<div>', '', m)
        return m


    for each_article in article_title_html:
        try :
            b = each_article.a.get('href').split('/')[1]
            article_url = "https://okgo.tw/" + str(b)
            article_name = each_article.h2.string
            article_res = ss.get(article_url, headers=headers)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')
            article_page = article_soup.select('div.sec3.word.Resize')
            #print(article_page)
            article_content = str(article_page).split("<div>",1)[1].split("</div>")[0]
            #article_content = article_content.replace(r'.*<a.*">','').replace(r'</a>','')
            article_content = cleancontent(article_content)
            #print(article_content)
            #print(str(article_page).split())
            condition_1 = str(article_page).split("電話：")[1].split("<br>")[0]
            if condition_1 == '-':
                article_phone = 'NA'
            else :
                article_phone = condition_1
            #print(article_phone)
            condition_2 = str(article_page).split("地址：")[1].split("<br>")[0]
            if condition_2 == '-':
                article_address = 'NA'
            else :
                article_address = condition_2
            #print(article_address)
            article_county = article_soup.select('strong')
            article_county = str(article_county).split(short_url+'">')[1].split('</a>')[0]

            print('==============')
            print(article_county)
            print(each_article.h2.string)
            print("https://okgo.tw/"+ str(b))

        except :
            print("==========")
            print("Oops!error")
            print("==========")

        article_json = {
            "文章網址": article_url,
            "發文時間": 'NA',
            "標題": article_name,
            "景點名稱": article_name,
            "文章內容": article_content,
            "留言": "NA",
            "地址": article_address,
            "縣市": article_county,
        }
        acticle_js = json.dumps(article_json, ensure_ascii=False,indent=1)

        try:
            if not os.path.exists(resource_path + '\\' + article_county):
                os.mkdir(resource_path + '\\' + article_county)
            with open(r'%s/%s.json' % (resource_path + '\\' + article_county, article_name), 'w', encoding='utf-8') as w:
                w.write(acticle_js)
        except:
            print("==========")
            print("Oops!error")
            print("==========")

        #print(acticle_js)

    print(article_county+" complete")

print("totally complete")


