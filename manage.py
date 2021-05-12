from tkinter import *
import accounthome
import signin
import sqlite3
#base is mod instead of root

#'get'username in mgasset from accounthome
def mgasset(get):
    mod = Toplevel()
    mod.title('Manage Assets')
    mod.geometry("1100x750")

    # Create Update function to update a record
    def update():
        # Create a database or connect to one
        conn = sqlite3.connect('asset.db')
        # Create cursor
        c = conn.cursor()

        record_id = delete_box.get()

        c.execute("""UPDATE Asset SET
    		assetname = :first,
    		assettype = :last,
    		heldby = :address,
    		detail = :city,
    		yoy = :state,
    		value = :zipcode 
    		WHERE oid = :oid""",
                  {
                      'first': f_name_editor.get(),
                      'last': l_name_editor.get(),
                      'address': address_editor.get(),
                      'city': city_editor.get(),
                      'state': state_editor.get(),
                      'zipcode': zipcode_editor.get(),
                      'oid': record_id
                  })

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        editor.destroy()
        mod.deiconify()

    # Create Edit function to update a record
    def edit():
        mod.withdraw()
        global editor
        editor = Tk()
        editor.title('Update Asset Details')

        editor.geometry("400x300")
        # Create a database or connect to one
        conn = sqlite3.connect('asset.db')
        # Create cursor
        c = conn.cursor()

        record_id = delete_box.get()
        # Query the database
        c.execute("SELECT * FROM Asset WHERE oid =  :record_id AND heldby= :get",{'record_id':record_id,'get':get})  #UP
        records = c.fetchall()

        # Create Global Variables for text box names
        global f_name_editor
        global l_name_editor
        global address_editor
        global city_editor
        global state_editor
        global zipcode_editor

        # Create Text Boxes
        f_name_editor = Entry(editor, width=30)
        f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        l_name_editor = Entry(editor, width=30)
        l_name_editor.grid(row=1, column=1)
        address_editor = Entry(editor, width=30)
        address_editor.grid(row=2, column=1)
        city_editor = Entry(editor, width=30)
        city_editor.grid(row=3, column=1)
        state_editor = Entry(editor, width=30)
        state_editor.grid(row=4, column=1)
        zipcode_editor = Entry(editor, width=30)
        zipcode_editor.grid(row=5, column=1)

        # Create Text Box Labels
        f_name_label = Label(editor, text="Asset Name")
        f_name_label.grid(row=0, column=0, pady=(10, 0))
        l_name_label = Label(editor, text="Asset Type")
        l_name_label.grid(row=1, column=0)
        address_label = Label(editor, text="Held By")
        address_label.grid(row=2, column=0)
        city_label = Label(editor, text="Asset Details")
        city_label.grid(row=3, column=0)
        state_label = Label(editor, text="Year On Year Change")
        state_label.grid(row=4, column=0)
        zipcode_label = Label(editor, text="Current Valuation")
        zipcode_label.grid(row=5, column=0)

        # Loop thru results
        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            #address_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            state_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])

        # Create a Save Button To Save edited record
        edit_btn = Button(editor, text="Save", command=update)
        edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # Create Function to Delete A Record
    def delete():
        # Create a database or connect to one
        conn = sqlite3.connect('asset.db')
        # Create cursor
        c = conn.cursor()

        # Delete a record
        c.execute("DELETE from Asset WHERE oid = " + delete_box.get())

        delete_box.delete(0, END)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

    # Create Submit Function For database
    def submit():
        # Create a database or connect to one
        conn = sqlite3.connect('asset.db')
        # Create cursor
        c = conn.cursor()

        # Insert Into Table
        c.execute("INSERT INTO Asset VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'address':get,
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
        #address.delete(0, END)#replaced because autofill username
        city.delete(0, END)
        state.delete(0, END)
        zipcode.delete(0, END)

    # Create Query Function
    #bring username for personalised results
    def query():
        # Create a database or connect to one
        conn = sqlite3.connect('asset.db')
        # Create cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *, oid FROM Asset WHERE heldby = :get",{'get':get})
        records = c.fetchall()
        # print(records)

        # Loop Thru Results
        print_records = ''
        for record in records:
            print_records += str(record[6]) + " | " + str(record[0]) + " | " + str(record[1]) +  " | " + str(record[3]) +" | " + str(record[4]) +" | " + str(record[5])+"\n"+"\n"

        query_label = Label(mod, text=print_records)
        query_label.grid(row=12, column=0, columnspan=12)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

    # Create Text Boxes
    f_name = Entry(mod, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name = Entry(mod, width=30)
    l_name.grid(row=1, column=1)
    #address = Entry(mod, width=30)#replaced because autofill username
    #address.grid(row=2, column=1)#replaced because autofill username
    city = Entry(mod, width=40)
    city.grid(row=3, column=1)
    state = Entry(mod, width=30)
    state.grid(row=4, column=1)
    zipcode = Entry(mod, width=30)
    zipcode.grid(row=5, column=1)
    delete_box = Entry(mod, width=30)
    delete_box.grid(row=9, column=1, pady=5)

    # Create Text Box Labels
    f_name_label = Label(mod, text="Asset Name ")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(mod, text="Asset Type")
    l_name_label.grid(row=1, column=0)
    #address_label = Label(mod, text="Held By (Username)")#replaced because autofill username
    #address_label.grid(row=2, column=0)#replaced because autofill username
    city_label = Label(mod, text="Details")
    city_label.grid(row=3, column=0)
    state_label = Label(mod, text="Year on Year Change")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(mod, text="Current Valuation")
    zipcode_label.grid(row=5, column=0)
    delete_box_label = Label(mod, text="Select ID")
    delete_box_label.grid(row=9, column=0, pady=5)

    # Create Submit Button
    submit_btn = Button(mod, text="Add Record To Database", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Create a Query Button
    query_btn = Button(mod, text="View All Asset Held", command=query)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    # Create A Delete Button
    delete_btn = Button(mod, text="Delete Record", command=delete)
    delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

    # Create an Update Button
    edit_btn = Button(mod, text="Edit Record", command=edit)
    edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)
