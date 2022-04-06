from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

window = Tk()
window.title('Phone Book')
window.geometry("1000x550")
window.resizable("false", "false")


def query_database():
    # Clear the Treeview
    for record in my_tree.get_children():
        my_tree.delete(record)

    # Create a database or connect to one that exists
    conn = sqlite3.connect('users.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")
    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
        # increment counter
        count += 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


def search_records():
    lookup_record = search_entry.get()
    # close the search box
    search.destroy()

    # Clear the Treeview
    for record in my_tree.get_children():
        my_tree.delete(record)

    # Create a database or connect to one that exists
    conn = sqlite3.connect('users.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers WHERE last_name like ?", (lookup_record,))
    records = c.fetchall()

    # Add our data to the screen
    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
        # increment counter
        count += 1

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


def lookup_records():
    global search_entry, search

    search = Toplevel(window)
    search.title("Search")
    search.geometry("400x200")

    # Create label frame
    search_frame = LabelFrame(search, text="Last Name")
    search_frame.pack(padx=10, pady=10)

    # Add entry box
    search_entry = Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(pady=20, padx=20)

    # Add button
    search_button = Button(search, text="Search", command=search_records)
    search_button.pack(padx=20, pady=20)


# Add Fake Data
"""
data = [
	["TestName1", "TestSurname2", 1, "123 Test St.", "Test City", "qwerty123@mail.com", "+381 23 456 7890"],
	["John", "Smith", 2, "456 West St.", "Kharkiv", "uiop897@mail.com", "+385 24 967 4829"],
	["Tim", "Sweeney", 3, "789 Main St.", "Kyiv", "dfs3_inu34@mail.com", "+385 22 197 4780"],
	["Alex", "Doe", 4, "333 Top Way.", "Poltava", "34fKs1_J83jd@mail.com", "+380 43 168 2190"],
	["Robert", "Martin", 5, "887 Left St.", "Lviv", "f490JKWd3@mail.com", "+380 86 340 5299"],
	["Steve", "Price", 6, "1234 Some St.", "Odessa", "k94jfdK_df@mail.com", "+380 49 283 4020"],
	["Vlad", "Brown", 7, "666 Street St.", "Kryvyi Rih", "FUHWksw0l9d@mail.com", "+380 73 829 9435"],
	["Mark", "Zuckerberg", 8, "12 East St.", "New York", "39fjkKJFAf@mail.com", "+1 (646) 235-5678"],
	["John", "Romero", 9, "678 North St.", "Colorado", "f43_Wfkskef@mail.com", "+1 (652) 132-9768"],
	["Todd", "Hovard", 10, "9 South St.", "Pennsylvania", "fk9340kfkewfS_jkh675@mail.com", "+1 (923) 364-7623"],
    ["Steve", "Price", 11, "1234 Some St.", "Odessa", "k94jfdK_df@mail.com", "+380 49 283 4020"],
    ["Vlad", "Brown", 12, "666 Street St.", "Kryvyi Rih", "FUHWksw0l9d@mail.com", "+380 73 829 9435"],
    ["Mark", "Zuckerberg", 13, "12 East St.", "New York", "39fjkKJFAf@mail.com", "+1 (646) 235-5678"],
    ["John", "Romero", 14, "678 North St.", "Colorado", "f43_Wfkskef@mail.com", "+1 (652) 132-9768"],
    ["Todd", "Hovard", 15, "9 South St.", "Pennsylvania", "fk9340kfkewfS_jkh675@mail.com", "+1 (923) 364-7623"]
]
"""

# Create a database or connect to one that exists
conn = sqlite3.connect('users.db')

# Create a cursor instance
c = conn.cursor()

# Create Table
c.execute("""CREATE TABLE if not exists customers (
	first_name text,
	last_name text,
	id integer,
	address text,
	city text,
	email text,
	tel_num text)
	""")
# Add fake data to table
"""
for record in data:
	c.execute("INSERT INTO customers VALUES (:first_name, :last_name, :id, :address, :city, :email, :tel_num)",
		{
		'first_name': record[0],
		'last_name': record[1],
		'id': record[2],
		'address': record[3],
		'city': record[4],
		'email': record[5],
		'tel_num': record[6]
		}
		)
"""

# Commit changes
conn.commit()

# Close our connection
conn.close()

# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

# Create a Treeview Frame
tree_frame = Frame(window)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Columns
my_tree['columns'] = ("First Name", "Last Name", "ID", "Address", "City", "E-mail", "Tel. Num")

# Format Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("Address", anchor=CENTER, width=140)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("E-mail", anchor=CENTER, width=140)
my_tree.column("Tel. Num", anchor=CENTER, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Address", text="Address", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("E-mail", text="E-mail", anchor=CENTER)
my_tree.heading("Tel. Num", text="Tel. Num", anchor=CENTER)

# Add Record Entry Boxes
data_frame = LabelFrame(window, text="Info")
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label = Label(data_frame, text="First Name")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text="ID")
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

address_label = Label(data_frame, text="Address")
address_label.grid(row=1, column=0, padx=10, pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1, column=1, padx=10, pady=10)

city_label = Label(data_frame, text="City")
city_label.grid(row=1, column=2, padx=10, pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1, column=3, padx=10, pady=10)

email_label = Label(data_frame, text="E-mail")
email_label.grid(row=1, column=4, padx=10, pady=10)
email_entry = Entry(data_frame)
email_entry.grid(row=1, column=5, padx=10, pady=10)

telnum_label = Label(data_frame, text="Tel. Num")
telnum_label.grid(row=1, column=6, padx=10, pady=10)
telnum_entry = Entry(data_frame)
telnum_entry.grid(row=1, column=7, padx=10, pady=10)


# Move Row Up
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)


# Move Row Down
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)


