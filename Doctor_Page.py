from tkinter import *
from functions import *
from DesignFunctions import *
import tkinter.messagebox as err_massage
from tkinter import ttk
from tkinter.messagebox import showinfo
import functions as fu


class doctor_page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Doctor Page'
        backGround_image_and_text(self,'images/1.gif','Doctor Page')

        self.listBox = self.scrollbar_for_listbox_right()
        self.listBox.bind('<Double-1>',
                          lambda x: self.item_selected(even=None, controller=controller))
        self.update_show_listBox()

        self.Buttons('Hospital Page', lambda: controller.show_frames(
            'hospital_page'), 15, 20, 480)
        self.Buttons('Add Doctor', lambda: controller.show_frames(
            'add_doctor'), 12, 140, 480)
        self.Buttons('Search Doctor',
                     lambda: self.open_search_window(controller), 18, 237, 480)
        self.Buttons('Show all Doctors',
                     lambda: self.update_show_listBox(), 49, 20, 510)

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
        mainWindow = search_doctor(self, controller)
        mainWindow.grab_set()

    def item_selected(self, controller, even):
        print('fu.doctor_list = ', fu.doctor_list)
        global selected_indices
        selected_indices = self.listBox.curselection()
        print('selected_indices = ', selected_indices)
        index = list(filter(lambda x: x.NationalNumber ==
                            fu.doctor_list[selected_indices[0]].VisitorDoctorNationalNumber, LoadDoctors()))[0]
        print('index = ', index)
        # selected_langs = ",".join([self.listBox.get(i)
        #                           for i in selected_indices])
        # msg = f'You selected: {selected_langs}'
        # print(type(fu.doctor_list[selected_indices[0]]))
        # print(selected_indices[0])
        # print(fu.doctor_list[selected_indices[0]].FirstName)

    # def load_entries_for_delete_and_update_page(self, controller):

        controller.show_frames('delete_and_update_doctor')

        self.delete_entries_of_selected_doctor(controller)

        controller.frames['delete_and_update_doctor'].Entry_1.insert(
            END, fu.doctor_list[selected_indices[0]].FirstName)
        controller.frames['delete_and_update_doctor'].Entry_2.insert(
            END, fu.doctor_list[selected_indices[0]].LastName)
        controller.frames['delete_and_update_doctor'].Entry_3.insert(
            END, fu.doctor_list[selected_indices[0]].Age)
        controller.frames['delete_and_update_doctor'].Entry_4.set(
            # fu.doctor_list[selected_indices[0]].VisitorDoctorNationalNumber
            f'{index.id}. Dr.{index.FirstName} {index.LastName}'
        )
        controller.frames['delete_and_update_doctor'].Entry_5.insert(
            END, fu.doctor_list[selected_indices[0]].NationalNumber)
        controller.frames['delete_and_update_doctor'].sickness_text.insert(
            END, fu.doctor_list[selected_indices[0]].Sickness)

    def delete_entries_of_selected_doctor(self, controller):
        controller.frames['delete_and_update_doctor'].Entry_1.delete(0, END)
        controller.frames['delete_and_update_doctor'].Entry_2.delete(0, END)
        controller.frames['delete_and_update_doctor'].Entry_3.delete(0, END)
        controller.frames['delete_and_update_doctor'].Entry_5.delete(0, END)
        controller.frames['delete_and_update_doctor'].sickness_text.delete(
            '1.0', END)




class add_doctor(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Add Doctor'
        self.backGround_image_and_texts('images/7.gif')

        self.Entry_1 = self.Entries(20, 130, 345)
        self.Entry_2 = self.Entries(20, 130, 395)
        self.Entry_3 = self.Entries(20, 130, 445)
        self.Entry_4 = drop_down(self).VisitorDoctorNationalNumber_cb
        self.Entry_5 = self.Entries(20, 410, 395)

        self.sickness_text = self.scrollbar_for_text()

        self.b1 = self.Buttons('Back to Doctor Page', lambda: controller.show_frames(
            self.back_to_doctor_page()), 20, 20, 500)
        self.Buttons('Save', lambda: controller.show_frames(
            self.get_entries(controller)), 18, 750, 500)

    def backGround_image_and_texts(self, photo):
        self.backgrandImage = PhotoImage(file=photo)
        canvas = Canvas(self)
        canvas.pack(side='top', fill='both', expand=True)
        canvas.create_image(0, 0, image=self.backgrandImage, anchor="nw")

        self.labels(canvas, 'doctor Information', 450, 50, 24)
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

            try:
                CheckHumanInput(get_entry5, get_entry1, get_entry2, get_entry3)
                CheckdoctorInput(get_entry5, get_entry4, get_entry6)
                show_confirm_massageBox = err_massage.askquestion(
                    "Confirm", "Are you sure?")
                if show_confirm_massageBox == 'yes':
                    Insertdoctor(get_entry5, get_entry1, get_entry2,
                                  get_entry6, get_entry3, get_entry4)
                    err_massage.showinfo(
                        'Confirm', 'Save Information Successful')
                    controller.frames['doctor_page'].update_show_listBox()
                    self.delete_entries()
                    return 'doctor_page'
                else:
                    print('No')
                    return 'add_doctor'
            except Exception as ErrorMessage:
                err_massage.showerror('Error', ErrorMessage)
                return 'add_doctor'
        else:
            return 'add_doctor'

        #     massege_error = Receptiondoctor(FirstName=get_entry1, LastName=get_entry2, Age=get_entry3,
        #                                      VisitorDoctorNationalNumber=get_entry4, NationalNumber=get_entry5,
        #                                      Sickness=get_entry6)

        #     confirm_for_save = self.show_errors(massege_error)
        # if confirm_for_save is True:
        #     controller.frames['doctor_page'].update_show_listBox()
        #     self.delete_entries()
        #     return 'doctor_page'
        # else:
        #     return 'add_doctor'




