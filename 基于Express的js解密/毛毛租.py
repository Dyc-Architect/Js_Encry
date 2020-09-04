# coding=utf-8
# Copyright (c) 2019  - Beijing Intelligent Star, Inc.  All rights reserved
"""
文件名：毛毛租.py
功能：
代码历史：2020/9/4: 杜艺创
"""
import requests
url = 'https://www.maomaozu.com/index/index.json'
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}
data = {
    'payload': requests.get('http://127.0.0.1:3000/maomaozu')
}
data = {
    'data':requests.post(url=url,headers=headers,data=data).text
}
print(requests.post('http://127.0.0.1:3000/maomaozu/decrypt',data=data).text)