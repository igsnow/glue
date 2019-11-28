import PyHook3
import pythoncom
import random
import win32clipboard as w
import win32con

array = []


def on_keyboard_event(event):
    if event.Key == 'Lmenu':
        print('监听按键', event.Key)
        # 随机读取一行文字
        s = random.choice(array)
        print(s)
        # 将文字写入剪切板
        set_text(s)
        # 粘贴文字到剪切板
        copy_text()
    return True


def set_text(str):
    # 打开剪切板
    w.OpenClipboard()
    # 置空剪切板
    w.EmptyClipboard()
    # 写入文字
    w.SetClipboardText(str)
    # 关闭剪切板
    w.CloseClipboard()


def get_text():
    w.OpenClipboard()
    # 获取剪切板数据
    res = w.GetClipboardData(win32con.CF_TEXT)
    return res


def copy_text():
    r = get_text()
    print(r.decode('gbk'))


if __name__ == '__main__':
    f = open('msg.txt', 'r', encoding='utf8')
    # 逐行读取文件
    array = f.readlines()
    # print(array)
    # 创建hook句柄
    hm = PyHook3.HookManager()
    # 处理被监控的键
    hm.KeyDown = on_keyboard_event
    # 监听键盘事件
    hm.HookKeyboard()
    # 循环获取消息
    pythoncom.PumpMessages()
    # 关闭文件
    f.close()
