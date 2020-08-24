# coding=utf-8
# Copyright (c) 2019  - Beijing Intelligent Star, Inc.  All rights reserved
"""
文件名：360kuai.py
功能：
代码历史：2020/8/24: 杜艺创
"""
import json

import requests
import execjs
import re


def js_fun(encrypt):
    decrypt = '''
            var s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
            u = String.fromCharCode
            o = function(e) {
                var t = {};
                for (var n = 0, r = e.length; n < r; n++)
                    t[e.charAt(n)] = n;
                return t
            }(s)
            b = function(e) {
                var t = e.length
                    , n = t % 4
                    , r = (t > 0 ? o[e.charAt(0)] << 18 : 0) | (t > 1 ? o[e.charAt(1)] << 12 : 0) | (t > 2 ? o[e.charAt(2)] << 6 : 0) | (t > 3 ? o[e.charAt(3)] : 0)
                    , i = [u(r >>> 16), u(r >>> 8 & 255), u(r & 255)];
                return i.length -= [0, 0, 2, 1][n],
                    i.join("")
            }
            m = new RegExp(["[A-B]"].join("|"),"g")
            g = function(e) {
                switch (e.length) {
                    case 4:
                        var t = (7 & e.charCodeAt(0)) << 18 | (63 & e.charCodeAt(1)) << 12 | (63 & e.charCodeAt(2)) << 6 | 63 & e.charCodeAt(3)
                            , n = t - 65536;
                        return u((n >>> 10) + 55296) + u((n & 1023) + 56320);
                    case 3:
                        return u((15 & e.charCodeAt(0)) << 12 | (63 & e.charCodeAt(1)) << 6 | 63 & e.charCodeAt(2));
                    default:
                        return u((31 & e.charCodeAt(0)) << 6 | 63 & e.charCodeAt(1))
                }
            }
            w =  function(e) {
                return e.replace(/[\s\S]{1,4}/g, b)
            }
            function y(e) {
                return e.replace(m, g)
            }
            function E(e) {
                return y(w(e))
            }
            function Base64_decode(e) {
                return E(String(e).replace(/[-_]/g, function(e) {
                    return e == "-" ? "+" : "/"
                }).replace(/[^A-Za-z0-9\+\/]/g, ""))
            }
            function detail(e) {
                var t = e.slice(0, 1e3).split("").map(function(e, t) {
                    return String.fromCharCode(e.charCodeAt() - t % 2)
                }).join("");
                return Base64_decode(t + e.slice(1e3))
            }
    ''' + '''var e = "%s"''' % encrypt
    com = execjs.compile(decrypt)
    text = com.call('detail', encrypt)
    return text


def get_detail(url):
    url = url
    text = requests.get(url).text
    try:
        encrypt = re.findall('window.__INITIAL_DATA__\s*?=\s*?[\"\']\\\n(.*?)[\"\']\;', text.replace('\\', ''))[0]
    except:
        return
    content = js_fun(encrypt)
    detail = json.loads(content)
    return detail


if __name__ == '__main__':
    url = 'https://www.360kuai.com/91b9e2f020240ab14'
    result = get_detail(url)
    print(result.get('result').get('Detail').get('title'))