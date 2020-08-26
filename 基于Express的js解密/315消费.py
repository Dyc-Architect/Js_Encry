# coding=utf-8
# Copyright (c) 2019  - Beijing Intelligent Star, Inc.  All rights reserved
"""
文件名：315消费.py
功能：
代码历史：2020/8/25: 杜艺创
"""
import requests

def get_data():
    result = requests.get(url='http://127.0.0.1:3000/315').json()
    code = result.get('code')
    data = {
        'code':code
    }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '727',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'api2.xfb315.com',
        'Origin': 'https://www.xfb315.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.xfb315.com/tousu',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'source': 'pc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    }
    url = 'https://api2.xfb315.com/v6.5.1/tousu_list'
    resp = requests.post(url=url,data=data,headers=headers).json()
    print(resp.get('data'))


if __name__ == '__main__':
    get_data()