from tkinter import *
from functions import *
from DesignFunctions import *
import tkinter.messagebox as err_massage
from tkinter import ttk
from tkinter.messagebox import showinfo
import functions as fu


class drug_page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Drug Page'
        backGround_image_and_text(self, 'images/9.gif', 'Drug Page')

        self.listBox = self.scrollbar_for_listbox_right()
        self.listBox.bind('<Double-1>',
                          lambda x: self.item_selected(even=None, controller=controller))
        self.update_show_listBox()

        self.Buttons('Hospital Page', lambda: controller.show_frames(
            'hospital_page'), 15, 20, 480)
        self.Buttons('Add Drug', lambda: controller.show_frames(
            'add_drug'), 12, 140, 480)
        self.Buttons('Search Drug',
                     lambda: self.open_search_window(controller), 18, 237, 480)
        self.Buttons('Show all Drugs',
                     lambda: self.update_show_listBox(), 49, 20, 510)

    def update_show_listBox(self):
        fu.drug_list = LoadMedicines()
        self.listBox.delete(0, END)
        if len(fu.drug_list) == 0:
            self.listBox.insert(
                END, '             \
                                List is Empty !!!')
        else:
            i = 1
            for item in fu.drug_list:
                self.listBox.insert(END, f' {i} . {item}')
                i += 1

    def show_listBox_for_search(self, searchList):
        fu.drug_list = searchList
        self.listBox.delete(0, END)
        i = 1
        for item in fu.drug_list:
            self.listBox.insert(END, f' {i} . {item}')
            i += 1

    def Buttons(self, button_text, Command, Width, X, Y):
        Button(self, text=button_text, command=Command,
               width=Width).place(x=X, y=Y)

    def scrollbar_for_listbox_right(self):
        drug_list_var = StringVar(value=fu.drug_list)

        scrollbar = Scrollbar(self)
        listBox = Listbox(self, width=58, height=24,
                          yscrollcommand=scrollbar.set,
                          listvariable=drug_list_var,
                          selectmode='single', activestyle='none')
        scrollbar.config(command=listBox.yview)
        scrollbar.place(x=375, y=80, height=388)
        listBox.place(x=20, y=80)
        return listBox

    def open_search_window(self, controller):
        if len(fu.drug_list) == 0:
            err_massage.showerror(
                'Error', 'There is not any Drug in List !!!')
        else:
            mainWindow = search_drug(self, controller)
            mainWindow.grab_set()

    def item_selected(self, controller, even):
        print('fu.drug_list = ', fu.drug_list)
        global selected_indices
        selected_indices = self.listBox.curselection()
        print('selected_indices = ', selected_indices)
    #     # index = list(filter(lambda x: x.NationalNumber ==
    #     #                     fu.patient_list[selected_indices[0]].VisitordrugNationalNumber, Loaddrugs()))[0]
    #     # print('index ==== ', index)
    #     # selected_langs = ",".join([self.listBox.get(i)
    #     #                           for i in selected_indices])
    #     # msg = f'You selected: {selected_langs}'
    #     # print(type(fu.drug_list[selected_indices[0]]))
    #     # print(selected_indices[0])
    #     # print(fu.drug_list[selected_indices[0]].FirstName)

    #     print('siiiiiiik = ', fu.drug_list[selected_indices[0]])

    # # def load_entries_for_delete_and_update_page(self, controller):

    #     controller.show_frames('delete_and_update_drug')

    #     self.delete_entries_of_selected_drug(controller)

    #     controller.frames['delete_and_update_drug'].Entry_1.insert(
    #         END, fu.drug_list[selected_indices[0]].FirstName)
    #     controller.frames['delete_and_update_drug'].Entry_2.insert(
    #         END, fu.drug_list[selected_indices[0]].LastName)
    #     controller.frames['delete_and_update_drug'].Entry_3.insert(
    #         END, fu.drug_list[selected_indices[0]].Age)
    #     controller.frames['delete_and_update_drug'].Entry_4.set(
    #         f'{fu.drug_list[selected_indices[0]].Type}'
    #     )
    #     controller.frames['delete_and_update_drug'].Entry_5.insert(
    #         END, fu.drug_list[selected_indices[0]].NationalNumber)
    #     # controller.frames['delete_and_update_drug'].sickness_text.insert(
    #     #     END, fu.drug_list[selected_indices[0]].Sickness)

    # def delete_entries_of_selected_drug(self, controller):
    #     controller.frames['delete_and_update_drug'].Entry_1.delete(0, END)
    #     controller.frames['delete_and_update_drug'].Entry_2.delete(0, END)
    #     controller.frames['delete_and_update_drug'].Entry_3.delete(0, END)
    #     controller.frames['delete_and_update_drug'].Entry_5.delete(0, END)
    #     # controller.frames['delete_and_update_drug'].sickness_text.delete(
    #     #     '1.0', END)


