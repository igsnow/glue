from xpinyin import Pinyin

p = Pinyin()

# 默认以'-'作为分隔符
print(p.get_pinyin('杭州'))

# 显示音调   'marks'标记、'numbers'音标序号
print(p.get_pinyin('杭州', tone_marks='marks'))

# 删除分隔符
print(p.get_pinyin('杭州', ''))

# 设置空白分隔符
print(p.get_pinyin('杭州', ' '))
