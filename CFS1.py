import os
import time
import pyautogui

SP = 'SP'

pyautogui.click(1725,52) 
pyautogui.hotkey('ctrl', 'f11')
time.sleep(1)

for x in range (1,4):
    pyautogui.press('tab')

pyautogui.typewrite('SP21')
time.sleep(2)
pyautogui.press('enter')
pyautogui.click(1700,56)
pyautogui.click(884,150)
time.sleep(1)
#pyautogui.doubleClick(680,466)
#pyautogui.hotkey('ctrl', 'c')
pyautogui.press('e')

#Enter Tiburon Interface
time.sleep(1)
pyautogui.click(2167,617)
#time.sleep(1)

#SP/CFS manual edits
pyautogui.click(2115,907)
pyautogui.click(2114,904)
#time.sleep(1)
pyautogui.press('backspace')
pyautogui.press('backspace')
time.sleep(1)
pyautogui.click(2199,906)

#Successful ST feature
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
pyautogui.press('backspace')
#pyautogui.press('backspace')
time.sleep(5)
#pyautogui.click(3378,117)
time.sleep(1)



#Automate start feature
#pyautogui.click(3380,107)
#pyautogui.hotkey('ctrl', 'NumPad_Decimal')

#Automate a copy/paste feature
#pyautogui.doubleClick(680,466)
#pyautogui.hotkey('ctrl', 'c')
#pyautogui.doubleClick(2200,905)
#pyautogui.hotkey('ctrl', 'v')

#Create a 'for loop'
#pyautogui.press('backspace')
#pyautogui.press('backspace')
#time.sleep(1)
#pyautogui.press('end')
#pyautogui.press('backspace')
#pyautogui.press('backspace')
#pyautogui.press('backspace')
#pyautogui.press('backspace')
#pyautogui.press('backspace')
#time.sleep(2)

#Formatting
#pyautogui.press(')')
#pyautogui.click(1041,473)
#pyautogui.press('backspace')
#pyautogui.click(1041,473)
#pyautogui.press('end')
