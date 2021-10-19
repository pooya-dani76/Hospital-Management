from tkinter import *
from tkinter.font import BOLD
from functions import *


class hospital_page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.windowTitle = 'Hospital Page'

        backGround_image_and_text(self,'images/8.gif', 'Wellcome to Hospital')

        self.create_button('Patient Page', 340, 350,
                           lambda: controller.show_frames('patient_page'))
        self.create_button('Doctor Page', 340, 400,
                           lambda: controller.show_frames('doctor_page'))
        self.create_button('Drug Page', 340, 450,
                           lambda: controller.show_frames('drug_page'))
        self.create_button('Exit', 340, 500,
                           lambda: controller.destroy())

    def create_button(self, button_text, X, Y, Command):
        Button(self, text=button_text, width=30,
               height=2, command=Command).place(x=X, y=Y)
         
