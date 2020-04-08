import os
import ssl
import requests
from bs4 import BeautifulSoup
import re
import json

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
ss = requests.session()
ss.cookies['over18'] = '1'

resource_path = r'D:\專題\ptt_food'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

url = 'https://www.ptt.cc/bbs/Food/search?q=%E9%A3%9F%E8%A8%98'
n = 2000   #2000頁 (每日約更新2~3頁，可設定 n=5 抓取最新資料)
for i in range(0,n):
    res = ss.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    article_title_html = soup.select('div[class="title"]')


    for each_article in article_title_html:
        try:
            tmp = re.match('.*(台北|新北|基隆|桃園|新竹|宜蘭).*',each_article.text.lstrip().rstrip())
            #tmp = re.match('.*(台北).*', each_article.text.lstrip().rstrip()) #自行代換其他縣市
            print(tmp.group(0))
            print('https://www.ptt.cc' + each_article.a['href'])

            article_url = 'https://www.ptt.cc' + each_article.a['href']
            article_text = tmp.group(0)
            #article_text = each_article.a.text
            article_res = ss.get(article_url, headers=headers)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')

            author = ''
            title = ''
            datetime = ''
            try:
                article_content = '餐廳名稱' + article_soup.select('div#main-content')[0].text.split('餐廳名稱')[1]
                #article_content = article_soup.select('div[id="main-content"]')
                article_info_list = article_soup.select('div[class="article-metaline"] span')
                article_name = re.search(r'.*餐廳名稱：*(.*)',article_content).group(1)
                article_address = re.search(r'.*地址：[0-9]*(.*)',article_content).group(1)
                article_county = re.search(r'.*地址：[0-9]*.*?(台北市|新北市|基隆市|桃園市|新竹縣|宜蘭縣)',article_content).group(1)
                #article_county = re.search(r'.*地址：[0-9]*(.*(台北市))', article_content).group(1) #自行代換其他縣市
                for n, info in enumerate(article_info_list):
                    if (n+1)%6 == 2:
                        author = info.text
                    if (n+1)%6 == 4:
                        title = info.text
                    if (n+1)%6 == 0:
                        datetime = info.text
                '''
                (json檔案格式)
                美食欄位:
                {
                "文章網址": "",
                "發文時間": "",
                "標題": "",
                "餐廳名稱": "",
                "美食名稱": ["" ,"",.....], 
                "文章內容": "",  
                "留言": ["" ,"",.....],
                "地址": "", 
                "縣市": "",
                 }
                '''
                #article_content += '\n---split---\n'
                #article_content += '作者: %s\n'%(author)
                #article_content += '標題: %s\n'%(title)
                #article_content += '時間: %s\n'%(datetime)
                article_json = {
                "文章網址": article_url,
                "發文時間": datetime,
                "標題": title,
                "餐廳名稱": article_name,
                "美食名稱": "NA",
                "文章內容": article_content,
                "留言": "NA",
                "地址": article_address,
                "縣市": article_county,
                 }
                acticle_js = json.dumps(article_json, ensure_ascii=False,indent=1)
                if not os.path.exists(resource_path + '\\' + article_county):
                    os.mkdir(resource_path + '\\' + article_county)
                with open(r'%s/%s.json' % (resource_path + '\\' + article_county, article_text), 'w', encoding='utf-8') as w:
                    w.write(acticle_js)
                print()
            except FileNotFoundError as e:
                print('==========')
                print(article_url)
                print(e.args)
                print('==========')
            except :
                print('==========')
                print('other false')
                print('==========')
        except AttributeError as e:
            print('==========')
            print(each_article)
            print(e.args)
            print('==========')

    url = 'https://www.ptt.cc' + soup.select('div[class="btn-group btn-group-paging"]')[0].select('a')[1]['href']