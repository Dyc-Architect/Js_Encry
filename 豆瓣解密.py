# -*- coding: utf-8 -*-
# @Time: 2020/10/24 22:15
# @Author: dyc
# @File: 豆瓣解密.py
import base64
import time
from hashlib import sha1
import hmac

import requests


def encrypt():
    timestamp = str(1603592059)
    key = 'bf7dddc7c9cfe6f7'
    encrypt_data = 'GET&%2Fapi%2Fv2%2Fgroup%2Frec_groups_by_tag&{}'.format(timestamp)
    key = bytearray(key, encoding='utf-8')
    encrypt_data = bytearray(encrypt_data, encoding='utf-8')
    hmac_code = hmac.new(key, encrypt_data, sha1)
    code = hmac_code.digest()
    _sig = base64.encodestring(code).decode('utf-8')
    return _sig,timestamp

def get_resp():
    url = 'https://frodo.douban.com/api/v2/group/rec_groups_by_tag'
    print(url)
    headers = {
        'User-Agent':'api-client/1 com.douban.frodo/6.42.2(194) Android/22 product/shamu vendor/OPPO model/OPPO R11 Plus  rom/android  network/wifi  platform/mobile nd/1'
    }
    params = {
        'start':'30',
        'count':'30',
        'tag':'新组',
        'apikey':'0dad551ec0f84ed02907ff5c42e8ec70',
        '_sig':encrypt()[0].replace('\n',''),
        '_ts':encrypt()[1],
        'os_rom':'android',
        'channel':'Huawei_Market',
        'udid':'cfc0ae8eb4c6e304bb9ebc9e03164dd9040ff483',
    }
    resp = requests.get(url=url,headers=headers,params=params).text
    return resp
if __name__ == '__main__':
    print(get_resp())