class add_drug(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Add Drug'
        self.backGround_image_and_texts('images/13.gif')

        self.Entry_1 = self.Entries(20, 130, 200)
        self.Entry_2 = self.Entries(20, 130, 250)

        self.description_text = self.scrollbar_for_text()
        # self.Entry_3 = self.Entries(20, 410, 200)
        # self.Entry_4 = drug_drop_down(self).drugDegree_cb
        # self.Entry_5 = self.Entries(20, 410, 250)

        self.b1 = self.Buttons('Back to Drug Page', lambda: controller.show_frames(
            self.back_to_drug_page()), 20, 20, 500)
        self.Buttons('Save', lambda: controller.show_frames(
            self.get_entries(controller)), 18, 750, 500)

    def backGround_image_and_texts(self, photo):
        self.backgrandImage = PhotoImage(file=photo)
        canvas = Canvas(self)
        canvas.pack(side='top', fill='both', expand=True)
        canvas.create_image(0, 0, image=self.backgrandImage, anchor="nw")

        self.labels(canvas, 'Drug Information', 450, 50, 24)
        self.labels(canvas, 'Drag Name :', 80, 205, 11)
        self.labels(canvas, 'Stock :', 62, 255, 11)
        self.labels(canvas, 'Description :', 315, 205, 11)
        # self.labels(canvas, "Degree :", 315, 205, 11)
        # self.labels(canvas, 'National Number :', 345, 255, 11)

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
        get_entry3 = self.description_text.get("1.0", END)
        try:
            CheckMedicineInput(get_entry1, get_entry2, get_entry3)
            show_confirm_massageBox = err_massage.askquestion(
                "Confirm", "Are you sure?")
            if show_confirm_massageBox == 'yes':
                InsertMedicine(get_entry1, get_entry2, get_entry3)
                err_massage.showinfo(
                    'Confirm', 'Save Information Successful')
                controller.frames['drug_page'].update_show_listBox()
                self.delete_entries()
                return 'drug_page'
            else:
                print('No')
                return 'add_drug'
        except Exception as ErrorMessage:
            err_massage.showerror('Error', ErrorMessage)
            return 'add_drug'

    def delete_entries(self):
        self.Entry_1.delete(0, END)
        self.Entry_2.delete(0, END)
        self.description_text.delete("1.0", END)
        # self.Entry_3.delete(0, END)
        # self.Entry_4.set('')
        # self.Entry_5.delete(0, END)

    def Buttons(self, button_text, Command, Width, X, Y):
        Button(self, text=button_text, command=Command,
               width=Width).place(x=X, y=Y)

    def back_to_drug_page(self):
        self.delete_entries()
        return 'drug_page'

    def scrollbar_for_text(self):
        scrollbar = Scrollbar(self)
        text = Text(self, height=4, width=40, yscrollcommand=scrollbar.set)
        scrollbar.config(command=text.yview)
        scrollbar.place(x=695, y=198, height=68)
        text.place(x=365, y=198)
        return text


class delete_and_update_drug(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Delete And Update'
        self.backGround_image_and_texts('images/13.gif')

        self.Entry_1 = self.Entries(20, 130, 345)
        self.Entry_2 = self.Entries(20, 130, 395)
        self.Entry_3 = self.Entries(20, 130, 445)
        self.Entry_4 = drug_drop_down(self).drugDegree_cb
        self.Entry_5 = self.Entries(20, 410, 395)

        self.b1 = self.Buttons('Back to Drug Page', lambda: controller.show_frames(
            self.back_to_drug_page(controller)), 20, 20, 500)
        self.Buttons('Update', lambda: controller.show_frames(
            self.update_get_entries(controller)), 10, 800, 500)
        self.Buttons('Delete', lambda: controller.show_frames(
            self.delete_drug(controller)), 10, 700, 500)

    def backGround_image_and_texts(self, photo):
        self.backgrandImage = PhotoImage(file=photo)
        canvas = Canvas(self)
        canvas.pack(side='top', fill='both', expand=True)
        canvas.create_image(0, 0, image=self.backgrandImage, anchor="nw")

        self.labels(canvas, 'Drug Information', 450, 50, 24)
        self.labels(canvas, 'First Name :', 80, 350, 11)
        self.labels(canvas, 'Last Name :', 80, 400, 11)
        self.labels(canvas, 'Age :', 55, 450, 11)
        self.labels(canvas, "Degree :", 315, 350, 11)
        self.labels(canvas, 'National Number :', 345, 400, 11)

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
        get_entry4 = self.show_drug_name_error()
        if get_entry4 is not False:
            get_entry5 = self.Entry_5.get()

            try:
                CheckHumanInput(get_entry5, get_entry1, get_entry2, get_entry3)
                CheckMedicineInput(get_entry5, get_entry4)
                show_confirm_massageBox = err_massage.askquestion(
                    "Confirm", "Are you sure?")
                if show_confirm_massageBox == 'yes':
                    fu.drug_list[selected_indices[0]].Update(
                        get_entry5, get_entry1, get_entry2, get_entry3, get_entry4)
                    err_massage.showinfo(
                        'Confirm', 'Update Information Successful')
                    controller.frames['add_patient'].Entry_4['values'] = fu.update_drugs_to_dropDown(
                    )
                    controller.frames['delete_and_update_patient'].Entry_4['values'] = fu.update_drugs_to_dropDown(
                    )
                    controller.frames['drug_page'].update_show_listBox()
                    self.delete_entries()
                    return 'drug_page'
                else:
                    print('No')
                    return 'delete_and_update_drug'
            except Exception as ErrorMessage:
                err_massage.showerror('Error', ErrorMessage)
                return 'delete_and_update_drug'
        else:
            return 'delete_and_update_drug'

    def delete_drug(self, controller):
        # print('hello')
        # print(self.Entry_1.get())
        # print(type(selected_indices[0]))
        # print(fu.drug_list[selected_indices[0]])
        # Deletedrug(national)
        show_confirm_massageBox = err_massage.askquestion(
            "Confirm", "Are you sure?")
        if show_confirm_massageBox == 'yes':
            err_massage.showinfo(
                'Confirm', 'Delete Drug Successful')
            fu.drug_list[selected_indices[0]].Delete
            del fu.drug_list[selected_indices[0]]
            controller.frames['drug_page'].update_show_listBox()
            controller.frames['add_patient'].Entry_4['values'] = fu.update_drugs_to_dropDown(
            )
            controller.frames['delete_and_update_patient'].Entry_4['values'] = fu.update_drugs_to_dropDown(
            )
            return 'drug_page'
        else:
            return 'delete_and_update_drug'

    def delete_entries(self):
        self.Entry_1.delete(0, END)
        self.Entry_2.delete(0, END)
        self.Entry_3.delete(0, END)
        self.Entry_4.set('')
        self.Entry_5.delete(0, END)

    def Buttons(self, button_text, Command, Width, X, Y):
        Button(self, text=button_text, command=Command,
               width=Width).place(x=X, y=Y)

    def back_to_drug_page(self, controller):
        self.delete_entries()
        return 'drug_page'

    def show_drug_name_error(self):
        try:
            get_entry4 = self.Entry_4.get()
            return get_entry4
        except:
            err_massage.showerror("Drug's Name Error",
                                  'Please Select a Drug ')
            return False


class search_drug(Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.position()

        self.labels('Search by Drugname :', 5, 40)

        self.entry1 = self.entries(25, 132, 40)

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
        self.title('Search')
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
        print('get_Entry1 = ', get_Entry1)
        search_list = FindMedicine(Name=get_Entry1)
        print('size = ', search_list)
        if len(search_list) == 0:
            self.destroy()
            err_massage.showerror('Error', 'Not Found Any Drug !!!')
            controller.frames['drug_page'].update_show_listBox()

        else:
            if get_Entry1 == '':
                err_massage.showerror(
                    'Error', 'There is not any Entry for Search !!!\n\n Try Again ... ')
            else:
                self.destroy()
                err_massage.showinfo('Confirm', 'Search Drug Successful')
                controller.frames['drug_page'].show_listBox_for_search(
                    search_list)


class drug_drop_down:
    def __init__(self, parent):

        selected_drugDegree = StringVar()

        self.drugDegree_cb = ttk.Combobox(
            parent, textvariable=selected_drugDegree, width=20, height=5)
        self.drugDegree_cb['values'] = TypeList
        self.drugDegree_cb['state'] = 'readonly'
        self.drugDegree_cb.place(x=408, y=195)
        self.drugDegree_cb.bind(
            '<<ComboboxSelected>>', self.drugDegree_changed)

    def drugDegree_changed(self, event):
        msg = f'You selected {self.drugDegree_cb.get()}!'
        showinfo(title='Result', message=msg)
