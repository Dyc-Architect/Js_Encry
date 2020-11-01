# -*- coding: utf-8 -*-
# @Time: 2020/10/31 17:27
# @Author: dyc
# @File: zhuge.py
import re

import requests


def cookie(arg1):
    arg1 = arg1
    _0x20a7bf = 0
    _0x4b082b = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6, 11, 39, 18, 20, 8, 14, 21, 32,
                 26, 2, 30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36]
    _0x4da0dc = ['', '', '', '', '', '', '4', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '', 'A', '', '', '', '', '', '', 'F', '', '', '', '', '', '']
    _0x12605e = ""
    while _0x20a7bf < len(arg1):

        _0x385ee3 = arg1[_0x20a7bf]
        _0x217721 = 0
        while _0x217721 < len(_0x4b082b):
            if _0x4b082b[_0x217721] == _0x20a7bf + 1:
                _0x4da0dc[_0x217721] = _0x385ee3
            _0x217721 += 1
        _0x20a7bf += 1

    _0x12605e = "".join(_0x4da0dc)
    _0x23a392 = _0x12605e
    _0x4e08d8 = "3000176000856006061501533003690027800375"
    _0x5a5d3b = ""
    _0xe89588 = 0
    while _0xe89588 < len(_0x23a392) and _0xe89588 < len(_0x4e08d8):
        _0x401af1 = int(_0x23a392[_0xe89588:_0xe89588 + 2], 16)
        _0x105f59 = int(_0x4e08d8[_0xe89588:_0xe89588 + 2], 16)
        _0x189e2c = hex((_0x401af1 ^ _0x105f59))
        if len(_0x189e2c) == 3:
            _0x189e2c = "0" + _0x189e2c
        _0x5a5d3b += _0x189e2c
        _0xe89588 += 2
    return _0x5a5d3b.replace('0x','')


def run():
    url = 'http://news.zhuge.com/bj/'

    resp = requests.get(url=url).text
    arg1 = re.findall('arg1\s*?\=\s*?[\"\'](\S*?)[\"\']', resp)[0]
    headers = {
        'cookie' : 'acw_sc__v2=' + cookie(arg1) +';'
    }
    resp = requests.get(url=url,headers=headers).text
    return resp

if __name__ == '__main__':
    print(run())