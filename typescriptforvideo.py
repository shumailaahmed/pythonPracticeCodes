import os
import pyautogui
import keyboard
import time
import win32api, win32con
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def click_right(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,x,y,0,0)

click(260,741) #click on python icon in taskbar
time.sleep(2)

pyautogui.keyDown('ctrl')
pyautogui.keyDown('shift')
pyautogui.keyDown('s')

pyautogui.keyUp('ctrl')
pyautogui.keyUp('shift')
pyautogui.keyUp('s')

time.sleep(1)
keyboard.write('Pyagonist_ReadfromDiskTest',delay=0.15)
pyautogui.press('enter')

# Set path to the folder: (replace with your own filepath!):
folder = r"D:\Pathtofolder"

# Set name of the file
filename = "<filename txt>"

# Generate full filepath by combining the folder and filename
fp = os.path.join(folder, filename)

# Read all contents of the file:
with open(fp, "r") as infile:
    text = infile.read()
    #print(text)
    keyboard.write(text,delay=0.15)
    pyautogui.press('enter')

pyautogui.keyDown('ctrl')
pyautogui.keyDown('s')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('s')


pyautogui.keyDown('alt')
pyautogui.keyDown('F4')
pyautogui.keyUp('alt')
pyautogui.keyUp('F4')
