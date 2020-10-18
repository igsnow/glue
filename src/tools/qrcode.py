# 生成普通二维码
from MyQR import myqr

myqr.run(words='https://www.baidu.com')

# 生成带图片的二维码
myqr.run(words='https://www.baidu.com', picture='money.jpg', colorized=True)
