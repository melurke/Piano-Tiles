import pyautogui
import win32api, win32con
import time
import keyboard

pyautogui.click(506, 411)

y = 180
x_list = [369, 457, 546, 629]

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while not keyboard.is_pressed('q'):
    for x in x_list:
        if pyautogui.pixel(x, y)[0] == 0:
            click(x, y)
