import pyautogui
import win32api, win32con
import time
import keyboard

pyautogui.click(490, 474)

y = 156
x_list = [300, 420, 550, 660]

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while not keyboard.is_pressed('q'):
    for x in x_list:
        if abs(pyautogui.pixel(x, y)[0] - 21) < 20:
            click(x, y)
