import yagmail

# 连接邮箱服务器    邮箱授权码还在修改手机号，waiting...
yag = yagmail.SMTP(user='zzy3882629@126.com', password='zzy18796729065@', host='smtp.126.com')
# 邮箱正文
contents = ['this is a eamil from python']
# 发送邮件
yag.send('716810918@qq.com', 'subject', contents)
