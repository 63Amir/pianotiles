import pyautogui
import time
import keyboard
import win32api, win32con
import os
def clear():
    os.system('cls')

# Get The Color
color = str(input("Bring Mouse to a Piano Tile and press Enter"))
if color == "":
    red = pyautogui.position()
    red, green, blue = pyautogui.pixel(red[0], red[1])
# Positions of 4 Piano lines
a_input = str(input("Bring Mouse to Point A than Press Enter"))
if a_input == "":
    a = pyautogui.position()
b_input = str(input("Bring Mouse to Point B than Press Enter"))
if b_input == "":
    b = pyautogui.position()
c_input = str(input("Bring Mouse to Point C than Press Enter"))
if c_input == "":
    c = pyautogui.position()
d_input = str(input("Bring Mouse to Point D than Press Enter"))
if d_input == "":
    d = pyautogui.position()
clear()
print("""
                                 ..;;;;;;;              B
                               ,;;;;;;;;;'              Y
                             ,;;;;;;;\                  
                           ,;;;;;;;;  \                 A
                         ,;;;;;;;;     \                M
                       ,;;;;;;;;        \               I
                     ,;;;;;;;; ,,,,      \              R
                   ,;;;;;;;; '     ',     \             
                 ,;;;;;;;;            ' . ,\,           V
             .,;;;;;;;;_______________      \ ',        1
            /__________I             I__________\\
            I__________I_____________I___________I
            [=MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM=]
             { }        { }  III              { }
             { }        { }  III              { }
             { }       [__]  III              { }
            _{ }             III              { }
            [__]            O C O             [__]
                    
                     Press Esc for Stop                             
""")

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('esc') == False:
    if pyautogui.pixel(a[0],a[1])[0] == red:
        click(a[0],a[1])
    if pyautogui.pixel(b[0],a[1])[0] == red:
        click(b[0],a[1])
    if pyautogui.pixel(c[0],a[1])[0] == red:
        click(c[0],a[1])
    if pyautogui.pixel(d[0],a[1])[0] == red:
        click(d[0],a[1])
