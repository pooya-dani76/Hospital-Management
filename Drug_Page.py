from tkinter import *
from functions import *

class drug_page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Drug Page'
        backGround_image_and_text(self,'images/9.gif','Drug Page')
        # controller.change_window_name('Drug Page')
