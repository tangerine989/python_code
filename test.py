import re

article_content = '''
   餐廳名稱：La maison 蛋糕工作室
   消費時間：2013年/1月
   地址：153台中縣東區進德路154號
   電話：0927-101-595
   營業時間：PM12:00~PM9:00 周日公休
   推薦菜色：修格拉巧克力
'''
#print(type(article_content))
#t = re.search(r'.*地址：[0-9]*(.*)',article_content)
#print(t.group(1))

#t = re.search(r'.*地址：[0-9]*(.*(市|縣))',article_content)
#print(t.group(1))

county_list = ['台北','新北','基隆','桃園','新竹','宜蘭']
for i in county_list:
    print(i)