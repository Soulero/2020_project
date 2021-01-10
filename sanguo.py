# -*- coding= utf-8 -*-
# @Author : 余晓伟

import requests
from bs4 import BeautifulSoup
if __name__=="__main__":
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    url='https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text=requests.get(url=url,headers=header).text
    soup=BeautifulSoup(page_text,'lxml')
    li_list=soup.select('.book-mulu>ul>li')
    fp=open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title=li.a.string
        data_url='https://www.shicimingju.com'+li.a['href']
        data_text=requests.get(url=data_url,headers=header).text
        data_soup=BeautifulSoup(data_text,'lxml')
        div_tag=data_soup.find('div',class_='chapter_content')
        content=div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功！')






