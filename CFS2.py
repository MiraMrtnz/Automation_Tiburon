import os
import time
import pyautogui

SP = 'SP'

pyautogui.click(1725,52) 
pyautogui.hotkey('ctrl', 'f11')
time.sleep(1)

for x in range (1,4):
    pyautogui.press('tab')

pyautogui.typewrite('SP16')
time.sleep(2)
pyautogui.press('enter')
pyautogui.click(1700,56)
pyautogui.click(884,150)
pyautogui.press('e')
pyautogui.click(1081,252)

time.sleep(1)
pyautogui.click(1049,537)
pyautogui.press('backspace')
#pyautogui.press('backspace')
time.sleep(1)
pyautogui.press('end')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
time.sleep(2)
pyautogui.press(')')
#pyautogui.click(1041,473)

#pyautogui.press('backspace')
#pyautogui.click(1041,473)
#pyautogui.press('end')
