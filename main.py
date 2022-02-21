# This is a sample Python script.

#Think about doing a dropdown menu for the intergers so if they choose 1 / 12 from there and we don't need to take input

import random
import string
from tkinter import *

master = Tk()
master.title('Password Generator')
master.geometry('250x220')
master.configure(bg='light grey')

intentry = IntVar()

numberlabel = Label(master, text='-Number of characters- ',
                     bg = "light grey").grid(row=0, column=1, sticky=W)

numberentry= Entry(master, textvariable=intentry, bd=0,).grid(row=1, column=1, sticky=W)

resultlabel = Label(master, text='-Password generated-',
                     bg = "light grey").grid(row=2, column=1, sticky=W)

mainloop()



def passwordgen(input):
    n = int(input(""))
    if n >=16:
        return("The maximum character limit for passwords is 16 - please try again")
    else:
        return(''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(n)))

print(passwordgen(input))