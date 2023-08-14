from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
from PIL import ImageTk

data_file = 'employee_data.json'
array = []

main = Tk()
main.title("Employee Management")
main.geometry('1174x680')


#creat Frame
layoutFrame = Frame(main)
layoutFrame.place(x=640, y=700)

leftFrame = Frame(main)
leftFrame.place(x=50, y=80, width=300, height=600)

rightFrame = Frame(main)
rightFrame.place(x=350, y=80, width=820, height=600)

#create columns
columns = ('name', 'id', 'gender', 'age', 'contact')
table = ttk.Treeview(rightFrame, columns=columns, show='headings')
table.heading('name', text='Name', )
table.heading('id', text='ID')
table.heading('gender', text='Gender')
table.heading('age', text='Age')
table.heading('contact', text='Contact')
table['show'] = 'headings'
table.pack(fill=BOTH, expand=1)

#Title
title = Label(layoutFrame, text='Employee Management')
title.grid(row=0, columnspan=2)

#logo_image
logo_company = ImageTk.PhotoImage(file='/Users/nguyennhi/Downloads/8fdd82fb737eb9af651088d577d56c08-2.png', master=main)
logo_companyLabel = Label(leftFrame, image=logo_company, text='OOO', compound=LEFT,
                          font=('times new roman', 30, 'bold'))
logo_companyLabel.image = logo_company
logo_companyLabel.grid(row=0, column=0)

#def
def read_data():
    global array
    try:
        with open(data_file, 'r', encoding='utf-8') as myfile:
            array = json.load(myfile)
    except Exception as e:
        print(f"Error reading file: {e}")
        messagebox.showwarning(title='Error', message='Error reading file')
        array = []


def save_data():
    try:
        with open(data_file, 'w', encoding='utf-8') as myfile:
            json.dump(array, myfile, indent=4)
    except Exception as e:
        print(f"Error saving file: {e}")
        messagebox.showwarning(title='Error', message='Error saving file')

def clear_tree_view(mytree):
    for item in mytree.get_children():
        mytree.delete(item)

def display():
    clear_tree_view(table) 

    if len(array) == 0:
        read_data()  

    for item in array:
        table.insert("", END, values=(item['name'], item['employee_id'], item['gender'], item['age'], item['contact']))



def find_employee(employee_id):
    for employee in array:
        if employee['employee_id'] == employee_id:
            return employee
    return None


def add_employee():
    def add_data():
        existing_employee = find_employee(idEntry.get())
        if existing_employee is not None:
            messagebox.showwarning(message='Employee with ID already exists')
        else:
            obj = {
                'name': nameEntry.get(),
                'employee_id': idEntry.get(),
                'age': ageEntry.get(),
                'gender': gender_cbb.get(),
                'contact': contactEntry.get()
            }
            array.append(obj)
            save_data()
            display()

            nameEntry.delete(0, END)
            idEntry.delete(0, END)
            ageEntry.delete(0, END)
            gender_cbb.delete(0, END)
            contactEntry.delete(0, END)

            add_window.destroy()

    add_window = Toplevel(main)

    nameLabel = Label(add_window, text='Name')
    nameLabel.grid(row=4, column=0)
    name_value = StringVar()
    nameEntry = Entry(add_window, textvariable=name_value)
    nameEntry.grid(row=4, column=1)

    idLabel = Label(add_window, text='ID')
    id_value = IntVar()
    idLabel.grid(row=0, column=0)
    idEntry = Entry(add_window, textvariable=id_value)
    idEntry.grid(row=0, column=1)

    genderLabel = Label(add_window, text='Gender')
    genderLabel.grid(row=1, column=0)
    gender_value = StringVar()
    gender_cbb = ttk.Combobox(add_window, textvariable=gender_value)
    gender_cbb.grid(row=1, column=1)
    gender_cbb['values'] = ['Male', 'Female', 'None']

    ageLabel = Label(add_window, text='Age')
    ageLabel.grid(row=2, column=0)
    age_value = IntVar()
    ageEntry = Entry(add_window, textvariable=age_value)
    ageEntry.grid(row=2, column=1)

    contactLabel = Label(add_window, text='Phone')
    contactLabel.grid(row=3, column=0)
    contact_value = IntVar()
    contactEntry = Entry(add_window, textvariable=contact_value)
    contactEntry.grid(row=3, column=1)

    addButton = ttk.Button(add_window, text='ADD', command=add_data)
    addButton.grid(row=5, columnspan=2)


