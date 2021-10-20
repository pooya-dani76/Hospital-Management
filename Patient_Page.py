
import tkinter as tk
from tkinter import *
from functions import *
from DesignFunctions import *
import tkinter.messagebox as err_massage
from tkinter import ttk
from tkinter.messagebox import showinfo


class patient_page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Patient Page'

        backGround_image_and_text(self, 'images/5.gif', 'Patient Page')

        self.listBox = self.scrollbar_for_listbox_right()
        self.listBox.bind('<<ListboxSelect>>',
                          lambda x: self.item_selected(even=None, controller=controller))
        self.update_show_listBox()

        self.Buttons('Hospital Page', lambda: controller.show_frames(
            'hospital_page'), 15, 20, 480)
        self.Buttons('Add Patient', lambda: controller.show_frames(
            'add_patient'), 12, 140, 480)
        self.Buttons('Search Patient',
                     lambda: self.open_search_window(), 18, 237, 480)

    def x(self, controller):
        self.switch_page = controller.show_frames('hospital_page')

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
        patient_list_var = StringVar(value=patient_list)

        scrollbar = Scrollbar(self)
        listBox = Listbox(self, width=58, height=24,
                          yscrollcommand=scrollbar.set,
                          listvariable=patient_list_var, selectmode='extended',)
        scrollbar.config(command=listBox.yview)
        scrollbar.place(x=375, y=80, height=388)
        listBox.place(x=20, y=80)
        return listBox

    def open_search_window(self):
        mainWindow = search_patient(self)
        mainWindow.grab_set()

    def item_selected(self, controller, even):
        patient_list = LoadPatients()
        selected_indices = self.listBox.curselection()
        controller.show_frames('add_patient')

        # selected_langs = ",".join([self.listBox.get(i)
        #                           for i in selected_indices])
        # msg = f'You selected: {selected_langs}'
        # print(type(patient_list[selected_indices[0]]))
        # print(patient_list)
        print(patient_list[selected_indices[0]].FirstName)


class add_patient(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Add Patient'
        self.backGround_image_and_texts('images/7.gif')

        self.Entry_1 = self.Entries(20, 130, 345)
        self.Entry_2 = self.Entries(20, 130, 395)
        self.Entry_3 = self.Entries(20, 130, 445)
        self.Entry_4 = drop_down(self).VisitorDoctorNationalNumber_cb
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
        confirm_for_save = False
        get_entry1 = self.Entry_1.get()
        get_entry2 = self.Entry_2.get()
        get_entry3 = self.Entry_3.get()
        get_entry4 = self.show_doctor_name_error()
        if get_entry4 is not False:
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
        self.Entry_4.set('')
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

    def show_doctor_name_error(self):
        try:
            get_entry4 = list(filter(lambda x:  x.id == int(
                self.Entry_4.get().split('.')[0]), LoadDoctors()))[0].NationalNumber
            return get_entry4
        except:
            err_massage.showerror("Doctor's Name Error",
                                  'Please Select a Doctor ')
            return False


class search_patient(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.position()

        self.labels('Search by Firstname :', 5, 15)
        self.labels('Search by Lastname :', 5, 60)

        self.entry1 = self.entries(25, 132, 15)
        self.entry2 = self.entries(25, 132, 60)

        self.button1 = self.buttons('Done', 8, None, 230, 120)
        self.button2 = self.buttons('Cancel', 8, None, 160, 120)

    def position(self):
        w = 300
        h = 150
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/8)
        y = (hs/50*28) - (h/2)
        self.title('Search')
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(width=False, height=False)

    def labels(self, label_text, X, Y):
        label = Label(self, text=label_text, font=("Helvetica", 8, 'bold'))
        label.place(x=X, y=Y)

    def entries(self, Width, X, Y):
        entry = Entry(self, width=Width)
        entry.place(x=X, y=Y)

    def buttons(self, button_text, Width, Command, X, Y):
        button = Button(self, text=button_text, width=Width)
        button.place(x=X, y=Y)


class drop_down:
    def __init__(self, parent):

        selected_VisitorDoctorNationalNumber = StringVar()

        self.VisitorDoctorNationalNumber_cb = ttk.Combobox(
            parent, textvariable=selected_VisitorDoctorNationalNumber, width=20, height=5)
        self.VisitorDoctorNationalNumber_cb['values'] = VisitorDoctorNationalNumber_list
        self.VisitorDoctorNationalNumber_cb['state'] = 'readonly'
        self.VisitorDoctorNationalNumber_cb.place(x=408, y=340)
        self.VisitorDoctorNationalNumber_cb.bind(
            '<<ComboboxSelected>>',self.VisitorDoctorNationalNumber_changed)

    def VisitorDoctorNationalNumber_changed(self, event):
        msg = f'You selected {self.VisitorDoctorNationalNumber_cb.get()}!'
        showinfo(title='Result', message=msg)
        print(list(filter(lambda x:  x.id == int(self.VisitorDoctorNationalNumber_cb.get(
        ).split('.')[0]), LoadDoctors()))[0].NationalNumber)
        # print(self.VisitorDoctorNationalNumber_cb.get().split('.')[0])


VisitorDoctorNationalNumber_list = list(
    map(lambda x: f'{x.id}. Dr.{x.FirstName} {x.LastName}', LoadDoctors()))
