from tkinter import *

import signin
from signin import *
import sqlite3
import manage
#base is home instead of root
import trade



def activity(got):
    home = Toplevel()
    home.title('My Activity')
    home.geometry("1100x750")
    ##redirectfunctions

    def redtomgasset():
        manage.mgasset(got)#send 'got' to mgasset

    def redtotradelist():
        trade.tradef()



    homelab=Label(home ,text="Welcome Back!",font=('Helvetica', 30),fg='gray')
    homelab.grid(row=0,column=0,pady=20,padx=10)
    greet = Label(home,text=got+"(signed in)",font=('Helvetica', 20))
    greet.grid(row=0, column=1, pady=20, padx=10)

    btn = Button(home, text="Manage Assets", font=('Helvetica', 25, 'bold'),command=redtomgasset).grid(row=1, column=1,padx=40, pady=30,ipadx=100)
    btn = Button(home, text="Trade Assets", font=('Helvetica', 25, 'bold'),command=redtotradelist).grid(row=2, column=1,  padx=40, pady=30,ipadx=100)

