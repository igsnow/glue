#coding=utf-8
import sys
import win32clipboard as w
import win32con
import pyHook
import pythoncom
import random

array = []

def onMouseEvent(event):
    if (event.MessageName != "mouse move" and event.MessageName != "mouse wheel"):
        print(event.MessageName)
    return True


def onKeyboardEvent(event):
    if (event.Key == "Lcontrol"):
        b = random.sample(array, 1)
        settext(b[0].decode('utf-8').encode(sys.getfilesystemencoding()))
    print(event.Key)
    return True


def gettext():
    w.OpenClipboard()
    t = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return t

def settext(str):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, str)
    w.CloseClipboard()

if __name__ == '__main__':
    f = open('kouhai.txt', 'r')
    array = f.readlines()
    hm = pyHook.HookManager()
    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()
    # hm.MouseAll = onMouseEvent
    # hm.HookMouse()
    pythoncom.PumpMessages()
