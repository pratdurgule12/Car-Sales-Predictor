# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 19:22:15 2021

@author: Prathamesh P Durgule
"""

from tkinter import*
from PIL import Image,ImageTk

root=Tk()
root.geometry('500x444')
image= Image.open('C:\\Users\\Prathamesh P Durgule\\Desktop\\I1.jpeg')
render = ImageTk.PhotoImage(image)

img = Label(root,image = render)
img.place(x=0,y=0)
Label(root, text="").pack()
Label(root, text="CAR SALES PREDICTOR",font="Verdana",bg="blue",anchor="w").pack()
Label(root, text="").pack()

Label(root, text="SALARY",anchor="w",justify="left",bg="lightyellow").pack()

Label(root, text="").pack()

username_login_entry = Entry(root, textvariable="SALARY")
username_login_entry.pack()

Label(root, text="").pack()

Label(root, text="AGE",anchor="w",justify="left",bg="lightyellow").pack()

Label(root, text="").pack()

password__login_entry = Entry(root, textvariable="AGE", show= '*')
password__login_entry.pack()

Label(root, text="").pack()

Button(root, text="ENTER", width=10, height=1,bg="grey").pack()

root.title("CAR SALES PREDICTOR")
root.mainloop()
