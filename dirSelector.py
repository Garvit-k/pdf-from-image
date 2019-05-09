from tkinter import filedialog
from tkinter import *

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

root = Tk()
root.wm_minsize(200,200)
folder_path = StringVar()
lbl1 = Label(master=root,textvariable=folder_path)
lbl1.grid(row=0, column=1)
button2 = Button(text="Browse", width=10, command=browse_button)
button2.grid(row=0, column=3)
closeButton = Button(root, text='Exit', width=20, command=root.destroy)
closeButton.grid(row=1,column=1)
print(folder_path)
mainloop()

def getFolder():
    return folder_path

