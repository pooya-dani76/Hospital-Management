from tkinter import *
from Hospital_Page import*
from Patient_Page import *
from Doctor_Page import*
from Drug_Page import *


class pages_management(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        main_Frame = Frame(self)
        main_Frame.pack(side='top', fill='both', expand='True')
        main_Frame.grid_rowconfigure(0, weight=1)
        main_Frame.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (hospital_page, patient_page, doctor_page, drug_page):
            frame = F(main_Frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frames(hospital_page)

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


my_application = pages_management()
my_application.mainloop()
