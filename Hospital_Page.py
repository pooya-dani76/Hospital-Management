from tkinter import *
from tkinter.font import BOLD
from functions import *
from DesignFunctions import *
import tkinter.messagebox as err_massage


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

    def create_button(self, button_text, X, Y, Command):
        Button(self, text=button_text, width=30,
               height=2, command=Command).place(x=X, y=Y)

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
