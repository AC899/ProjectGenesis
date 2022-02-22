# This is a sample Python script.

#Think about doing a dropdown menu for the intergers so if they choose 1 / 12 from there and we don't need to take input

import random
import string
from tkinter import *

#entry box

master = Tk()
master.title('Password Generator')
master.geometry('250x220')
master.configure(bg='light grey')

def passwordgen():
    n = intentry.get() #tried numberentry.get
    if n >=16:
        return("maximum character limit is 16 - try again")
    else:
        return(res.set(''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(n))))

intentry = IntVar()
res=StringVar()

numberlabel = Label(master, text='-Number of characters- ',
                     bg = "light grey").grid(row=0, column=1, sticky=W)

numberentry= Entry(master, text='', textvariable=intentry, bd=0,).grid(row=1, column=1, sticky=W)
# master.bind('<Return>',passwordgen)
#
resultlabel = Label(master, text='-Password generated-',
                     bg = "light grey").grid(row=2, column=1, sticky=W)

resulentryfinal = Entry(master, text='', textvariable=res, bd=0, state='readonly').grid(row=3, column=1, sticky=W)

b = Button(master, text='convert', command=passwordgen)
b.grid(row=5, column=1, sticky=W)

mainloop()

#make it so as when you press enter in number entry - it returns passwordgen in the







# def passwordgen(input):
#     n = int(input(""))
#     if n >=16:
#         return("maximum character limit is 16 - try again")
#     else:
#         return(''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(n)))
#
# print(passwordgen(input))