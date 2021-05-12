from tkinter import *

import sqlite3
#make func signup
#local root is sup
#sup = Tk()

def signupfunc():

    sup = Toplevel()
    sup.title('Sign Up')

    sup.geometry("600x400")

    # Databases

    # Create a database or connect to one
    conn = sqlite3.connect('asset.db')

    # Create cursor
    c = conn.cursor()










    # Create Submit Function For database
    def submit():
        # Create a database or connect to one
        conn = sqlite3.connect('asset.db')
        # Create cursor
        c = conn.cursor()

        # Insert Into Table
        c.execute("INSERT INTO Holder VALUES (:id, :passw, :email, :name, :type)",
                  {
                      'id': h_id.get(),
                      'passw': h_passw.get(),
                      'email': h_email.get(),
                      'name': h_name.get(),
                      'type': h_type.get()

                  })

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        # Clear The Text Boxes
        h_id.delete(0, END)
        h_passw.delete(0, END)
        h_email.delete(0, END)
        h_name.delete(0, END)
        h_type.delete(0, END)
        endlabel=Label(sup,text="Thanks for joining.Sign In again from homepage.").grid(row=7,column=0)


    # Create Query Function


    # Create Text Boxes
    h_id = Entry(sup, width=30)
    h_id.grid(row=1, column=1, padx=20, pady=(10, 0))
    h_passw = Entry(sup, width=30)
    h_passw.grid(row=2, column=1)
    h_email = Entry(sup, width=30)
    h_email.grid(row=3, column=1)
    h_name = Entry(sup, width=30)
    h_name.grid(row=4, column=1)
    h_type = Entry(sup, width=30)
    h_type.grid(row=5, column=1)

    # Create Text Box Labels
    h_id_label = Label(sup, text="Username")
    h_id_label.grid(row=1, column=0, pady=(10, 0))
    h_passw_label = Label(sup, text="Password")
    h_passw_label.grid(row=2, column=0)
    h_email_label = Label(sup, text="Email")
    h_email_label.grid(row=3, column=0)
    h_name_label = Label(sup, text="Name")
    h_name_label.grid(row=4, column=0)
    h_type_label = Label(sup, text="Type(Individual,Mutual or Company)")
    h_type_label.grid(row=5, column=0)


    # Create Submit Button
    submit_btn = Button(sup, text="Sign Up", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    #sup.mainloop()

