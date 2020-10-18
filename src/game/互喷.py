# coding=utf-8
import win32clipboard as w
import win32con
import win32api
import PyHook3
import pythoncom
import random

array = []


def on_keyboard_event(event):
    if event.Key == "Lmenu":
        print('监听按键: ', event.Key)
        # 随机读取一行文字
        b = random.choice(array)
        print('随机语录: ', b)
        # 写入系统缓存
        set_text(b)
        # 自动粘贴剪切板的内容
        copy_text()
    return True


def set_text(str):
    # 打开剪切板
    w.OpenClipboard()
    # 置空剪切板
    w.EmptyClipboard()
    # 写入剪切板
    w.SetClipboardText(str)
    # 关闭剪切板
    w.CloseClipboard()


def get_text():
    w.OpenClipboard()
    res = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return res


def copy_text():
    r = get_text()
    print('剪切板: ', r.decode('gbk'))
    # Y 唤起聊天框
    win32api.keybd_event(0x59, 0, 0, 0)
    # 释放按键Y
    win32api.keybd_event(0x59, 0, win32con.KEYEVENTF_KEYUP, 0)
    # ctrl
    win32api.keybd_event(0x11, 0, 0, 0)
    # v
    win32api.keybd_event(0x56, 0, 0, 0)
    # 释放按键ctrl、v
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    # enter
    win32api.keybd_event(0x0D, 0, 0, 0)
    # 释放按键enter
    win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == '__main__':
    # 修改了读取文件报错
    f = open('../tools/msg.txt', 'r', encoding='utf-8')
    # 逐行读取文件内容
    array = f.readlines()
    # 创建hook句柄
    hm = PyHook3.HookManager()
    # 监控键盘
    hm.KeyDown = on_keyboard_event
    hm.HookKeyboard()
    # 循环获取消息
    pythoncom.PumpMessages()
    # 关闭文件
    f.close()
