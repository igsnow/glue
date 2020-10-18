import pandas as pd

# 读取数据
cols_data = pd.read_excel('../../static/refund.xls', usecols=[0])
cols_list = cols_data.values.tolist()

# 读取第一行的内容，一般是表头，如account
labels = list(cols_data.columns.values)

# 是否要包含第一行的内容
# cols_list.insert(0, cols_data.columns.values)

# 写入文件
with open('thcode.txt', 'w') as f:
    for i in cols_list:
        f.write(f"'{i[0]}',\n")
