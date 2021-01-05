from WindowMgr import *
from const import *
from time import sleep
import pyautogui


def vscode_setup():
    launch('code', workspace_path)
    w = WindowMgr()
    w.find_window_wildcard('Visual Studio Code')
    w.set_foreground()

    open_terminal()
    start_dotnet()
    new_terminal()
    start_angular()


def open_terminal():
    sleep(2)
    pyautogui.hotkey('ctrl', 'alt', '`', '0')


def new_terminal():
    pyautogui.hotkey('ctrl', 'shift', '`')


def start_dotnet():
    pyautogui.write('cd API')
    pyautogui.press('enter')
    pyautogui.write('dotnet run')
    pyautogui.press('enter')


def start_angular():
    pyautogui.write('cd client')
    pyautogui.press('enter')
    pyautogui.write('ng serve')
    pyautogui.press('enter')
