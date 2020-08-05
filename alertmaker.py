Python 3.8.2 (default, Apr 27 2020, 15:53:34) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.

#This program will make an alert appear 
#on screen when the button is pressed.

Credit = Vibemaster

>>> from tkinter import *
>>> from tkinter import messagebox
>>> from tkinter import Button
>>> from tkinter import Tk, TOP
>>> def callback():
	root = Tk()
	root.withdraw()
	messagebox.showinfo('Doop', 'Hello There')

	
>>> boot = Tk()
>>> b = Button(boot, text='Press me!', command = callback).pack(side = TOP)
