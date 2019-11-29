import PyHook3
import pythoncom
import random
import win32clipboard as w
import win32con
import win32api

array = []


def on_keyboard_event(event):
    if event.Key == 'Lmenu':
        print(event.Key)
        s = random.choice(array)
        print('随机', s)
        set_text(s)
        copy_text()
    return True


def set_text(str):
    # 打开剪切板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(str)
    w.CloseClipboard()


def get_text():
    w.OpenClipboard()
    res = w.GetClipboardData(win32con.CF_TEXT).decode('gbk')
    w.CloseClipboard()
    return res


def copy_text():
    res = get_text()
    print('剪切板', res)
    # 按下y键
    win32api.keybd_event(0x59, 0, 0, 0)
    # 释放y键
    win32api.keybd_event(0x59, 0, win32con.KEYEVENTF_KEYUP, 0)
    # 按下ctrl键
    win32api.keybd_event(0x11, 0, 0, 0)
    # 按下 v键
    win32api.keybd_event(0x56, 0, 0, 0)
    # 先释放v,再释放ctrl
    win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
    # 按下enter
    win32api.keybd_event(0x0D, 0, 0, 0)
    # 释放enter
    win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)


if __name__ == '__main__':
    # 打开文件
    f = open('msg.txt', 'r', encoding='utf8')
    # 逐行读取文件
    array = f.readlines()
    # print(array)
    # 获取操作句柄
    hm = PyHook3.HookManager()
    # 创建监听键盘按下事件方法
    hm.KeyDown = on_keyboard_event
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    f.close()
