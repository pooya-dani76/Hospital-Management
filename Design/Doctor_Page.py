import sys
sys.path.append('../Backend')
from tkinter import *
from functions import *
from DesignFunctions import *
import tkinter.messagebox as err_massage
from tkinter import ttk
from tkinter.messagebox import showinfo
import functions as fu
from Pages_Help import *


class doctor_page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Doctor Page'
        backGround_image_and_text(self, 'images/1.gif', 'Doctor Page')

        self.listBox = self.scrollbar_for_listbox_right()
        self.listBox.bind('<Double-1>',
                          lambda x: self.item_selected(even=None, controller=controller))
        self.update_show_listBox()

        self.Buttons('Back', lambda: controller.show_frames(
            'hospital_page'), 15, 20, 480)
        self.Buttons('Add Doctor', lambda: controller.show_frames(
            'add_doctor'), 12, 140, 480)
        self.Buttons('Search Doctor',
                     lambda: self.open_search_window(controller), 18, 237, 480)
        self.Buttons('Show all Doctors',
                     lambda: self.update_show_listBox(), 49, 20, 510)
        show_help_button = Button(self, text='Help', command=lambda: self.show_help(
            parent, controller), width=3, height=0)
        show_help_button.place(x=10, y=10)

    def show_help(self, parent, controller):
        A = pages_help(parent, controller, DoctorPageHelp,
                       'images/1.gif', 'doctor_page', 90, 15, 130, 310, 10, 518, 10)
        A.grid(row=0, column=0, sticky="nsew")
        A.tkraise()

    def update_show_listBox(self):
        fu.doctor_list = LoadDoctors()
        self.listBox.delete(0, END)
        if len(fu.doctor_list) == 0:
            self.listBox.insert(
                END, '             \
                                List is Empty !!!')
        else:
            i = 1
            for item in fu.doctor_list:
                self.listBox.insert(END, f' {i} . {item}')
                i += 1

    def show_listBox_for_search(self, searchList):
        fu.doctor_list = searchList
        self.listBox.delete(0, END)
        i = 1
        for item in fu.doctor_list:
            self.listBox.insert(END, f' {i} . {item}')
            i += 1

    def Buttons(self, button_text, Command, Width, X, Y):
        Button(self, text=button_text, command=Command,
               width=Width).place(x=X, y=Y)

    def scrollbar_for_listbox_right(self):
        doctor_list_var = StringVar(value=fu.doctor_list)

        scrollbar = Scrollbar(self)
        listBox = Listbox(self, width=58, height=24,
                          yscrollcommand=scrollbar.set,
                          listvariable=doctor_list_var,
                          selectmode='single', activestyle='none')
        scrollbar.config(command=listBox.yview)
        scrollbar.place(x=375, y=80, height=388)
        listBox.place(x=20, y=80)
        return listBox

    def open_search_window(self, controller):
        if len(fu.doctor_list) == 0:
            err_massage.showerror(
                'Error', 'There is not any Doctor in List !!!')
        else:
            mainWindow = search_doctor(self, controller)
            mainWindow.grab_set()

    def item_selected(self, controller, even):
        global selected_indices
        selected_indices = self.listBox.curselection()
        controller.show_frames('delete_and_update_doctor')

        self.delete_entries_of_selected_doctor(controller)

        controller.frames['delete_and_update_doctor'].Entry_1.insert(
            END, fu.doctor_list[selected_indices[0]].FirstName)
        controller.frames['delete_and_update_doctor'].Entry_2.insert(
            END, fu.doctor_list[selected_indices[0]].LastName)
        controller.frames['delete_and_update_doctor'].Entry_3.insert(
            END, fu.doctor_list[selected_indices[0]].Age)
        controller.frames['delete_and_update_doctor'].Entry_4.set(
            f'{fu.doctor_list[selected_indices[0]].Type}'
        )
        controller.frames['delete_and_update_doctor'].Entry_5.insert(
            END, fu.doctor_list[selected_indices[0]].NationalNumber)

    def delete_entries_of_selected_doctor(self, controller):
        controller.frames['delete_and_update_doctor'].Entry_1.delete(0, END)
        controller.frames['delete_and_update_doctor'].Entry_2.delete(0, END)
        controller.frames['delete_and_update_doctor'].Entry_3.delete(0, END)
        controller.frames['delete_and_update_doctor'].Entry_5.delete(0, END)


