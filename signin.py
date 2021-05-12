from tkinter import *
import sqlite3
import accounthome
#top is called sigin



def signinfunc():


    sigin = Toplevel()
    sigin.title('Sign In')


    sigin.geometry("1150x750")


    # submit button fuction
    def auth():

        conn=sqlite3.connect('asset.db')
        c=conn.cursor()

        c.execute("SELECT HolderID,Holder_Password FROM Holder where HolderID=:unamel", {'unamel': unamel.get()})
        check = c.fetchone()
        list =(unamel.get(), passl.get())
        sent=str(unamel.get())

        if check== list:
            accounthome.activity(sent)

            sigin.destroy()

        else:
            unamel.delete(0, END)
            passl.delete(0,END)
            labelf = Label(sigin, text="Please Try Again").grid(row=7, column=1, padx=20)






    label = Label(sigin, text="Enter ID and password").grid(row=0, column=1, padx=20)
    labelu = Label(sigin, text="ID").grid(row=2, column=1, padx=20)
    unamel = Entry(sigin, width=30)
    unamel.grid(row=3, column=1, padx=20)


    labelp = Label(sigin, text="Password").grid(row=4, column=1, padx=20)
    passl = Entry(sigin, width=30)
    passl.grid(row=5, column=1, padx=20)






    submit_btn = Button(sigin, text="Sign In", command=auth).grid(row=6, column=1, columnspan=2, pady=10, padx=10, ipadx=100)

