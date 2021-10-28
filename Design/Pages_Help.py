from tkinter import Frame
from functions import *


class pages_help(Frame):
    def __init__(self, parent, controller, label_text,
                 background_image, previous_page, Width,
                 Height, Label_X, Label_Y, Button_X, Button_Y, button_width):
        super().__init__(parent)

        self.windowTitle = 'Help'

        backGround_image_and_text(self, background_image, 'Help')

        label = Label(self, text=label_text, width=Width, height=Height)
        label.place(x=Label_X, y=Label_Y)

        button = Button(self, text='Back', command=lambda: controller.show_frames(
            previous_page), width=button_width)
        button.place(x=Button_X, y=Button_Y)
