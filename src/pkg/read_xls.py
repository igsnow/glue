import pandas as pd

# 读取数据
cols_data = pd.read_excel('../../static/special_rate .xlsx', usecols=[1])
cols_list = cols_data.values.tolist()

# 写入文件
with open('thcode.txt', 'w') as f:
    for i in cols_list:
        f.write("'" + i[0] + "',\n")
