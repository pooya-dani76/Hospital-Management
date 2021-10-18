from tkinter import *
from tkinter.font import BOLD
from Doctor_Page import doctor_page
from Drug_Page import drug_page

from Patient_Page import patient_page


class hospital_page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.windowTitle = 'Hospital Page'

        self.backgrandImage = PhotoImage(file='images/8.gif')
        canvas = Canvas(self)
        canvas.pack(side='top', fill='both', expand=True)
        canvas.create_image(0, 0, image=self.backgrandImage, anchor="nw")
        canvas.create_text(450, 50, text='Wellcome to Hospital',
                           font=("Times New Roman", 24, BOLD), activefill='blue',
                           disabledfill='red', fill='green')

        self.create_button('Patient Page', 340, 350,
                           lambda: controller.show_frames(patient_page))
        self.create_button('Doctor Page', 340, 400,
                           lambda: controller.show_frames(doctor_page))
        self.create_button('Drug Page', 340, 450,
                           lambda: controller.show_frames(drug_page))
        self.create_button('Exit', 340, 500,
                           lambda: controller.destroy())

    def create_button(self, button_text, X, Y, Command):
        Button(self, text=button_text, width=30,
               height=2, command=Command).place(x=X, y=Y)
