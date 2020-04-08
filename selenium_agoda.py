from selenium.webdriver import Chrome
import time
import requests
import lxml
from datetime import datetime

driver = Chrome('./chromedriver')

#url = 'https://www.agoda.com/zh-tw/'
url = 'https://www.agoda.com/zh-tw/search?asq=Q6eYGMvEw0vwN5Y6vAd41PiwFzlbWptpE%2BmJqI80iVhu5wPVNnpsO0i3p6v5omYrukqLbqIfPKfWug0t%2F3DlXZNfP7XUG%2B%2BJ7P6stl%2F7v9SQjY5j6RU7NPthq2Z3TafKFCv9MDnRTnlC3HkKjGw3alYlQjNbMAZLSj4thObh0eUGnR6hESvbEtgeCqaTQijglKuOL4Nn8uSikeV%2BmYnN5uL2AUnfOhFRTEDVteJxPyI%3D&city=4951&cid=-218&tick=637171307556&languageId=20&userId=9228ee06-854a-4991-9fa2-1dc5504ccb07&sessionId=avyg3br0ufv0stagbgnwxuuk&pageTypeId=1&origin=TW&locale=zh-TW&aid=130589&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=9228ee06-854a-4991-9fa2-1dc5504ccb07&prid=0&checkIn=2020-02-21&checkOut=2020-02-22&rooms=1&adults=2&children=0&priceCur=TWD&los=1&textToSearch=%E5%8F%B0%E5%8C%97%E5%B8%82&productType=-1&travellerType=1&familyMode=off'

driver.get(url)
'''
time.sleep(2)
driver.find_elements_by_class_name('PillDropdown')[2].click()  #進入星級評等
time.sleep(1)
driver.find_elements_by_class_name('filter-item-react')[0].click() #選擇五星級
time.sleep(1)
driver.find_elements_by_class_name('filter-item-react')[1].click() #選擇四星級
time.sleep(1)
driver.find_elements_by_class_name('PillDropdown')[1].click()  #進入價格
time.sleep(1)
driver.find_element_by_xpath("//input[@id='price_box_1']").click()
driver.find_element_by_xpath("//input[@id='price_box_0']").send_keys(1000) #最低價 key 1000
time.sleep(1)
driver.find_element_by_xpath("//input[@id='price_box_1']").click()
driver.find_element_by_xpath("//input[@id='price_box_1']").send_keys(3000) #最高價 key 3000
#time.sleep(1)
#driver.find_element_by_class_name('btn.Searchbox__searchButton.Searchbox__searchButton--active').click() #搜尋
'''

#滾動到最底部
js1 = 'return document.body.scrollHeight'
js2 = 'window.scrollTo(0, document.body.scrollHeight)'
old_scroll_height = 0
count = 0
n = 20
for i in range(0,n):
    #while driver.execute_script(js1) >= old_scroll_height:
    a = datetime.now()
    while True:
        old_scroll_height = driver.execute_script(js1)
        driver.execute_script(js2)
        time.sleep(1)
        count = count + 1
        print(count)
        print(datetime.now())
        if (datetime.now() - a).seconds > 5 :
            break
    #time.sleep(5)
    try:
        driver.find_element_by_id('paginationNext').click()
    except FileNotFoundError as e:
        print('沒有下一頁了')
        print(e.args)
    except :
        print('錯誤')

