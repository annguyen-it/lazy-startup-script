import ctypes
import win32gui
import re
from time import sleep
import os


class WindowMgr:
    def __init__(self):
        self._handle = None

    def find_window(self, class_name, window_name=None):
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        if (re.match(wildcard, str(win32gui.GetWindowText(hwnd)))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        win32gui.SetForegroundWindow(self._handle)


def launch(app, file_dir=''):
    os.system(app + ' ' + file_dir)


def move_to_desktop(desktop):
    sleep(0.5)
    virtual_desktop_accessor = ctypes.WinDLL('./VirtualDesktopAccessor.dll')
    virtual_desktop_accessor.GoToDesktopNumber(desktop)
    sleep(0.5)
