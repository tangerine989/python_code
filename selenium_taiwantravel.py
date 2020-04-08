from selenium.webdriver import Chrome
import time

driver = Chrome('./chromedriver')

url = 'https://okgo.tw/buty/taipei.html'

driver.get(url)
time.sleep(1)
#driver.find_element_by_xpath("/html/body/form/div[2]/div[1]/div[0]/div[4]/div[0]/div[2]/ul/")
#driver.find_elements_by_class_name('tooptip')[0].click()
driver.find_element_by_xpath("//span[@class='tooltip'][1]").click()
