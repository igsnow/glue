import sys
import win32clipboard as w
import win32con
import pyHook
import pythoncom
import random

array = []


def onKeyboardEvent(event):
    if (event.Key == 'Space'):
        e = random.choice(array)
        str = e.decode('utf-8')
        print(event.Key + '=>' + str)
        # 写入系统
        setTxt(str.encode(sys.getfilesystemencoding()))
    return True


def setTxt(str):
    print(win32con.CF_TEXT)
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, str)
    w.CloseClipboard()


if __name__ == '__main__':
    f = open('kouhai.txt', 'rb')
    array = f.readlines()
    print(array)
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    f.close()
