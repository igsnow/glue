import pandas as pd

df = pd.read_excel('../../static/refund.xls')
data = df.head(10)  # 默认获取前5行数据
print("获取到的值：\n{0}".format(data))
