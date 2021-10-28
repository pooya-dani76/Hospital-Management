import sys

sys.path.append('./Design')
sys.path.append('./Backend')

from tkinter import *
from Hospital_Page import *
from Patient_Page import *
from Doctor_Page import*
from Drug_Page import *
from Pages_Help import *


class main(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.main_Frame = Frame(self)
        self.main_Frame.pack(side='top', fill='both', expand='True')
        self.main_Frame.grid_rowconfigure(0, weight=1)
        self.main_Frame.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (hospital_page, patient_page, doctor_page,
                  drug_page, add_patient, delete_and_update_patient,
                  add_doctor, delete_and_update_doctor, add_drug,
                  delete_and_update_drug):
            frame = F(self.main_Frame, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frames(hospital_page.__name__)
        self.position()

    def show_frames(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()
        self.change_window_name(frame.windowTitle)

    def change_window_name(self, text):
        self.title(text)

    def position(self):
        w = 900
        h = 550
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/25*10) - (h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.resizable(width=False, height=False)


my_application = main()
my_application.mainloop()
