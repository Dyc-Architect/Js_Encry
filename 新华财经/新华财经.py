# coding=utf-8
# Copyright (c) 2019  - Beijing Intelligent Star, Inc.  All rights reserved
"""
文件名：新华财经.py
功能：
代码历史：2020/8/24: 杜艺创
"""
import requests
import execjs


def get_hkey(id):
    js = ''
    with open(r'D:\dyc\JS\新华财经\xinhuacaijing.js', 'r') as r:
        js += r.read()
    js_content = execjs.compile(js)
    result = js_content.call('get_hkey_value', id)
    value, hkey = result.get('value'), result.get('hkey')
    get_data(hkey, value)


def get_data(hkey, value):
    url = 'https://bm.cnfic.com.cn/app-news/news/share/get'
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "hkey": hkey,
        "Host": "bm.cnfic.com.cn",
        "Origin": "https://bm.cnfic.com.cn",
        "Referer": "https://bm.cnfic.com.cn/share/index.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    }
    params = {
                 "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVSUQiOiI0YzkzMDA4NjE1YzJkMDQxZTMzZWJhYzYwNWQxNGI1YiIsInN1YiI6IkxPR0lOQVBJIiwiYXVkIjoiV2ViRnJvbnQiLCJpc3MiOiJVU0VSX0xPR0lOX1NFUlZJQ0UiLCJleHAiOjE1NTE3ODQ4NTAsImlhdCI6MTU1MTc3NzY1MH0=.AXdUBcNoU8CvrMtqYFhlHEgM11P-j70fBiNR-2AE_x0"
             }
    resp = requests.post(url=url, headers=headers, params=params, data=value).text
    get_real_data(resp,hkey)


def get_real_data(data,hkey):
    js = ''
    with open(r'D:\dyc\JS\新华财经\xinhuacaijing.js', 'r') as r:
        js += r.read()
    js_content = execjs.compile(js)
    result = js_content.call('dencrypt', str(data), str(hkey))
    print(result)


if __name__ == '__main__':
    get_hkey(1994422)
