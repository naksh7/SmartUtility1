import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkinter.messagebox import showinfo

from SpeechRecognition import run_alexa

lastClickX = 0
lastClickY = 0


def savelastclickpos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x, y))


# root window
root = tk.Tk()
root.attributes('-topmost', True)                                 #Always on Top
root.geometry("100x100+1800+900")
root.title('Image Button Demo')
root.overrideredirect(True)
root.bind('<Button-1>', savelastclickpos)
root.bind('<B1-Motion>', dragging)
transparent_color = '#abcdef'
root.wm_attributes('-transparentcolor', transparent_color)        #Transparent color of Window
#canvas = tk.Canvas(root, bg=transparent_color, highlightthickness=0)
#canvas.pack()

# download button
def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'

    )
    run_alexa()


#quitImage = tk.PhotoImage(Image.open("google.png"))
#quitButton = canvas.create_image(bg=transparent_color,highlightthickness=0)
download_icon = tk.PhotoImage(file='google.png')
download_button = ttk.Button(
     root,
     image=download_icon,
     command=download_clicked
 )

download_button.pack(
     ipadx=5,
     ipady=5,
     expand=True
 )


root.mainloop()