# -*- coding= utf-8 -*-
# @Time : 2021/1/10 20:43
# @Author : 石皓翔
import requests
import os
from lxml import etree

if __name__=="__main__":
    url='http://pic.netbian.com/4kmeinv/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    res=requests.get(url=url,headers=header)
    #res.encoding='utf-8'
    page_text=res.text
    tree=etree.HTML(page_text)
    li_list=tree.xpath('//div[@class="slist"]/ul/li')
    if not os.path.exists('./piclib'):
        os.mkdir('./piclib')
    for li in li_list:
        img_src='http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        img_name=li.xpath('./a/img/@alt')[0]+'.jpg'
        img_name=img_name.encode('iso-8859-1').decode('gbk')
        img_data=requests.get(url=img_src,headers=header).content
        img_path='piclib/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'爬取成功！')


