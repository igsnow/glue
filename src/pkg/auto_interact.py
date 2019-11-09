# coding=utf-8
import sys
import win32clipboard as w
import win32con
import pyHook
import pythoncom
import random

array = []


def onKeyboardEvent(event):
    if (event.Key == "Lcontrol"):
        print('监听按键:' + event.Key)
        # 随机读取一行文字
        b = random.sample(array, 1)
        print('随机抽取的文字：' + b[0].decode('utf-8'))
        # 写入系统缓存
        settext(b[0].decode('utf-8').encode(sys.getfilesystemencoding()))
    return True


def settext(str):
    # 打开剪切板
    w.OpenClipboard()
    # 置空剪切板
    w.EmptyClipboard()
    # 写入剪切板
    w.SetClipboardData(win32con.CF_TEXT, str)
    # 关闭剪切板
    w.CloseClipboard()


if __name__ == '__main__':
    # 修改了读取文件报错
    f = open('kouhai.txt', 'rb')
    # 逐行读取文件内容
    array = f.readlines()
    print(array)
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
