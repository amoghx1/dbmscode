from tkinter import *
import accounthome
import signin
import sqlite3
#base is trd instead of root


def tradef():
    trd = Toplevel()
    trd.title('Stock Exchange')
    trd.geometry("1100x750")
    def add():
        # Create a database or connect to one   submit fcn
        conn = sqlite3.connect('asset.db')
        # Create cursor
        c = conn.cursor()

        # Insert Into Table
        c.execute("INSERT INTO Tradelisting VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'address': address.get(),
                      'city': city.get(),
                      'state': state.get(),
                      'zipcode': zipcode.get()
                  })

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        # Clear The Text Boxes
        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        zipcode.delete(0, END)

    def query():
        # Create a database or connect to one
        conn = sqlite3.connect('asset.db')
        # Create cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *, oid FROM Tradelisting")
        records = c.fetchall()
        # print(records)

        # Loop Thru Results
        print_records = ''
        for record in records:
            print_records += str(record[6]) + " | " + str(record[0]) + " | " + str(record[1]) + " | " + str(record[2]) + " | " +  str(record[3]) + " | " +str(record[4]) + " | " +str(record[5])+"\n"+"\n"

        query_label = Label(trd, text=print_records)
        query_label.grid(row=12, column=0, columnspan=10)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

    f_name = Entry(trd, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name = Entry(trd, width=30)
    l_name.grid(row=1, column=1)
    address = Entry(trd, width=30)
    address.grid(row=2, column=1)
    city = Entry(trd, width=30)
    city.grid(row=3, column=1)
    state = Entry(trd, width=30)
    state.grid(row=4, column=1)
    zipcode = Entry(trd, width=30)
    zipcode.grid(row=5, column=1)
    delete_box = Entry(trd, width=30)
    delete_box.grid(row=9, column=1, pady=5)

    # Create Text Box Labels
    f_name_label = Label(trd, text="Listing Title")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(trd, text="Username")
    l_name_label.grid(row=1, column=0)
    address_label = Label(trd, text="Asset Listed")
    address_label.grid(row=2, column=0)
    city_label = Label(trd, text="Contact")
    city_label.grid(row=3, column=0)
    state_label = Label(trd, text="Listed By")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(trd, text="Offer Price")
    zipcode_label.grid(row=5, column=0)

    # Create Submit Button
    submit_btn = Button(trd, text="Add Listing", command=add)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Create a Query Button
    query_btn = Button(trd, text="Show All Listings", command=query)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)


