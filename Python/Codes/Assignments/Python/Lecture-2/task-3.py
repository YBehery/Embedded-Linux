import pyautogui
import time
def setup(str):
    pyautogui.shortcut('ctrl','shift','x')
    pyautogui.shortcut('ctrl','a')
    pyautogui.hotkey('backspace')
    pyautogui.write(str)
    time.sleep(4)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('down')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')

setup ('clangd')
setup('c++ testmate')
setup ('c++ helper')
setup('cmake')
setup('cmake tools')
