import pyautogui
import time

time.sleep(5)

message = "This is an automatic typing bot demo.\nIt types each word with a slight delay.\nEnjoy!"

pyautogui.write(message, interval=0.1)