#! /user/bin/python3

import requests
from bs4 import BeautifulSoup
import sqlite3
tmp=0
t_name=0
t_content=0
data=requests.get("http://tieba.baidu.com/p/4366651917")
data.encoding="UTF-8"
soup=BeautifulSoup(data.text,'lxml')
title=soup.find('h1',class_="core_title_txt")
author=soup.find('div',class_="louzhubiaoshi",attrs={'author':True})
name=soup.find_all('li',class_="d_name")
content=soup.find_all('div',class_="d_post_content")
print(title.get_text())
print(author.attrs['author'])
conn=sqlite3.connect("savedata.db")
c=conn.cursor()
c.execute("create table savedata(count,author,content)")
for i in range(len(name)):
    tmp=i+1
    t_name=name[i].get_text().replace("\n","")
    t_content=content[i].get_text().lstrip()
    c.execute("insert into savedata values (%d,'%s','%s')"%(tmp,t_name,t_content))
c.execute("select * from savedata")
result=c.fetchall()
print(result)
c.close()
conn.close()