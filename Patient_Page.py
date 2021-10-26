from tkinter import *
from functions import *
from DesignFunctions import *
import tkinter.messagebox as err_massage
from tkinter import ttk
from tkinter.messagebox import showinfo
import functions as fu
from Pages_Help import *


class patient_page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Patient Page'

        backGround_image_and_text(self, 'images/5.gif', 'Patient Page')

        self.listBox = self.scrollbar_for_listbox_right()
        self.listBox.bind('<Double-1>',
                          lambda x: self.item_selected(even=None, controller=controller))
        self.update_show_listBox()

        self.Buttons('Back', lambda: controller.show_frames(
            'hospital_page'), 15, 20, 480)
        self.Buttons('Add Patient', lambda: controller.show_frames(
            'add_patient'), 12, 140, 480)
        self.Buttons('Search Patient',
                     lambda: self.open_search_window(controller), 18, 237, 480)
        self.Buttons('Show All Patients',
                     lambda: self.update_show_listBox(), 49, 20, 510)
        show_help_button = Button(self,text='Help',command=lambda: self.show_help(
            parent, controller),width=3,height=0)
        show_help_button.place(x=10,y=10)

    def show_help(self, parent, controller):
        A = pages_help(parent, controller, PatientPageHelp,
                       'images/5.gif', 'patient_page', 90, 16, 130, 295, 10, 518, 10)
        A.grid(row=0, column=0, sticky="nsew")
        A.tkraise()

    def update_show_listBox(self):
        fu.patient_list = LoadPatients()
        self.listBox.delete(0, END)
        if len(fu.patient_list) == 0:
            self.listBox.insert(
                END, '             \
                                List is Empty !!!')
        else:
            i = 1
            for item in fu.patient_list:
                self.listBox.insert(END, f' {i} . {item}')
                i += 1

    def show_listBox_for_search(self, searchList):
        fu.patient_list = searchList
        self.listBox.delete(0, END)
        i = 1
        for item in fu.patient_list:
            self.listBox.insert(END, f' {i} . {item}')
            i += 1

    def Buttons(self, button_text, Command, Width, X, Y):
        Button(self, text=button_text, command=Command,
               width=Width).place(x=X, y=Y)

    def scrollbar_for_listbox_right(self):
        patient_list_var = StringVar(value=fu.patient_list)

        scrollbar = Scrollbar(self)
        listBox = Listbox(self, width=58, height=24,
                          yscrollcommand=scrollbar.set,
                          listvariable=patient_list_var,
                          selectmode='single', activestyle='none')
        scrollbar.config(command=listBox.yview)
        scrollbar.place(x=375, y=80, height=388)
        listBox.place(x=20, y=80)
        return listBox

    def open_search_window(self, controller):
        if len(fu.patient_list) == 0:
            err_massage.showerror(
                'Error', 'There is not any Patient in List !!!')
        else:
            mainWindow = search_patient(self, controller)
            mainWindow.grab_set()

    def item_selected(self, controller, even):
        global selected_indices
        selected_indices = self.listBox.curselection()
        index = list(filter(lambda x: x.NationalNumber ==
                            fu.patient_list[selected_indices[0]].VisitorDoctorNationalNumber, LoadDoctors()))[0]
        controller.show_frames('delete_and_update_patient')

        self.delete_entries_of_selected_patient(controller)

        controller.frames['delete_and_update_patient'].Entry_1.insert(
            END, fu.patient_list[selected_indices[0]].FirstName)
        controller.frames['delete_and_update_patient'].Entry_2.insert(
            END, fu.patient_list[selected_indices[0]].LastName)
        controller.frames['delete_and_update_patient'].Entry_3.insert(
            END, fu.patient_list[selected_indices[0]].Age)
        controller.frames['delete_and_update_patient'].Entry_4.set(
            f'{index.id}. Dr.{index.FirstName} {index.LastName}'
        )
        controller.frames['delete_and_update_patient'].Entry_5.insert(
            END, fu.patient_list[selected_indices[0]].NationalNumber)
        controller.frames['delete_and_update_patient'].sickness_text.insert(
            END, fu.patient_list[selected_indices[0]].Sickness)

    def delete_entries_of_selected_patient(self, controller):
        controller.frames['delete_and_update_patient'].Entry_1.delete(0, END)
        controller.frames['delete_and_update_patient'].Entry_2.delete(0, END)
        controller.frames['delete_and_update_patient'].Entry_3.delete(0, END)
        controller.frames['delete_and_update_patient'].Entry_5.delete(0, END)
        controller.frames['delete_and_update_patient'].sickness_text.delete(
            '1.0', END)


