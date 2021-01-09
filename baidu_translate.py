# -*- coding= utf-8 -*-
# @Time : 2021/1/9 17:06
# @Author : 张清泉

import requests
import json

if __name__=="__main__":
    url='https://fanyi.baidu.com/sug'
    word=input('input a word that you want to translate:')
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    data={
        'kw':word
    }
    res=requests.post(url=url,data=data,headers=header)
    data1_json=res.json()
    fname=word+'.json'
    fp=open(fname,'w',encoding='utf-8')
    json.dump(data1_json,fp=fp,ensure_ascii=False)
    print("translate successfully!!!")




