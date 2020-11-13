import time

"""
测试python的jit加速前后运行速度对比
"""
start_time = time.time()
sum_num = 0
for i in range(987654321):
    sum_num = sum_num + i
end_time = time.time()
print(sum_num)
print(end_time - start_time)