class add_patient(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Add Patient'
        self.backGround_image_and_texts('images/7.gif')

        self.Entry_1 = self.Entries(20, 130, 345)
        self.Entry_2 = self.Entries(20, 130, 395)
        self.Entry_3 = self.Entries(20, 130, 445)
        self.Entry_4 = patient_drop_down(self).VisitorDoctorNationalNumber_cb
        self.Entry_5 = self.Entries(20, 410, 395)

        self.sickness_text = self.scrollbar_for_text()

        self.b1 = self.Buttons('Back', lambda: controller.show_frames(
            self.back_to_patient_page()), 20, 20, 500)
        self.Buttons('Save', lambda: controller.show_frames(
            self.get_entries(controller)), 18, 750, 500)

        show_help_button = Button(self,text='Help',command=lambda: self.show_help(
            parent, controller),width=3,height=0)
        show_help_button.place(x=10,y=10)

    def show_help(self, parent, controller):
        A = pages_help(parent, controller, AddPatientsHelp,
                       'images/7.gif', 'add_patient', 90, 25, 130, 160, 10, 518, 10)
        A.grid(row=0, column=0, sticky="nsew")
        A.tkraise()

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
        get_entry4 = self.show_doctor_name_error()
        if get_entry4 is not False:
            get_entry5 = self.Entry_5.get()
            get_entry6 = self.sickness_text.get("1.0", END)

            try:
                CheckHumanInput(get_entry5, get_entry1, get_entry2, get_entry3)
                CheckPatientInput(get_entry5, get_entry4, get_entry6)
                CheckPatientNationalNumberIsExists(get_entry5)
                show_confirm_massageBox = err_massage.askquestion(
                    "Confirm", "Are you sure?")
                if show_confirm_massageBox == 'yes':
                    InsertPatient(get_entry5, get_entry1, get_entry2,
                                  get_entry6, get_entry3, get_entry4)
                    err_massage.showinfo(
                        'Confirm', 'Save Information Successful')
                    controller.frames['patient_page'].update_show_listBox()
                    self.delete_entries()
                    return 'patient_page'
                else:
                    return 'add_patient'
            except Exception as ErrorMessage:
                err_massage.showerror('Error', ErrorMessage)
                return 'add_patient'
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


class delete_and_update_patient(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Delete And Update'
        self.backGround_image_and_texts('images/7.gif')

        self.Entry_1 = self.Entries(20, 130, 345)
        self.Entry_2 = self.Entries(20, 130, 395)
        self.Entry_3 = self.Entries(20, 130, 445)
        self.Entry_4 = patient_drop_down(self).VisitorDoctorNationalNumber_cb
        self.Entry_5 = self.Entries(20, 410, 395)

        self.sickness_text = self.scrollbar_for_text()

        self.b1 = self.Buttons('Back', lambda: controller.show_frames(
            self.back_to_patient_page()), 20, 20, 500)
        self.Buttons('Update', lambda: controller.show_frames(
            self.update_get_entries(controller)), 10, 800, 500)
        self.Buttons('Delete', lambda: controller.show_frames(
            self.delete_patient(controller)), 10, 700, 500)

        show_help_button = Button(self,text='Help',command=lambda: self.show_help(
            parent, controller),width=3,height=0)
        show_help_button.place(x=10,y=10)

    def show_help(self, parent, controller):
        A = pages_help(parent, controller, UpdateAndDeletePatientsHelp,
                       'images/7.gif', 'delete_and_update_patient', 90, 30, 130, 85, 10, 518, 10)
        A.grid(row=0, column=0, sticky="nsew")
        A.tkraise()

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

    def update_get_entries(self, controller):
        get_entry1 = self.Entry_1.get()
        get_entry2 = self.Entry_2.get()
        get_entry3 = self.Entry_3.get()
        get_entry4 = self.show_doctor_name_error()
        if get_entry4 is not False:
            get_entry5 = self.Entry_5.get()
            get_entry6 = self.sickness_text.get("1.0", END)

            try:
                CheckHumanInput(get_entry5, get_entry1, get_entry2, get_entry3)
                CheckPatientInput(get_entry5, get_entry4, get_entry6)
                if fu.patient_list[selected_indices[0]].NationalNumber != get_entry5:
                    CheckPatientNationalNumberIsExists(get_entry5)
                show_confirm_massageBox = err_massage.askquestion(
                    "Confirm", "Are you sure?")
                if show_confirm_massageBox == 'yes':
                    fu.patient_list[selected_indices[0]].Update(
                        get_entry5, get_entry1, get_entry2, get_entry6, get_entry3, get_entry4)
                    err_massage.showinfo(
                        'Confirm', 'Update Information Successful')
                    controller.frames['patient_page'].update_show_listBox()
                    self.delete_entries()
                    return 'patient_page'
                else:
                    return 'delete_and_update_patient'
            except Exception as ErrorMessage:
                err_massage.showerror('Error', ErrorMessage)
                return 'delete_and_update_patient'
        else:
            return 'delete_and_update_patient'

    def delete_patient(self, controller):
        show_confirm_massageBox = err_massage.askquestion(
            "Confirm", "Are you sure?")
        if show_confirm_massageBox == 'yes':
            err_massage.showinfo(
                'Confirm', 'Delete Patient Successful')
            fu.patient_list[selected_indices[0]].Delete
            del fu.patient_list[selected_indices[0]]
            controller.frames['patient_page'].update_show_listBox()
            return 'patient_page'
        else:
            return 'delete_and_update_patient'

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
            err_massage.showinfo('Confirm', 'Update Information Successful')
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
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.position()

        self.labels('Search by Firstname :', 5, 15)
        self.labels('Search by Lastname :', 5, 60)

        self.entry1 = self.entries(25, 132, 15)
        self.entry2 = self.entries(25, 132, 60)

        self.button1 = self.buttons(
            'Done', 8, lambda: self.get_entries(controller), 230, 120)
        self.button2 = self.buttons(
            'Cancel', 8, lambda: self.destroy(), 160, 120)

    def position(self):
        w = 300
        h = 150
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/8)
        y = (hs/50*28) - (h/2)
        self.title('Search Patient')
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(width=False, height=False)

    def labels(self, label_text, X, Y):
        label = Label(self, text=label_text, font=("Helvetica", 8, 'bold'))
        label.place(x=X, y=Y)

    def entries(self, Width, X, Y):
        entry = Entry(self, width=Width)
        entry.place(x=X, y=Y)
        return entry

    def buttons(self, button_text, Width, Command, X, Y):
        button = Button(self, text=button_text, width=Width, command=Command)
        button.place(x=X, y=Y)

    def get_entries(self, controller):
        get_Entry1 = self.entry1.get()
        get_Entry2 = self.entry2.get()
        search_list = FindPatient(FirstName=get_Entry1, LastName=get_Entry2)
        if len(search_list) == 0:
            self.destroy()
            err_massage.showerror('Error', 'Not Found Any Patient !!!')
            controller.frames['patient_page'].update_show_listBox()

        else:
            if get_Entry1 == '' and get_Entry2 == '':
                err_massage.showerror(
                    'Error', 'There is not any Entry for Search !!!\n\n Try Again ... ')
            else:
                self.destroy()
                err_massage.showinfo('Confirm', 'Search Patient Successful')
                controller.frames['patient_page'].show_listBox_for_search(
                    search_list)


class patient_drop_down:
    def __init__(self, parent):

        selected_VisitorDoctorNationalNumber = StringVar()

        self.VisitorDoctorNationalNumber_cb = ttk.Combobox(
            parent, textvariable=selected_VisitorDoctorNationalNumber, width=20, height=5)
        self.VisitorDoctorNationalNumber_cb['values'] = fu.update_doctors_to_dropDown(
        )
        self.VisitorDoctorNationalNumber_cb['state'] = 'readonly'
        self.VisitorDoctorNationalNumber_cb.place(x=408, y=340)
        self.VisitorDoctorNationalNumber_cb.bind(
            '<<ComboboxSelected>>', self.VisitorDoctorNationalNumber_changed)

    def VisitorDoctorNationalNumber_changed(self, event):
        msg = f'You selected {self.VisitorDoctorNationalNumber_cb.get()}!'
        showinfo(title='Result', message=msg)

