import sys
import win32clipboard as w
import win32con
import pyHook
import pythoncom
import random

# 消息列表
array = []


def onKeyboardEvent(event):
    print(event.Key)
    if (event.Key == 'Space'):
        e = random.choice(array)
        str = e.decode('utf-8')
        setTxt(str.encode(sys.getfilesystemencoding()))
    return True


def setTxt(str):
    print(str)
    w.OpenClipboard()
    w.EmptyClipboard()
    # 获取剪切板的输入框
    w.SetClipboardData(win32con.CF_TEXT, str)
    w.CloseClipboard()


if __name__ == '__main__':
    # 打开本地文件
    f = open('kouhai.txt', 'rb')
    # 读取文件内容
    array = f.readlines()
    print(type(array))
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    f.close()
