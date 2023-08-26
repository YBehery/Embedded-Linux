import pyautogui
import time
pyautogui.hotkey('win')
pyautogui.write('firefox')
pyautogui.hotkey('enter')
time.sleep(2)
pyautogui.write('outlook.live')
time.sleep(2)
pyautogui.hotkey('enter')
time.sleep(10)
a=pyautogui.locateCenterOnScreen('/home/behery/Pictures/Screenshots/a.png')
pyautogui.moveTo(x=a[0],y=a[1])# I don't want to click it


