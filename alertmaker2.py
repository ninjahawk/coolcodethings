Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.

#Works the exact same way as the original
#except that this second version makes use 
#of methods instead of functions just romping
#about part of no class. This is a simple 
#alertmaker. 

Credit = Nathan B Langley

from tkinter import messagebox
from tkinter import Button
from tkinter import Tk, TOP
class doop:
	def callback(self):
		root = Tk()
		root.withdraw()
		messagebox.showinfo('doop', 'Doop boop')
boot = Tk()
d = doop()
b = Button(boot, text='Hello Bub', command = d.callback())
def bb():
	b = Button(boot, text='Hello Bub', command = d.callback())
	
a = Button(boot, text='Press here', command = bb).pack(side = TOP)
