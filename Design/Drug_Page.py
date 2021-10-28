from tkinter import *
from functions import *
from DesignFunctions import *
import tkinter.messagebox as err_massage
import functions as fu
from Pages_Help import *


class drug_page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Drug Page'
        backGround_image_and_text(self, 'images/9.gif', 'Drug Page')

        self.listBox = self.scrollbar_for_listbox_right()
        self.listBox.bind('<Double-1>',
                          lambda x: self.item_selected(even=None, controller=controller))
        self.update_show_listBox()

        self.Buttons('Back', lambda: controller.show_frames(
            'hospital_page'), 15, 20, 480)
        self.Buttons('Add Drug', lambda: controller.show_frames(
            'add_drug'), 12, 140, 480)
        self.Buttons('Search Drug',
                     lambda: self.open_search_window(controller), 18, 237, 480)
        self.Buttons('Show all Drugs',
                     lambda: self.update_show_listBox(), 49, 20, 510)
        show_help_button = Button(self, text='Help', command=lambda: self.show_help(
            parent, controller), width=3, height=0)
        show_help_button.place(x=10, y=10)

    def show_help(self, parent, controller):
        A = pages_help(parent, controller, DrugPageHelp,
                       'images/9.gif', 'drug_page', 100, 17, 110, 280, 10, 518, 10)
        A.grid(row=0, column=0, sticky="nsew")
        A.tkraise()

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
        global selected_indices
        selected_indices = self.listBox.curselection()

        controller.show_frames('delete_and_update_drug')

        self.delete_entries_of_selected_drug(controller)

        controller.frames['delete_and_update_drug'].Entry_1.insert(
            END, fu.drug_list[selected_indices[0]].Name)
        controller.frames['delete_and_update_drug'].stock_textVariable.set(
            str(fu.drug_list[selected_indices[0]].Stock)
        )
        controller.frames['delete_and_update_drug'].description_text.insert(
            END, fu.drug_list[selected_indices[0]].Description)

    def delete_entries_of_selected_drug(self, controller):
        controller.frames['delete_and_update_drug'].Entry_1.delete(0, END)
        controller.frames['delete_and_update_drug'].description_text.delete(
            '1.0', END)


