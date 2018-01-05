#! /user/bin/python3

import requests
from bs4 import BeautifulSoup
import sqlite3
from prettytable import from_db_cursor
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
conn=sqlite3.connect("savedata.db")
c=conn.cursor()
c.execute("create table savedata(count,author,content)")
for i in range(len(name)):
    tmp=i+1
    t_name=name[i].get_text().replace("\n","")
    t_content=content[i].get_text().lstrip()
    c.execute("insert into savedata values (%d,'%s','%s')"%(tmp,t_name,t_content))
c.execute("select * from savedata")
pt=from_db_cursor(c)
result=pt.get_html_string(header=False,align="1")
t=open("result_1.html",'w')
t.write('标题：'+title.get_text()+'<hr/>'+'作者：'+author.attrs['author']+'<hr/>'+result)
t.close()
c.close()
conn.close()