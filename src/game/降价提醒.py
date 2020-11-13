"""
爬取京东商品价格，降价桌面右下角提醒通知
"""
import time
import random
from bs4 import BeautifulSoup
from plyer import notification
from selenium.webdriver import Chrome, ChromeOptions


def get_price(url):
    options = ChromeOptions()
    options.add_argument("headless")
    d = Chrome(options=options)
    d.get(url)
    soup = BeautifulSoup(d.page_source, "html.parser")
    d.close()
    price = float(soup.find("span", class_="price J-p-100016034394").text)
    return price


while True:
    price = get_price("https://item.jd.com/100016034394.html")
    print(price)
    if price <= 7000:
        notification.notify(
            title="降价提醒",
            message="买！买！买！！！",
            app_icon="cart.ico",
            timeout=10
        )
        break
    time.sleep(random.randint(30, 60))