class add_drug(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Add Drug'
        self.backGround_image_and_texts('images/13.gif')

        self.Entry_1 = self.Entries(20, 130, 200)
        self.Entry_2 = self.Entries(20, 130, 250)

        self.description_text = self.scrollbar_for_text()

        self.b1 = self.Buttons('Back', lambda: controller.show_frames(
            self.back_to_drug_page()), 20, 20, 500)
        self.Buttons('Save', lambda: controller.show_frames(
            self.get_entries(controller)), 18, 750, 500)
        show_help_button = Button(self, text='Help', command=lambda: self.show_help(
            parent, controller), width=3, height=0)
        show_help_button.place(x=10, y=10)

    def show_help(self, parent, controller):
        A = pages_help(parent, controller, AddDrugsHelp,
                       'images/13.gif', 'add_drug', 90, 16, 130, 100, 10, 518, 10)
        A.grid(row=0, column=0, sticky="nsew")
        A.tkraise()

    def backGround_image_and_texts(self, photo):
        self.backgrandImage = PhotoImage(file=photo)
        canvas = Canvas(self)
        canvas.pack(side='top', fill='both', expand=True)
        canvas.create_image(0, 0, image=self.backgrandImage, anchor="nw")

        self.labels(canvas, 'Drug Information', 450, 50, 24)
        self.labels(canvas, 'Drag Name :', 80, 205, 11)
        self.labels(canvas, 'Stock :', 62, 255, 11)
        self.labels(canvas, 'Description :', 315, 205, 11)

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
                return 'add_drug'
        except Exception as ErrorMessage:
            err_massage.showerror('Error', ErrorMessage)
            return 'add_drug'

    def delete_entries(self):
        self.Entry_1.delete(0, END)
        self.Entry_2.delete(0, END)
        self.description_text.delete("1.0", END)

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

        self.Entry_1 = self.Entries(20, 130, 150)
        self.buy_and_sell_entry = self.Entries(20, 130, 250)

        self.description_text = self.scrollbar_for_text()

        self.stock_textVariable = StringVar()
        self.stock_label = Label(
            self, textvariable=self.stock_textVariable, width=15)
        self.stock_label.place(x=128, y=195)

        self.b1 = self.Buttons('Back', lambda: controller.show_frames(
            self.back_to_drug_page()), 20, 20, 500)
        self.Buttons('Update', lambda: controller.show_frames(
            self.update_get_entries(controller)), 10, 800, 500)
        self.Buttons('Delete', lambda: controller.show_frames(
            self.delete_drug(controller)), 10, 700, 500)
        self.Buttons('Sell', lambda: self.sell_stock(), 7, 130, 275)
        self.Buttons('Buy', lambda: self.buy_stock(), 7, 195, 275)
        show_help_button = Button(self, text='Help', command=lambda: self.show_help(
            parent, controller), width=3, height=0)
        show_help_button.place(x=10, y=10)

    def show_help(self, parent, controller):
        A = pages_help(parent, controller, UpdateAndDeleteDrugsHelp,
                       'images/13.gif', 'delete_and_update_drug', 90, 25, 130, 100, 10, 518, 10)
        A.grid(row=0, column=0, sticky="nsew")
        A.tkraise()

    def backGround_image_and_texts(self, photo):
        self.backgrandImage = PhotoImage(file=photo)
        canvas = Canvas(self)
        canvas.pack(side='top', fill='both', expand=True)
        canvas.create_image(0, 0, image=self.backgrandImage, anchor="nw")

        self.labels(canvas, 'Drug Information', 450, 50, 24)
        self.labels(canvas, 'Drag Name :', 80, 155, 11)
        self.labels(canvas, 'Stock :', 62, 205, 11)
        self.labels(canvas, 'Description :', 315, 155, 11)

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
        get_entry2 = self.stock_textVariable.get()
        get_entry3 = self.description_text.get("1.0", END)

        try:
            CheckMedicineInput(get_entry1, get_entry2, get_entry3)
            if fu.drug_list[selected_indices[0]].Name != get_entry1:
                CheckMedicineNameIsExists(get_entry1)
            show_confirm_massageBox = err_massage.askquestion(
                "Confirm", "Are you sure?")
            if show_confirm_massageBox == 'yes':
                fu.drug_list[selected_indices[0]].Update(
                    get_entry1, get_entry2, get_entry3)
                err_massage.showinfo(
                    'Confirm', 'Update Information Successful')
                controller.frames['drug_page'].update_show_listBox()
                self.delete_entries()
                return 'drug_page'
            else:
                return 'delete_and_update_drug'
        except Exception as ErrorMessage:
            err_massage.showerror('Error', ErrorMessage)
            return 'delete_and_update_drug'

    def delete_drug(self, controller):
        show_confirm_massageBox = err_massage.askquestion(
            "Confirm", "Are you sure?")
        if show_confirm_massageBox == 'yes':
            err_massage.showinfo(
                'Confirm', 'Delete Drug Successful')
            fu.drug_list[selected_indices[0]].Delete
            del fu.drug_list[selected_indices[0]]
            controller.frames['drug_page'].update_show_listBox()
            return 'drug_page'
        else:
            return 'delete_and_update_drug'

    def delete_entries(self):
        self.Entry_1.delete(0, END)
        self.stock_textVariable.set(fu.drug_list[selected_indices[0]].Stock)
        self.description_text.delete("1.0", END)

    def Buttons(self, button_text, Command, Width, X, Y):
        Button(self, text=button_text, command=Command,
               width=Width).place(x=X, y=Y)

    def back_to_drug_page(self):
        self.delete_entries()
        fu.drug_list = LoadMedicines()
        return 'drug_page'

    def scrollbar_for_text(self):
        scrollbar = Scrollbar(self)
        text = Text(self, height=4, width=40, yscrollcommand=scrollbar.set)
        scrollbar.config(command=text.yview)
        scrollbar.place(x=695, y=148, height=68)
        text.place(x=365, y=148)
        return text

    def buy_stock(self):
        buy_stock_return = fu.drug_list[selected_indices[0]].Buy(
            self.buy_and_sell_entry.get())
        if buy_stock_return is True:
            self.stock_textVariable.set(
                fu.drug_list[selected_indices[0]].Stock)
            self.buy_and_sell_entry.delete(0, END)
        else:
            err_massage.showerror('Error', buy_stock_return)

    def sell_stock(self):
        sell_stock_return = fu.drug_list[selected_indices[0]].Sell(
            self.buy_and_sell_entry.get())
        if sell_stock_return is True:
            self.stock_textVariable.set(
                fu.drug_list[selected_indices[0]].Stock)
            self.buy_and_sell_entry.delete(0, END)
        else:
            err_massage.showerror('Error', sell_stock_return)


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
        self.title('Search Drug')
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
        search_list = FindMedicine(Name=get_Entry1)
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
