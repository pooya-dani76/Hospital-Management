from tkinter import *
from Hospital_Page import *


class patient_page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Patient Page'

        # controller.frames[hospital_page].backGround_image_and_text('images/8.gif','Wellcome to Hospital')

