from tkinter import *
from tkinter.font import BOLD
from DesignFunctions import *


def backGround_image_and_text(self, photo, text):
    self.backgrandImage = PhotoImage(file=photo)
    canvas = Canvas(self)
    canvas.pack(side='top', fill='both', expand=True)
    canvas.create_image(0, 0, image=self.backgrandImage, anchor="nw")
    canvas.create_text(450, 50, text=text,
                       font=("Times New Roman", 24, BOLD), activefill='blue',
                       disabledfill='red', fill='red')


def labels(Canvas, Text, x, y, font_size):
    Canvas.create_text(x, y, text=Text,
                       font=("Times New Roman", font_size, BOLD), activefill='blue',
                       disabledfill='red', fill='green')


# [y.NationalNumber  for y in mylist].index(x.NationalNumber)+1

def update_doctors_to_dropDown():
    mylist = LoadDoctors()
    VisitorDoctorNationalNumber_list = list(
        map(lambda x: f'{x.id}. Dr.{x.FirstName} {x.LastName}', LoadDoctors()))
    return VisitorDoctorNationalNumber_list


patient_list = []


doctor_list = []

drug_list = []
# selected_indices = None
# patient_list = LoadPatients()
