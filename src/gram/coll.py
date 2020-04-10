from collections import Counter

str = 'adfafgagadfad'
# 获取字符串中出现前n个次数最多的字符
print(Counter(str).most_common(3))