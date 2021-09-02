import tkinter as tk
from tkinter import *
import webbrowser
import numpy as np


    # link1= Label(root,text="Link",fg="blue",cursor="hand2")
    # link1.pack()
    # link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))
def callback(url):
    webbrowser.open_new(url)

class NameLink():
    def __init__(self):
        self.root=Tk()
    
    def callback(self,url):
        webbrowser.open_new(url)

    def CreateLink(self,arrayLink):
        for index,hyperLink in enumerate(arrayLink):
            link= Label(self.root,text="Link{}".format(index+1),fg="blue",cursor="hand2")
            link.pack()
            link.bind("<Button-1>", lambda e: self.callback(hyperLink))
        self.root.mainloop()
    # def Show(self):
        

arrayLink= np.array(['https://finance.vietstock.vn/CTG-ngan-hang-tmcp-cong-thuong-viet-nam.htm','https://finance.vietstock.vn/MBB-ngan-hang-tmcp-quan-doi.htm'])
links= NameLink()
links.CreateLink(arrayLink)
# links.Show()

# root = Tk()
# link1 = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
# link1.pack()
# link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

# link1 = Label(root, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
# link1.pack()
# link1.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

# root.mainloop()