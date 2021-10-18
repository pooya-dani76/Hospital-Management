from tkinter import *


class patient_page(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.windowTitle = 'Patient Page'
        # controller.change_window_name('Patient Page')
