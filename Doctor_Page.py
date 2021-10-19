from tkinter import *
from functions import *


class doctor_page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Doctor Page'
        backGround_image_and_text(self,'images/1.gif','Doctor Page')

