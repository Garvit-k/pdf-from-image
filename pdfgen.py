#Import all libraries
import img2pdf
import os
from PIL import Image
from tkinter import *
import dirSelector

def removealpha(inpath):
    print('Converting Image into non alpha channel image')
    for file in os.listdir(inpath):
        img = Image.open(inpath+file)
        size = img.size
        imgnew = Image.new('RGB',size,255)
        imgnew.paste(img,(0,0))
        imgnew.save('out/'+file)
    print('Image Conversion done.')

def pdfGen(inpath,outpath):
    l = os.listdir(inpath)
    lst = []
    print('PDF Creating...')
    for i in l:
        lst.append(open((inpath+i),'rb'))
    with open('out.pdf','wb') as f:
        f.write(img2pdf.convert(lst))

    print('PDF Generation done.')

def browse_button():
    from tkinter import filedialog
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


def guiGen():
   master = Tk()
   master.wm_minsize(width=200, height=200)
   Label(master, text='Input Directory').grid(row=0)
   Label(master, text='Output Directory').grid(row=1)
   folder_path = StringVar()
   e1 = Button(master, text='Select', width=10,command=browse_button)
   e2 = Button(master, text='Select', width=10,command=browse_button)
   e1.grid(row=0, column=1)
   e2.grid(row=1, column=1)
   button = Button(master, text='Stop', width=25, command=master.destroy)
   button.grid(row=2, column=1)

   mainloop()


def main():
    guiGen()
    # inpath = 'ada/'
    # outpath = 'result/'
    # removealpha(inpath)
    # pdfGen('out/',outpath)


if __name__ == "__main__":
    main()
