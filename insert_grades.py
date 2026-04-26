# import pyautogui
# from pynput.keyboard import *
# import time
# 
# 
# stop = False
# pause = True
#     
# 
# def on_press(key):
#     # print(key)
#     try:
#         global stop, pause
#         if key.char == 'q':
#             stop = True
#         elif key.char == 'b':
#             print('b pressed')
#             pause = False
#         elif key.char == 's':
#             pause = True 
#     except:
#         pass
# 
# 
# with open("students_grades.csv", "r", encoding="utf-8") as f:
#     l = [x.strip().split(',')[1] for x in f.readlines()[1:]]
# L = Listener(on_press=on_press)
# L.start()
# i = 0
# print("Ready. Press 'b' to begin, 's' to pause, 'q' to quit.")
# while not stop:
#     if pause:
#         time.sleep(0.1)
#         continue
# 
#     pyautogui.write(l[i], 0.005)
#     pyautogui.press('down')
#     i += 1
#     if i == len(l):
#         stop = True 
#         print('Done!')
# L.stop()

import time
from pynput.keyboard import Listener, Controller, Key

stop = False
pause = True

# Initialize the pynput keyboard controller
keyboard = Controller()

def on_press(key):
    try:
        global stop, pause
        if hasattr(key, 'char') and key.char:
            if key.char == 'q':
                stop = True
                print('\nQuitting...')
            elif key.char == 'b':
                print('\nStarted/Unpaused')
                pause = False
            elif key.char == 's':
                print('\nPaused')
                pause = True 
    except Exception:
        pass

with open("students_grades.csv", "r", encoding="utf-8") as f:
    # Extracting the second column 
    l = [x.strip().split(',')[1] for x in f.readlines()[1:]]

L = Listener(on_press=on_press)
L.start()

i = 0
print("Ready. Press 'b' to begin, 's' to pause, 'q' to quit.")

while not stop:
    if pause:
        time.sleep(0.1) # Prevents the while loop from maxing out CPU usage
        continue

    if i < len(l):
        # 1. Type the grade using Unicode injection (bypasses layout issues)
        keyboard.type(l[i])
        
        # 2. Small buffer to let the browser register the typing
        time.sleep(0.05) 
        
        # 3. Simulate pressing the down arrow
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        
        # 4. Small buffer to let the UI move to the next cell
        time.sleep(0.05)
        
        i += 1
    else:
        stop = True 
        print('\nDone!')

L.stop()
