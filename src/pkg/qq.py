import win32gui
import win32con
import win32clipboard as w

# 发送的消息
msg = 'lpl win'
# 窗口名字
name = '难听的歌'
# 将消息复制到剪切板
w.OpenClipboard()
w.EmptyClipboard()
w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
w.CloseClipboard()
# 获取窗口句柄
handle = win32gui.FindWindow(None, name)

if 1 == 1:
    win32gui.SendMessage(handle, 770, 0, 0)
    win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
