import requests

string = str(input('请输入要翻译的文字: '))

data = {
    'doctype': 'json',
    'type': 'auto',
    'i': string
}

url = 'http://fanyi.youdao.com/translate'
r = requests.get(url, params=data)
print(r.json())
