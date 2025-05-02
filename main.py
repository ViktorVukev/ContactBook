import csv
from tkinter import filedialog
from tkinter import *
from datetime import datetime
from tkinter import ttk
from tkcalendar import DateEntry

root = Tk()
root.title("Contact Manager")
root.geometry('1300x1000')
root.iconbitmap('contact_book.ico')

datas = []
melody_var = StringVar()
address = Text(root, height=5, width=40)
Number = StringVar()

def load_data():
    global datas
    try:
        with open('contacts.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            datas = [row for row in reader]
    except FileNotFoundError:
        pass

def save_data():
    with open('contacts.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(datas)

def add():
    global datas

    contact_data = [
        Name.get(),
        Mobile.get(),
        CompanyName.get(),
        Occupation.get(),
        CompanyAddress.get(),
        CompanyWebPage.get(),
        OtherPhone1.get(),
        OtherPhone2.get(),
        HomePhone.get(),
        OfficePhone.get(),
        PrivateEmail1.get(),
        PrivateEmail2.get(),
        OfficeEmail.get(),
        melody_var.get(),
        address.get("1.0", END).strip(),
        birthday_entry.get(),
        Notes.get(),
        SpouseName.get(),
        SpouseBirthday.get(),
        SpouseNotes.get(),
        Children1Name.get(),
        Children1Birthday.get(),
        Children1Notes.get(),
        Children2Name.get(),
        Children2Birthday.get(),
        Children2Notes.get()
    ]

    datas.append(contact_data)

    save_data()
    update_book()

def view():
    contact = datas[int(select.curselection()[0])]
    fields = [
        Name, Mobile, CompanyName, Occupation, CompanyAddress, CompanyWebPage,
        OtherPhone1, OtherPhone2, HomePhone, OfficePhone,
        PrivateEmail1, PrivateEmail2, OfficeEmail, Melody,
        Address, Birthday, Notes,
        SpouseName, SpouseBirthday, SpouseNotes,
        Children1Name, Children1Birthday, Children1Notes,
        Children2Name, Children2Birthday, Children2Notes
    ]
    for field, value in zip(fields, contact):
        field.set(value)

def delete():
    global datas
    if select.curselection():
        del datas[int(select.curselection()[0])]
        update_book()
        save_data()
        reset()

def reset():
    for var in all_vars:
        var.set('')

def update_book():
    select.delete(0, END)
    today = datetime.now().date()

    for contact in datas:
        name = contact[0]

        if len(contact) > 16:
            birthday_str = contact[15]
        else:
            birthday_str = ""

        display_name = name

        if birthday_str:
            try:
                birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()

                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                days_until_birthday = (birthday_this_year - today).days

                if days_until_birthday <= 10:
                    display_name += f"    🎂 in {days_until_birthday} days"

            except ValueError:
                print(f"Invalid birthday format for {name}: {birthday_str}")

        select.insert(END, display_name)

def export_contacts():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(datas)

def import_contacts():
    global datas
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            datas = [row for row in reader]
        update_book()
        save_data()

def search_contact():
    keyword = search_var.get().lower()
    select.delete(0, END)
    for contact in datas:
        if keyword in contact[0].lower():
            select.insert(END, contact[0])

def show_all_contacts():
    update_book()
    search_var.set('')

def export_all_brief():
    if not datas:
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            for contact in datas:
                f.write(f"Name: {contact[0]}, Mobile Phone: {contact[1]}\n")

def export_selected_full():
    if not select.curselection():
        return
    index = select.curselection()[0]
    contact = datas[index]
    fields = [
        "Name", "Mobile Phone", "Company Name", "Occupation", "Company Address", "Web Page",
        "Mobile Phone 2", "Mobile Phone 3", "Home Phone", "Office Phone",
        "Private Email 1", "Private Email 2", "Office Email",
        "Melody", "Other Address", "Birthday", "Notes",
        "Spouse Name", "Spouse Birthday", "Spouse Notes",
        "Child Name", "Child Birthday", "Child Notes"
    ]
    text = ""
    for field, value in zip(fields, contact):
        text += f"{field}: {value}\n"

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile=f"{contact[0]}_details.txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

Name = StringVar()
Mobile = StringVar()
CompanyName = StringVar()
Occupation = StringVar()
CompanyAddress = StringVar()
CompanyWebPage = StringVar()
OtherPhone1 = StringVar()
OtherPhone2 = StringVar()
HomePhone = StringVar()
OfficePhone = StringVar()
PrivateEmail1 = StringVar()
PrivateEmail2 = StringVar()
OfficeEmail = StringVar()
Melody = StringVar()
Address = StringVar()
Birthday = StringVar()
Notes = StringVar()
SpouseName = StringVar()
SpouseBirthday = StringVar()
SpouseNotes = StringVar()
Children1Name = StringVar()
Children1Birthday = StringVar()
Children1Notes = StringVar()
Children2Name = StringVar()
Children2Birthday = StringVar()
Children2Notes = StringVar()

all_vars = [
    Name, Mobile, CompanyName, Occupation, CompanyAddress, CompanyWebPage,
    OtherPhone1, OtherPhone2, HomePhone, OfficePhone,
    PrivateEmail1, PrivateEmail2, OfficeEmail, Melody,
    Address, Birthday, Notes,
    SpouseName, SpouseBirthday, SpouseNotes,
    Children1Name, Children1Birthday, Children1Notes,
    Children2Name, Children2Birthday, Children2Notes
]

labels = [
    "Name", "Mobile", "Company Name", "Occupation", "Company Address", "Company Web Page",
    "Other Phone 1", "Other Phone 2", "Home Phone", "Office Phone",
    "Private Email 1", "Private Email 2", "Office Email", "Melody",
    "Address", "Birthday", "Notes",
    "Spouse Name", "Spouse Birthday", "Spouse Notes",
    "Children 1 Name", "Children 1 Birthday", "Children 1 Notes",
    "Children 2 Name", "Children 2 Birthday", "Children 2 Notes"
]

frame_main = Frame(root)
frame_main.pack(pady=10, padx=10, fill=BOTH, expand=True)

frame_left_container = Frame(frame_main)
frame_left_container.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

canvas_left = Canvas(frame_left_container)
scrollbar_left = Scrollbar(frame_left_container, orient=VERTICAL, command=canvas_left.yview)
scrollable_frame_left = Frame(canvas_left)

scrollable_frame_left.bind(
    "<Configure>",
    lambda e: canvas_left.configure(
        scrollregion=canvas_left.bbox("all")
    )
)

canvas_left.create_window((0, 0), window=scrollable_frame_left, anchor="nw")
canvas_left.configure(yscrollcommand=scrollbar_left.set)

canvas_left.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar_left.pack(side=RIGHT, fill=Y)

frame_right = Frame(frame_main)
frame_right.pack(side=LEFT, fill=Y)

for idx, (text, var) in enumerate(zip(labels, all_vars)):
    if text == "Melody":
        Label(scrollable_frame_left, text=text, anchor='w', font='arial 10').grid(row=idx, column=0, sticky='w', pady=2)
        melody_combo = ttk.Combobox(scrollable_frame_left, textvariable=melody_var,
                                     values=["Melody 1", "Melody 2", "Melody 3"], width=40, state="readonly")
        melody_combo.grid(row=idx, column=1, pady=2)
    elif text == "Birthday":
        Label(scrollable_frame_left, text=text, anchor='w', font='arial 10').grid(row=idx, column=0, sticky='w', pady=2)
        birthday_entry = DateEntry(scrollable_frame_left, date_pattern='yyyy-mm-dd', width=40)
        birthday_entry.grid(row=idx, column=1, pady=2)
    else:
        Label(scrollable_frame_left, text=text, anchor='w', font='arial 10').grid(row=idx, column=0, sticky='w', pady=2)
        Entry(scrollable_frame_left, textvariable=var, width=43).grid(row=idx, column=1, pady=2)

frame_buttons = Frame(scrollable_frame_left)
frame_buttons.grid(row=len(labels), column=0, columnspan=2, pady=15)

btn_width = 15
Button(frame_buttons, text="Add", font="arial 12 bold", width=btn_width, command=add).grid(row=0, column=0, padx=5, pady=5)
Button(frame_buttons, text="View", font="arial 12 bold", width=btn_width, command=view).grid(row=0, column=1, padx=5, pady=5)
Button(frame_buttons, text="Delete", font="arial 12 bold", width=btn_width, command=delete).grid(row=0, column=2, padx=5, pady=5)
Button(frame_buttons, text="Reset", font="arial 12 bold", width=btn_width, command=reset).grid(row=0, column=3, padx=5, pady=5)
Button(frame_buttons, text="Export CSV", font="arial 12 bold", width=btn_width, command=export_contacts).grid(row=0, column=4, padx=5, pady=5)
Button(frame_buttons, text="Load CSV", font="arial 12 bold", width=btn_width, command=import_contacts).grid(row=0, column=5, padx=5, pady=5)

# RIGHT
search_var = StringVar()

frame_search = Frame(frame_right)
frame_search.pack(pady=10)

Entry(frame_search, textvariable=search_var, width=20, font='arial 12').grid(row=0, column=0, padx=5)
Button(frame_search, text="Search", font='arial 10', command=search_contact).grid(row=0, column=1, padx=5)
Button(frame_search, text="Show All", font='arial 10', command=show_all_contacts).grid(row=0, column=2, padx=5)
frame_export = Frame(frame_right)
frame_export.pack(pady=10)

Button(frame_export, text="Export All In Txt", font='arial 10', command=export_all_brief).grid(row=0, column=0, padx=5)
Button(frame_export, text="Export Selected In Txt", font='arial 10', command=export_selected_full).grid(row=0, column=1, padx=5)

Label(frame_right, text="Contacts", font="arial 14 bold").pack(pady=10)
scroll_bar = Scrollbar(frame_right, orient=VERTICAL)
select = Listbox(frame_right, yscrollcommand=scroll_bar.set, width=40, height=35, font='arial 10')
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=Y)

load_data()
update_book()

root.mainloop()
