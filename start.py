from tkinter import *
import sqlite3
import signin
import signup
import submit
#from signin import sigfunc

# rom Image import ImageTk,Image

root = Tk()
root.title('Asset Manager:Home')
root.geometry("1150x750")
bg = PhotoImage(file="backg.png")
label1 = Label(root, image=bg)
label1.place(x=60, y=20)



introlabel1 = Label(root, text="Asset Manager ", font=('Helvetica', 60, 'bold')).grid(row=9, column=2, padx=40, pady=40)
bufflab = Label(root, text=" ").grid(row=10, column=2, pady=50)
introlabel2 = Label(root, text=" Siddhanth Shresth(18ET1009)", font=('Helvetica', 20)).grid(row=11, column=2, padx=40)
introlabel3 = Label(root, text=" Yash Shenoy(18ET1114)", font=('Helvetica', 20)).grid(row=12, column=2, padx=40)
introlabel4 = Label(root, text=" Amogh Raut(18ET1088)", font=('Helvetica', 20)).grid(row=13, column=2, padx=40)
introlabel5 = Label(root, text="   TE 'C'  EXTC ", font=('Helvetica', 20)).grid(row=14, column=2, padx=40)
bufflab = Label(root).grid(row=15, pady=50)
newusr = Label(root, text="New User? ", font=('Helvetica', 15, 'bold')).grid(row=16, column=1, padx=40)
btn = Button(root, text="Sign Up", font=('Helvetica', 15, 'bold'), command=signup.signupfunc).grid(row=17, column=1, padx=40, pady=40)
already = Label(root, text="Already Registered? ", font=('Helvetica', 15, 'bold')).grid(row=16, column=3, padx=40)
btn2 = Button(root, text="Sign In", font=('Helvetica', 15, 'bold'), command=signin.signinfunc).grid(row=17, column=3,  padx=40, pady=40)
# btn=Button(root,text="",command=open).grid(row=7,column=1,padx=40,pady=40)

mainloop()


