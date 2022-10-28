from tkinter import *
from tkinter.messagebox import showinfo
from PIL import ImageGrab

import pyautogui
from PIL import ImageTk, Image
from tkinter import ttk

from SpeechRecognition import run_alexa

lastClickX = 0
lastClickY = 0

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y
    showinfo(
        title='Information',
        message='Download button clicked!'
    )
    run_alexa()

def Dragging(event):
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))


def my_command():
   print('pressed')

def screenshot(event):
   pyautogui.hotkey('win','shift','s')
   im = ImageGrab.grabclipboard()
   im.save('somefile.png', 'PNG')


window = Tk()
window.overrideredirect(True)                                       #For Borderless
window.attributes('-topmost', True)                                 #Always on Top
window.geometry("64x64+1800+900")                                   #Size of Window
window.bind('<Button-1>', SaveLastClickPos)
window.bind('<Button-3>', screenshot)
window.bind('<B1-Motion>', Dragging)
transparent_color = '#abcdef'                                       #Transparent color of Window
window.wm_attributes('-transparentcolor', transparent_color)        #Transparent color of Window
canvas = Canvas(window, bg=transparent_color,highlightthickness=0)  #No Window Border
canvas.pack(fill=BOTH, expand=1)
photo = PhotoImage(file='mic.png')
img_label= Label(image=photo)
button= ttk.Button(window, command= my_command)
button.pack(pady=30)

text= Label(window, text="")
text.pack(pady=30)


canvas.create_image(0, 0, image=photo, anchor=N+W)
window.mainloop()