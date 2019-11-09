import sys
import win32clipboard as w
import win32con
import pyHook
import pythoncom
import random

# 消息列表
array = []


def onkeyboardEvent(event):
    print('按键 ' + event.Key)
    if (event.Key == 'Space'):
        e = random.choice(array)
        str = e.decode('utf-8')
        print('msg ' + str)
        setTxt(str.encode(sys.getfilesystemencoding()))

    return True


def setTxt(str):
    print(str)
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, str)
    w.CloseClipboard()


if __name__ == '__main__':
    # 打开本地文件
    f = open('kouhai.txt', 'rb')
    # 读取文件
    array = f.readlines()
    print(type(array))
    hm = pyHook.HookManager()
    hm.KeyDown = onkeyboardEvent
    hm.HookKeyboard()
    # 循环接收消息
    pythoncom.PumpMessages()
    f.close()
