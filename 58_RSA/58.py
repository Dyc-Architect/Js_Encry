import json
import re
import time
import pytesseract
import execjs
import requests
import base64
from chaojiying import *


def get_pwd(userpwd):
    with open('58Rsa.js', "r", encoding='utf8') as f:
        ctx = execjs.compile(f.read())
        data = ctx.call("encryptString", userpwd)
    return data


def do_login(username,userpwd):
    global session,headers
    session = requests.session()

    url = 'https://passport.58.com/58/login/pc/dologin'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        'referer': 'https://passport.58.com/login/?path=https%3A//hz.58.com/searchjob/%3Fspm%3D116138685575.zhaopin_baidu%26utm_source%3D12345&PGTID=0d302409-0004-f026-99d0-d5d7983ad769&ClickID=5',
    }

    data = {
        'username': username,
        'password': get_pwd(userpwd),
        'finger2': 'zh-CN|24|1|4|1366_768|1366_737|-480|1|1|1|undefined|1|unknown|Win32|unknown|3|false|false|false|false|false|0_false_false|d41d8cd98f00b204e9800998ecf8427e|9d76d5d4912068e5bb68f6c511006265',
    }
    text = session.post(url=url,headers=headers,data=data).text
    return get_captcha(text)


def get_captcha(text):
    vcodekey = re.findall('vcodekey[\"\']\s*?\:\s*?[\"\'](\S*?)[\"\']',text)[0]
    url = 'https://passport.58.com/sec/58/validcode/get?vcodekey=%stime=%s'%(vcodekey,str(int(time.time()*1000)))
    text = session.get(url=url)
    with open('captcha.jpg','wb',) as f:
        f.write(text.content)
    # 百度接口识别图片
    # baidu_deal_img()
    # 超级鹰验证码平台接口识别
    deal_captcha = Chaojiying_Client('*********','*********','*******')
    img = open('captcha.jpg', 'rb').read()
    code = deal_captcha.PostPic(img, 1902)
    print(code)

def baidu_deal_img():
    '''
    百度接口识别图片，实验不可行
    '''
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=9GCNhraYwiXT2Avez3M496vl&client_secret=jun7bH9NRU1TqnMyqlwfHZs8CUW0hHC8'
    response = requests.get(host).json()
    # if response:
    #     print(response)
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage"
    # 二进制方式打开图片文件
    f = open('captcha.jpg', 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    access_token = response.get('access_token')
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
    return response


if __name__ == '__main__':
    username = '15596870128'
    userpwd = '123qweasd'
    print(do_login(username, userpwd))
