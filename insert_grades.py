import pyautogui
from pynput.keyboard import *


stop = False
pause = True

def enter_grade(grade):
    pyautogui.write(grade, 0.005)
    pyautogui.press('down')
    

def on_press(key):
    # print(key)
    global stop, pause
    if key.char == 'q':
        stop = True
    elif key.char == 'b':
        print('b pressed')
        pause = False
    elif key.char == 's':
        pause = True 


with open("students_grades.csv", "r", encoding="utf-8") as f:
    l = [x.strip().split(',')[1] for x in f.readlines()[1:]]
L = Listener(on_press=on_press)
L.start()
i = 0
while not stop:
    if pause:
        continue

    pyautogui.write(l[i], 0.005)
    pyautogui.press('down')
    i += 1
    if i == len(l):
        stop = True 
        print('Done!')
L.stop()