def delete_employee():
    selected_item = table.selection()

    if selected_item:
        selected_employee_id = table.item(selected_item, "values")[1]
        selected_employee = find_employee(selected_employee_id)

        if selected_employee:
            array.remove(selected_employee)
            table.delete(selected_item)
            save_data()
        else:
            messagebox.showwarning("Error", "Selected employee not found.")
    else:
        messagebox.showwarning("Error", "Select an employee to delete.")


def search_employee():
    def search_data():
        employee_id = idEntry.get()
        found_employee = None
        for employee in array:
            if employee['employee_id'] == employee_id:
                found_employee = employee
                break

        if found_employee:
            messagebox.showinfo("Employee found", 'Employee found ')
            update_table(found_employee)
        else:
            messagebox.showerror('Success', 'Employee not found')


    def update_table(employee):
        table.delete(*table.get_children())
        table.insert('', END, values=(
        employee['name'], employee['employee_id'], employee['gender'], employee['age'], employee['contact']))

    search_window = Toplevel(main)

    idLabel = Label(search_window, text='ID')
    id_value = IntVar()
    idLabel.grid(row=0, column=0)
    idEntry = Entry(search_window, textvariable=id_value)
    idEntry.grid(row=0, column=1)

    searchButton = ttk.Button(search_window, text='Search', command=search_data)
    searchButton.grid(row=1, columnspan=2)


def update_employee():
    def update_data():
        selected_item = table.selection()

        if selected_item:
            selected_employee_id = table.item(selected_item, "values")[1]
            selected_employee = find_employee(selected_employee_id)

            if selected_employee:
                selected_employee['name'] = nameEntry.get()
                selected_employee['employee_id'] = idEntry.get()
                selected_employee['age'] = ageEntry.get()
                selected_employee['gender'] = gender_cbb.get()
                selected_employee['contact'] = contactEntry.get()

                save_data()
                display()
                update_window.destroy()
            else:
                messagebox.showwarning("Error", "Selected employee not found.")
        else:
            messagebox.showwarning("Error", "Select an employee to update.")

    update_window = Toplevel(main)

    nameLabel = Label(update_window, text='Name')
    nameLabel.grid(row=4, column=0)
    name_value = StringVar()
    nameEntry = Entry(update_window, textvariable=name_value)
    nameEntry.grid(row=4, column=1)

    idLabel = Label(update_window, text='ID')
    id_value = IntVar()
    idLabel.grid(row=0, column=0)
    idEntry = Entry(update_window, textvariable=id_value)
    idEntry.grid(row=0, column=1)

    genderLabel = Label(update_window, text='Gender')
    genderLabel.grid(row=1, column=0)
    gender_value = StringVar()
    gender_cbb = ttk.Combobox(update_window, textvariable=gender_value)
    gender_cbb.grid(row=1, column=1)
    gender_cbb['values'] = ['Male', 'Female', 'None']

    ageLabel = Label(update_window, text='Age')
    ageLabel.grid(row=2, column=0)
    age_value = IntVar()
    ageEntry = Entry(update_window, textvariable=age_value)
    ageEntry.grid(row=2, column=1)

    contactLabel = Label(update_window, text='Phone')
    contactLabel.grid(row=3, column=0)
    contact_value = IntVar()
    contactEntry = Entry(update_window, textvariable=contact_value)
    contactEntry.grid(row=3, column=1)

    updateButton = ttk.Button(update_window, text='Update', command=update_data)
    updateButton.grid(row=5, columnspan=2)



def exit_employee():
    main.destroy()

#create Button
addButton = ttk.Button(leftFrame, text='Add Employee', width=25, command=add_employee).grid(row=1, column=0, pady=20)
delButton = ttk.Button(leftFrame, text='Delete Employee', width=25, command=delete_employee).grid(row=2, column=0,pady=20)
updateButton = ttk.Button(leftFrame, text='Update', width=25, command=update_employee).grid(row=3, column=0, pady=20)
searchButton = ttk.Button(leftFrame, text='Search', width=25, command=search_employee).grid(row=4, column=0, pady=20)
exitButton = ttk.Button(leftFrame, text='Exit', width=25, command=exit_employee).grid(row=5, column=0, pady=20)

#end
read_data()
display()
main.mainloop()