class add_doctor(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Add Doctor'
        self.backGround_image_and_texts('images/15.gif')

        self.Entry_1 = self.Entries(20, 680, 150)
        self.Entry_2 = self.Entries(20, 680, 200)
        self.Entry_3 = self.Entries(20, 680, 250)
        self.Entry_4 = doctor_drop_down(self).DoctorDegree_cb
        self.Entry_5 = self.Entries(20, 680, 300)

        self.b1 = self.Buttons('Back', lambda: controller.show_frames(
            self.back_to_doctor_page()), 20, 20, 500)
        self.Buttons('Save', lambda: controller.show_frames(
            self.get_entries(controller)), 18, 750, 500)
        show_help_button = Button(self, text='Help', command=lambda: self.show_help(
            parent, controller), width=3, height=0)
        show_help_button.place(x=10, y=10)

    def show_help(self, parent, controller):
        A = pages_help(parent, controller, AddDoctorsHelp,
                       'images/15.gif', 'add_doctor', 90, 22, 130, 205, 10, 518, 10)
        A.grid(row=0, column=0, sticky="nsew")
        A.tkraise()

    def backGround_image_and_texts(self, photo):
        self.backgrandImage = PhotoImage(file=photo)
        canvas = Canvas(self)
        canvas.pack(side='top', fill='both', expand=True)
        canvas.create_image(0, 0, image=self.backgrandImage, anchor="nw")

        self.labels(canvas, 'Doctor Information', 450, 50, 24)
        self.labels(canvas, 'First Name :', 585, 160, 11)
        self.labels(canvas, 'Last Name :', 585, 210, 11)
        self.labels(canvas, 'Age :', 565, 260, 11)
        self.labels(canvas, "Type :", 567, 360, 11)
        self.labels(canvas, 'National Number :', 605, 310, 11)

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
        get_entry4 = self.show_degree_error()
        if get_entry4 is not False:
            get_entry5 = self.Entry_5.get()

            try:
                CheckHumanInput(get_entry5, get_entry1, get_entry2, get_entry3)
                CheckDoctorInput(get_entry4)
                CheckDoctorNationalNumberIsExists(get_entry5)
                show_confirm_massageBox = err_massage.askquestion(
                    "Confirm", "Are you sure?")
                if show_confirm_massageBox == 'yes':
                    InsertDoctor(get_entry5, get_entry1,
                                 get_entry2, get_entry3, get_entry4)
                    err_massage.showinfo(
                        'Confirm', 'Save Information Successful')
                    controller.frames['add_patient'].Entry_4['values'] = fu.update_doctors_to_dropDown(
                    )
                    controller.frames['delete_and_update_patient'].Entry_4['values'] = fu.update_doctors_to_dropDown(
                    )
                    controller.frames['doctor_page'].update_show_listBox()
                    self.delete_entries()
                    return 'doctor_page'
                else:
                    return 'add_doctor'
            except Exception as ErrorMessage:
                err_massage.showerror('Error', ErrorMessage)
                return 'add_doctor'
        else:
            return 'add_doctor'

    def delete_entries(self):
        self.Entry_1.delete(0, END)
        self.Entry_2.delete(0, END)
        self.Entry_3.delete(0, END)
        self.Entry_4.set('')
        self.Entry_5.delete(0, END)

    def Buttons(self, button_text, Command, Width, X, Y):
        Button(self, text=button_text, command=Command,
               width=Width).place(x=X, y=Y)

    def back_to_doctor_page(self):
        self.delete_entries()
        return 'doctor_page'

    def show_degree_error(self):
        try:
            get_entry4 = self.Entry_4.get()
            return get_entry4
        except:
            err_massage.showerror("Doctor's Name Error",
                                  'Please Select a Doctor ')
            return False


class delete_and_update_doctor(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Delete And Update'
        self.backGround_image_and_texts('images/15.gif')

        self.Entry_1 = self.Entries(20, 680, 150)
        self.Entry_2 = self.Entries(20, 680, 200)
        self.Entry_3 = self.Entries(20, 680, 250)
        self.Entry_4 = doctor_drop_down(self).DoctorDegree_cb
        self.Entry_5 = self.Entries(20, 680, 300)

        self.b1 = self.Buttons('Back', lambda: controller.show_frames(
            self.back_to_doctor_page(controller)), 20, 20, 500)
        self.Buttons('Update', lambda: controller.show_frames(
            self.update_get_entries(controller)), 10, 800, 500)
        self.Buttons('Delete', lambda: controller.show_frames(
            self.delete_doctor(controller)), 10, 700, 500)
        show_help_button = Button(self, text='Help', command=lambda: self.show_help(
            parent, controller), width=3, height=0)
        show_help_button.place(x=10, y=10)

    def show_help(self, parent, controller):
        A = pages_help(parent, controller, UpdateAndDeleteDoctorsHelp,
                       'images/15.gif', 'delete_and_update_doctor', 90, 30, 130, 85, 10, 518, 10)
        A.grid(row=0, column=0, sticky="nsew")
        A.tkraise()

    def backGround_image_and_texts(self, photo):
        self.backgrandImage = PhotoImage(file=photo)
        canvas = Canvas(self)
        canvas.pack(side='top', fill='both', expand=True)
        canvas.create_image(0, 0, image=self.backgrandImage, anchor="nw")

        self.labels(canvas, 'Doctor Information', 450, 50, 24)
        self.labels(canvas, 'First Name :', 585, 160, 11)
        self.labels(canvas, 'Last Name :', 585, 210, 11)
        self.labels(canvas, 'Age :', 565, 260, 11)
        self.labels(canvas, "Type :", 567, 360, 11)
        self.labels(canvas, 'National Number :', 605, 310, 11)

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
        get_entry4 = self.show_degree_error()
        if get_entry4 is not False:
            get_entry5 = self.Entry_5.get()

            try:
                CheckHumanInput(get_entry5, get_entry1, get_entry2, get_entry3)
                CheckDoctorInput(get_entry4)
                if fu.doctor_list[selected_indices[0]].NationalNumber != get_entry5:
                    CheckDoctorNationalNumberIsExists(get_entry5)
                show_confirm_massageBox = err_massage.askquestion(
                    "Confirm", "Are you sure?")
                if show_confirm_massageBox == 'yes':
                    fu.doctor_list[selected_indices[0]].Update(
                        get_entry5, get_entry1, get_entry2, get_entry3, get_entry4)
                    err_massage.showinfo(
                        'Confirm', 'Update Information Successful')
                    controller.frames['add_patient'].Entry_4['values'] = fu.update_doctors_to_dropDown(
                    )
                    controller.frames['delete_and_update_patient'].Entry_4['values'] = fu.update_doctors_to_dropDown(
                    )
                    controller.frames['doctor_page'].update_show_listBox()
                    controller.frames['patient_page'].update_show_listBox()
                    self.delete_entries()
                    return 'doctor_page'
                else:
                    return 'delete_and_update_doctor'
            except Exception as ErrorMessage:
                err_massage.showerror('Error', ErrorMessage)
                return 'delete_and_update_doctor'
        else:
            return 'delete_and_update_doctor'

    def delete_doctor(self, controller):
        number_of_patient = len(SearchPatient(
            VisitorDoctorNationalNumber=fu.doctor_list[selected_indices[0]].NationalNumber))
        if number_of_patient == 0:
            show_confirm_massageBox = err_massage.askquestion(
                "Confirm", "are you sure?")
            if show_confirm_massageBox == 'yes':
                err_massage.showinfo(
                    'Confirm', 'Delete Doctor Successful')
                fu.doctor_list[selected_indices[0]].Delete
                del fu.doctor_list[selected_indices[0]]
                controller.frames['doctor_page'].update_show_listBox()
                controller.frames['patient_page'].update_show_listBox()
                controller.frames['add_patient'].Entry_4['values'] = fu.update_doctors_to_dropDown(
                )
                controller.frames['delete_and_update_patient'].Entry_4['values'] = fu.update_doctors_to_dropDown(
                )
                return 'doctor_page'
            else:
                return 'delete_and_update_doctor'
        else:
            show_confirm_massageBox = err_massage.askquestion(
                "Confirm", f"This Doctor is Visitor of {number_of_patient} Patient(s).\
                \nThese Patient May be Deleted !!!\nAre you Sure to Continue?")
            if show_confirm_massageBox == 'yes':
                err_massage.showinfo(
                    'Confirm', 'Delete Doctor Successful')
                fu.doctor_list[selected_indices[0]].Delete
                del fu.doctor_list[selected_indices[0]]
                controller.frames['doctor_page'].update_show_listBox()
                controller.frames['patient_page'].update_show_listBox()
                controller.frames['add_patient'].Entry_4['values'] = fu.update_doctors_to_dropDown(
                )
                controller.frames['delete_and_update_patient'].Entry_4['values'] = fu.update_doctors_to_dropDown(
                )
                return 'doctor_page'
            else:
                return 'delete_and_update_doctor'

    def delete_entries(self):
        self.Entry_1.delete(0, END)
        self.Entry_2.delete(0, END)
        self.Entry_3.delete(0, END)
        self.Entry_4.set('')
        self.Entry_5.delete(0, END)

    def Buttons(self, button_text, Command, Width, X, Y):
        Button(self, text=button_text, command=Command,
               width=Width).place(x=X, y=Y)

    def back_to_doctor_page(self, controller):
        self.delete_entries()
        return 'doctor_page'

    def show_degree_error(self):
        try:
            get_entry4 = self.Entry_4.get()
            return get_entry4
        except:
            err_massage.showerror("Doctor's Name Error",
                                  'Please Select a Doctor ')
            return False


class search_doctor(Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.position()

        self.labels('Search by Firstname :', 5, 15)
        self.labels('Search by Lastname :', 5, 50)
        self.labels('Search by Type :', 5, 85)

        self.entry1 = self.entries(25, 132, 15)
        self.entry2 = self.entries(25, 132, 50)
        self.entry3 = doctor_drop_down(self).DoctorDegree_cb
        self.entry3.place(x=132, y=85)

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
        self.title('Search Doctor')
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
        get_Entry3 = self.entry3.get()
        search_list = FindDoctor(FirstName=get_Entry1,
                                 LastName=get_Entry2, Type=get_Entry3)
        if len(search_list) == 0:
            self.destroy()
            err_massage.showerror('Error', 'Not Found Any Doctor !!!')
            controller.frames['doctor_page'].update_show_listBox()

        else:
            if get_Entry1 == '' and get_Entry2 == '' and get_Entry3 == '':
                err_massage.showerror(
                    'Error', 'There is not any Entry for Search !!!\n\n Try Again ... ')
            else:
                self.destroy()
                err_massage.showinfo('Confirm', 'Search Doctor Successful')
                controller.frames['doctor_page'].show_listBox_for_search(
                    search_list)


class doctor_drop_down:
    def __init__(self, parent):

        selected_DoctorDegree = StringVar()

        self.DoctorDegree_cb = ttk.Combobox(
            parent, textvariable=selected_DoctorDegree, width=20, height=5)
        self.DoctorDegree_cb['values'] = TypeList
        self.DoctorDegree_cb['state'] = 'readonly'
        self.DoctorDegree_cb.place(x=680, y=350)
        self.DoctorDegree_cb.bind(
            '<<ComboboxSelected>>', self.DoctorDegree_changed)

    def DoctorDegree_changed(self, event):
        msg = f'You selected {self.DoctorDegree_cb.get()}!'
        showinfo(title='Result', message=msg)
