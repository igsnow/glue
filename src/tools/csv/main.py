import pymongo
import pandas as pd
import numpy as np

client = pymongo.MongoClient('mongodb://116.62.11.8:27011')
db = client.get_database("erpdb")
db.authenticate('erpadmin', 'erpadmin112233')

mydb = client["erpdb"]
mycol = mydb["online"]

x = mycol.find_one()

print(x)

# data = np.arange(1, 101).reshape((10, 10))
# data_df = pd.DataFrame(data)
# data_df.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# data_df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# writer = pd.ExcelWriter('my.xlsx')
# data_df.to_excel(writer, float_format='%.5f')
# writer.save()
