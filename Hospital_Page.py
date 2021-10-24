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
                           lambda: controller.show_frames(self.show_error_for_empty_patientList()))
        self.create_button('Doctor Page', 340, 400,
                           lambda: controller.show_frames('doctor_page'))
        self.create_button('Drug Page', 340, 450,
                           lambda: controller.show_frames('drug_page'))
        self.create_button('Exit', 340, 500,
                           lambda: controller.destroy())

    def create_button(self, button_text, X, Y, Command):
        Button(self, text=button_text, width=30,
               height=2, command=Command).place(x=X, y=Y)

    def show_error_for_empty_patientList(self):
        if len(LoadDoctors()) == 0:
            err_massage.showerror('Error', "Doctor's List is Empty !!!\
                \nClick Doctor Page Button to Add a Doctor")
            return 'hospital_page'
        else:
            return 'patient_page'
