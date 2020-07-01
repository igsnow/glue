import sys


# 获取当前运行的类名和函数名
class Hi:
    def hello(self):
        print('the name of method is {}'.format(sys._getframe().f_code.co_name))
        print('the name of class is {}'.format(self.__class__.__name__))


h = Hi()
h.hello()
