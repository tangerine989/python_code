import os
import ssl
import requests
from bs4 import BeautifulSoup
import re
import json
from selenium.webdriver import Chrome
import time
from datetime import datetime

driver = Chrome('./chromedriver')
url = 'https://www.agoda.com/zh-tw/search?asq=Q6eYGMvEw0vwN5Y6vAd41PiwFzlbWptpE%2BmJqI80iVhu5wPVNnpsO0i3p6v5omYrukqLbqIfPKfWug0t%2F3DlXZNfP7XUG%2B%2BJ7P6stl%2F7v9SQjY5j6RU7NPthq2Z3TafKFCv9MDnRTnlC3HkKjGw3alYlQjNbMAZLSj4thObh0eUGnR6hESvbEtgeCqaTQijglKuOL4Nn8uSikeV%2BmYnN5uL2AUnfOhFRTEDVteJxPyI%3D&city=4951&cid=-218&tick=637171307556&languageId=20&userId=9228ee06-854a-4991-9fa2-1dc5504ccb07&sessionId=avyg3br0ufv0stagbgnwxuuk&pageTypeId=1&origin=TW&locale=zh-TW&aid=130589&currencyCode=TWD&htmlLanguage=zh-tw&cultureInfoName=zh-TW&ckuid=9228ee06-854a-4991-9fa2-1dc5504ccb07&prid=0&checkIn=2020-02-21&checkOut=2020-02-22&rooms=1&adults=2&children=0&priceCur=TWD&los=1&textToSearch=%E5%8F%B0%E5%8C%97%E5%B8%82&productType=-1&travellerType=1&familyMode=off'
driver.get(url)
time.sleep(2)
#driver.find_elements_by_class_name('InfoBox__HotelTitle').click()
driver.find_element_by_xpath("//h3[@class='InfoBox__HotelTitle']").click()

