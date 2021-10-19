import tkinter as tk
from tkinter import *
from functions import *
from DesignFunctions import *
import tkinter.messagebox as err_massage


class patient_page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Patient Page'

        backGround_image_and_text(self, 'images/5.gif', 'Patient Page')

        # self.listbox = Listbox(self, width=58, height=24)
        # self.listbox.place(x=20, y=80)
        self.listBox = self.scrollbar_for_listbox_right()
        self.listBox = self.scrollbar_for_listbox_top()
        self.update_show_listBox()

        self.Buttons('Hospital Page', lambda: controller.show_frames(
            'hospital_page'), 15, 20, 480)
        self.Buttons('Add Patient', lambda: controller.show_frames(
            'add_patient'), 12, 140, 480)
        self.Buttons('Search Patient', None, 18, 237, 480)

    def update_show_listBox(self):
        patient_list = LoadPatients()
        self.listBox.delete(0, END)
        i = 1
        for item in patient_list:
            self.listBox.insert(END, f' {i} . {item}')
            i += 1

    def Buttons(self, button_text, Command, Width, X, Y):
        Button(self, text=button_text, command=Command,
               width=Width).place(x=X, y=Y)

    def scrollbar_for_listbox_right(self):
        scrollbar = Scrollbar(self)
        listBox = Listbox(self, width=58, height=24,
                          yscrollcommand=scrollbar.set)
        scrollbar.config(command=listBox.yview)
        scrollbar.place(x=375, y=80, height=388)
        listBox.place(x=20, y=80)
        return listBox

    def scrollbar_for_listbox_top(self):
        scrollbar = Scrollbar(self, orient='horizontal')
        listBox = Listbox(self, width=58, height=24,
                          yscrollcommand=scrollbar.set)
        scrollbar.config(command=listBox.xview)
        scrollbar.place(x=22, y=60, width=350)
        listBox.place(x=20, y=80)
        return listBox


class add_patient(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Add Patient'
        self.backGround_image_and_texts('images/7.gif')

        self.Entry_1 = self.Entries(20, 130, 345)
        self.Entry_2 = self.Entries(20, 130, 395)
        self.Entry_3 = self.Entries(20, 130, 445)
        self.Entry_4 = self.Entries(20, 410, 345)
        self.Entry_5 = self.Entries(20, 410, 395)

        self.sickness_text = self.scrollbar_for_text()

        self.Buttons('Back to Patient Page', lambda: controller.show_frames(
            self.back_to_patient_page()), 20, 20, 500)
        self.Buttons('Save', lambda: controller.show_frames(
            self.get_entries(controller)), 18, 750, 500)

    def backGround_image_and_texts(self, photo):
        self.backgrandImage = PhotoImage(file=photo)
        canvas = Canvas(self)
        canvas.pack(side='top', fill='both', expand=True)
        canvas.create_image(0, 0, image=self.backgrandImage, anchor="nw")

        self.labels(canvas, 'Patient Information', 450, 50, 24)
        self.labels(canvas, 'First Name :', 80, 350, 11)
        self.labels(canvas, 'Last Name :', 80, 400, 11)
        self.labels(canvas, 'Age :', 55, 450, 11)
        self.labels(canvas, "Doctor's Name :", 340, 350, 11)
        self.labels(canvas, 'National Number :', 345, 400, 11)
        self.labels(canvas, 'Sickness :', 317, 450, 11)

    def labels(self, Canvas, text, x, y, font_size):
        Canvas.create_text(x, y, text=text,
                           font=("Times New Roman", font_size, BOLD), activefill='blue',
                           disabledfill='red', fill='red')

    def Entries(self, Width, X, Y):
        entry = Entry(self, width=Width)
        entry.place(x=X, y=Y)
        return entry

    def get_entries(self, controller):
        get_entry1 = self.Entry_1.get()
        get_entry2 = self.Entry_2.get()
        get_entry3 = self.Entry_3.get()
        get_entry4 = self.Entry_4.get()
        get_entry5 = self.Entry_5.get()
        get_entry6 = self.sickness_text.get("1.0", END)
        massege_error = ReceptionPatient(FirstName=get_entry1, LastName=get_entry2, Age=get_entry3,
                                         VisitorDoctorNationalNumber=get_entry4, NationalNumber=get_entry5,
                                         Sickness=get_entry6)

        confirm_for_save = self.show_errors(massege_error)
        if confirm_for_save is True:
            controller.frames['patient_page'].update_show_listBox()
            self.delete_entries()
            return 'patient_page'
        else:
            return 'add_patient'

    def delete_entries(self):
        self.Entry_1.delete(0, END)
        self.Entry_2.delete(0, END)
        self.Entry_3.delete(0, END)
        self.Entry_4.delete(0, END)
        self.Entry_5.delete(0, END)
        self.sickness_text.delete("1.0", END)

    def Buttons(self, button_text, Command, Width, X, Y):
        Button(self, text=button_text, command=Command,
               width=Width).place(x=X, y=Y)

    def scrollbar_for_text(self):
        scrollbar = Scrollbar(self)
        text = Text(self, height=5, width=30, yscrollcommand=scrollbar.set)
        scrollbar.config(command=text.yview)
        scrollbar.place(x=660, y=435, height=85)
        text.place(x=410, y=435)
        return text

    def show_errors(self, error):
        if error is not True:
            err_massage.showerror('Error', error)
            return False
        else:
            err_massage.showinfo('Confirm', 'Save Information Successful')
            return True

    def back_to_patient_page(self):
        self.delete_entries()
        return 'patient_page'


# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Combobox Widget')


# def month_changed(event):
#     msg = f'You selected {month_cb.get()}!'
#     showinfo(title='Result', message=msg)


# # month of year
# months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# label = ttk.Label(text="Please select a month:")
# label.pack(fill='x', padx=5, pady=5)

# # create a combobox
# selected_month = tk.StringVar()

# month_cb = ttk.Combobox(root, textvariable=selected_month)
# month_cb['values'] = months
# month_cb['state'] = 'readonly'  # normal
# month_cb.pack(fill='x', padx=5, pady=5)

# month_cb.bind('<<ComboboxSelected>>', month_changed)

# root.mainloop()


