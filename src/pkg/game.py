# coding=utf-8
import sys
import win32clipboard as w
import win32con
import win32api
import PyHook3
import pythoncom
import random

array = []


def onKeyboardEvent(event):
    if (event.Key == "Lmenu"):
        print('=> ' + event.Key)
        # 随机读取一行文字
        b = random.choice(array)
        print('=> ' + b)
        # 写入系统缓存
        setText(b)
        # 自动粘贴剪切板的内容
        handleText()
    return True


def setText(str):
    # 打开剪切板
    w.OpenClipboard()
    # 置空剪切板
    w.EmptyClipboard()
    # 写入剪切板
    w.SetClipboardText(str)
    # 关闭剪切板
    w.CloseClipboard()


def getText():
    w.OpenClipboard()
    res = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return res


def handleText():
    r = getText()
    print(r)

    # ctrl
    win32api.keybd_event(17, 0, 0, 0)
    # v
    win32api.keybd_event(86, 0, 0, 0)
    # enter
    win32api.keybd_event(13, 0, 0, 0)
    # 释放按键
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == '__main__':
    # 修改了读取文件报错
    f = open('msg.txt', 'r', encoding='utf-8')
    # 逐行读取文件内容
    array = f.readlines()
    # 创建hook句柄
    hm = PyHook3.HookManager()
    # 监控键盘
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    # 循环获取消息
    pythoncom.PumpMessages()
    # 关闭文件
    f.close()
