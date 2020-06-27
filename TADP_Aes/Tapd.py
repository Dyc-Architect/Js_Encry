import json

import execjs
import requests

def get_data(content):
    with open('Tapd.js',"r", encoding='utf8') as f:
        ctx = execjs.compile(f.read())
        data = json.loads(ctx.call("aes", content))
        return data

def login(content):
    url = 'https://www.tapd.cn/cloud_logins/login'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36',
    }
    datas = get_data(content)
    print(datas)
    data = {
        'data[Login][ref]': 'https://www.tapd.cn/my_worktable',
        'data[Login][encrypt_key]': datas.get('encrypt_key'),
        'data[Login][encrypt_iv]': datas.get('encrypt_iv'),
        'data[Login][site]': 'TADP_Aes',
        'data[Login][via]': 'encrypt_password',
        'data[Login][email]': '15596870128',
        'data[Login][password]': datas.get('password'),
        'data[Login][login]': 'login',
        'dsc_token': datas.get('dsc_token')
    }
    text = requests.post(url=url, data=data, headers=headers).text
    return text

if __name__ == '__main__':
    content = '111111'
    login(content)