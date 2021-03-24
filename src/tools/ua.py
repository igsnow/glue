import requests
import re

s = requests.Session()

response = s.get('https://sellercenter.lazada.co.th/apps/seller/login')

print(response.text)
st_match = re.search(r'"umidToken":"(.*?)"', response.text)
print(st_match)
