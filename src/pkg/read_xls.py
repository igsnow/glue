import pandas as pd

# 读取数据
cols_data = pd.read_excel('../../static/Classic low august 2020.xlsx', usecols=[0])
cols_list = cols_data.values.tolist()

# 写入文件
with open('thcode.txt', 'w') as f:
    for i in cols_list:
        f.write(f"'{i[0]}',\n")
