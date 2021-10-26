from tkinter import *
from tkinter.font import BOLD
from Pages_Help import pages_help
from functions import *
from DesignFunctions import *
import tkinter.messagebox as err_massage
from Pages_Help import *
from Consts import *


class hospital_page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.windowTitle = 'Hospital Page'

        backGround_image_and_text(self, 'images/8.gif', 'Wellcome to Hospital')

        self.create_button('Patient Page', 340, 350,
                           lambda: controller.show_frames(self.go_to_patient_page(controller)))
        self.create_button('Doctor Page', 340, 400,
                           lambda: controller.show_frames(self.go_to_doctor_page(controller)))
        self.create_button('Drug Page', 340, 450,
                           lambda: controller.show_frames(self.go_to_drug_page(controller)))
        self.create_button('Exit', 340, 500,
                           lambda: controller.destroy())
        self.create_button('Help', 7, 518, lambda: self.show_help(
            parent, controller), Width=3,Height=0)

    def show_help(self, parent, controller):
        A = pages_help(parent, controller,HospitalPageHelp,'images/8.gif','hospital_page',90,15,130,310,10,518,10)
        A.grid(row=0, column=0, sticky="nsew")
        A.tkraise()

    def create_button(self, button_text, X, Y, Command, Width=30, Height=2):
        Button(self, text=button_text, width=Width,
               height=Height, command=Command).place(x=X, y=Y)

    def go_to_patient_page(self, controller):
        if len(LoadDoctors()) == 0:
            err_massage.showerror('Error', "Doctor's List is Empty !!!\
                \nClick Doctor Page Button to Add a Doctor")
            return 'hospital_page'
        else:
            controller.frames['patient_page'].update_show_listBox()
            return 'patient_page'

    def go_to_doctor_page(self, controller):
        controller.frames['doctor_page'].update_show_listBox()
        return 'doctor_page'

    def go_to_drug_page(self, controller):
        controller.frames['drug_page'].update_show_listBox()
        return 'drug_page'
