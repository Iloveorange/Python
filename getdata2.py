#! /user/bin/python3

import requests
from bs4 import BeautifulSoup
data=requests.get("http://tieba.baidu.com/p/4366651917")
data.encoding="UTF-8"
soup=BeautifulSoup(data.text,'lxml')
name=soup.find_all('li',class_='d_name')
content=soup.find_all('div',class_="d_post_content")
tmp=1
for i in range(len(name)):
   print (tmp)
   print(name[i].get_text())
   print(content[i].get_text())
   tmp+=1