# Remove one record
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

    # Create a database or connect to one that exists
    conn = sqlite3.connect('users.db')

    # Create a cursor instance
    c = conn.cursor()

    # Delete From Database
    c.execute("DELETE from customers WHERE oid=" + id_entry.get())

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Clear The Entry Boxes
    clear_entries()

    # Add a little message box
    messagebox.showinfo("Deleted", "Your Record Has Been Deleted!")


# Remove Many records
def remove_many():
    # Add a message box
    response = messagebox.askyesno("Attention!", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")

    # Add logic for message box
    if response == 1:
        # Designate selections
        x = my_tree.selection()

        # Create List of ID's
        ids_to_delete = []

        # Add selections to ids_to_delete list
        for record in x:
            ids_to_delete.append(my_tree.item(record, 'values')[2])

        # Delete From Treeview
        for record in x:
            my_tree.delete(record)

        # Create a database or connect to one that exists
        conn = sqlite3.connect('users.db')

        # Create a cursor instance
        c = conn.cursor()

        # Delete Everything From The Table
        c.executemany("DELETE FROM customers WHERE id = ?", [(a,) for a in ids_to_delete])

        # Reset List
        ids_to_delete = []

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear entry boxes if filled
        clear_entries()


# Remove all records
def remove_all():
    # Add a message box
    response = messagebox.askyesno("Attention!", "This Will Delete EVERYTHING From The Table\nAre You Sure?!")

    # Add logic for message box
    if response == 1:
        # Clear the Treeview
        for record in my_tree.get_children():
            my_tree.delete(record)

        # Create a database or connect to one that exists
        conn = sqlite3.connect('users.db')

        # Create a cursor instance
        c = conn.cursor()

        # Delete Everything From The Table
        c.execute("DROP TABLE customers")

        # Commit changes
        conn.commit()

        # Close our connection
        conn.close()

        # Clear entry boxes if filled
        clear_entries()

        # Recreate The Table
        create_table_again()


# Clear entry boxes
def clear_entries():
    # Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    email_entry.delete(0, END)
    telnum_entry.delete(0, END)


# Select Record
def select_record(e):
    # Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    email_entry.delete(0, END)
    telnum_entry.delete(0, END)

    # Grab record Number
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    # outputs to entry boxes
    fn_entry.insert(0, values[0])
    ln_entry.insert(0, values[1])
    id_entry.insert(0, values[2])
    address_entry.insert(0, values[3])
    city_entry.insert(0, values[4])
    email_entry.insert(0, values[5])
    telnum_entry.insert(0, values[6])


# Update record
def update_record():
    # Grab the record number
    selected = my_tree.focus()
    # Update record
    my_tree.item(selected, text="", values=(fn_entry.get(), ln_entry.get(), id_entry.get(), address_entry.get(), city_entry.get(), email_entry.get(), telnum_entry.get(),))

    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect('users.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("""UPDATE customers SET
		first_name = :first,
		last_name = :last,
		address = :address,
		city = :city,
		email = :email,
		tel_num = :tel_num
		WHERE oid = :oid""",
              {
                  'first': fn_entry.get(),
                  'last': ln_entry.get(),
                  'address': address_entry.get(),
                  'city': city_entry.get(),
                  'email': email_entry.get(),
                  'tel_num': telnum_entry.get(),
                  'oid': id_entry.get(),
              })

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    email_entry.delete(0, END)
    telnum_entry.delete(0, END)


# add new record to database
def add_record():
    # Update the database
    # Create a database or connect to one that exists
    conn = sqlite3.connect('users.db')

    # Create a cursor instance
    c = conn.cursor()

    # Add New Record
    c.execute("INSERT INTO customers VALUES (:first, :last, :id, :address, :city, :email, :tel_num)",
              {
                  'first': fn_entry.get(),
                  'last': ln_entry.get(),
                  'id': id_entry.get(),
                  'address': address_entry.get(),
                  'city': city_entry.get(),
                  'email': email_entry.get(),
                  'tel_num': telnum_entry.get(),
              })

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()

    # Clear entry boxes
    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    id_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    email_entry.delete(0, END)
    telnum_entry.delete(0, END)

    # Clear The Treeview Table
    my_tree.delete(*my_tree.get_children())

    # Run to pull data from database on start
    query_database()


def create_table_again():
    # Create a database or connect to one that exists
    conn = sqlite3.connect('users.db')

    # Create a cursor instance
    c = conn.cursor()

    # Create Table
    c.execute("""CREATE TABLE if not exists customers (
		first_name text,
		last_name text,
		id integer,
		address text,
		city text,
		email text,
		tel_num text)
		""")

    # Commit changes
    conn.commit()

    # Close our connection
    conn.close()


# Add Menu
my_menu = Menu(window)
window.config(menu=my_menu)

# Configure our menu
option_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Options", menu=option_menu)
# Drop down menu
option_menu.add_command(label="Add record", command=add_record)
option_menu.add_command(label="Update record", command=update_record)
option_menu.add_separator()
option_menu.add_command(label="Remove all", command=remove_all)
option_menu.add_command(label="Remove one", command=remove_one)
option_menu.add_command(label="Remove many", command=remove_many)
option_menu.add_separator()
option_menu.add_command(label="Clear", command=clear_entries)
option_menu.add_separator()
option_menu.add_command(label="Exit", command=window.quit)

# Search Menu
search_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Search", menu=search_menu)
# Drop down menu
search_menu.add_command(label="Search", command=lookup_records)
search_menu.add_separator()
search_menu.add_command(label="Reset", command=query_database)


# Add Buttons
button_frame = LabelFrame(window, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record", command=add_record)
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

move_up_button = Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

# Run to pull data from database on start
query_database()

window.mainloop()
