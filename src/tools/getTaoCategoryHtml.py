import requests

url = 'https://zanfood.taobao.com/i/asynSearch.htm?mid=w-3067782975-0&wid=3067782975&path=/category-1522839476.htm&spm=2013.1.w4010-3067782969.8.680f732b78IAzf&search=y&categoryp=50010535&pidvid=20000%3A110445&scid=1522839476&catId=1522839476'
cookie_str = 'cna=bNDlFzRlJAQCATy63mxZJquE;lgc=zzy%5Cu6D6A%5Cu6DD8%5Cu6C99;tracknick=zzy%5Cu6D6A%5Cu6DD8%5Cu6C99;enc=LGQAApxylhoYV5EFeN%2FNQwQ5JLOflAnCG9r79L%2B7V5FDfkOsijOU%2Bw9UaitN24Pg9PL7qG3KQoDd8sTTXR8b9g%3D%3D;thw=cn;miid=844834271709185731;t=b346f0b736e697fa442a754537609956;mt=ci=5_1;_m_h5_tk=7560ff9dd2c5d223323f1f75497c6d85_1603196953436;_m_h5_tk_enc=05dd820c70677c5c12e12ba3450e1aa0;cookie2=73da4b0bf0a282004abef9249a22e593;_samesite_flag_=true;v=0;googtrans=/auto/zh-CN;sgcookie=E100G9iM%2BekbOTLmtHN%2FYcyx9jLHREyXYkBKkGS2bg5%2FpEn6eJb52RPxFzZdYq9OJFIr7mnAbpxr6Ebr3q%2B71v4SAw%3D%3D;unb=459950953;uc1=cookie14=Uoe0bktB1aH4hA%3D%3D&cookie21=VFC%2FuZ9ajCWYhIoorx%2BBOA%3D%3D&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&pas=0&existShop=false;uc3=id2=VynA2wkbmrHm&vt3=F8dCufHJk9MSqJ2dbPw%3D&nk2=GdImNHNmBRQC&lg2=Vq8l%2BKCLz3%2F65A%3D%3D;csg=f64f2dfe;cookie17=VynA2wkbmrHm;dnk=zzy%5Cu6D6A%5Cu6DD8%5Cu6C99;skt=f466023bf40549a3;existShop=MTYwMzI0Nzg5Nw%3D%3D;uc4=nk4=0%40Gxs1IfDgbX6BnZpQDqa0Z3C5Du0%3D&id4=0%40VX5ArP2FqcYAowlztwNnrlYTDKo%3D;_cc_=Vq8l%2BKCLiw%3D%3D;_l_g_=Ug%3D%3D;sg=%E6%B2%9931;_nk_=zzy%5Cu6D6A%5Cu6DD8%5Cu6C99;cookie1=VFc0fDLipfnVKJF7stRrnDDc0dH9kRmNiWCtW5tKExk%3D;_tb_token_=f37e3bb13ee5;pnm_cku822=098%23E1hvCQvUvbpvUvCkvvvvvjiWP2MUljEHR2SwsjD2PmPOzjrPRFMZ1j3EnLLZ6jYj29hvCvvvMM%2FgvpvIS6vvivvvByavpv1vvvC2yyCvjvUvvhBGphvwv9vvBj1vpCstvvChwu9Cvv3vpvLxiH6neg9CvvXmp99hjC%2BUvpCWpO%2FPv8RwjLW%2BofeaRFB%2BmB%2Buzj7JDox%2FwZCl%2Bb8rwZvaUWmQ%2Bul1oC69D70OVC6sbhet5LI6fvxYoaLhe1O07oDn9Wma%2BoHoEpchTvvCvvXvppvvvvvgvpvhphvvv8OCvvBvpvpZ;isg=BAIC-RDu6VIlIvVfnnCcC5OcUwhk0wbtL8gBckwbLnUgn6IZNGNW_YjfT5vj1H6F;l=eBOV_p4POzAfBhpCBOfanurza77OSIRYYuPzaNbMiOCPOgfB5auhWZ53ghL6C3GVhsOMR3-wPvU8BeYBqQOSnxvtvEyssfDmn;tfstk=cK61B9sOqV0_BePqQGZeb1V-TIvAwSmWc5TGf1e6mCY6wU1c2Y8WYcfmkvdJA'

cookies = {}
cookie_arr = cookie_str.split(';')

for i in cookie_arr:
    name, value = i.split('=', 1)
    cookies[name] = value

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

res = requests.get(url, headers=headers, cookies=cookies)
print(res.content)

with open('taobao.txt', 'w') as f:
    f.write(f'{res.content}')
