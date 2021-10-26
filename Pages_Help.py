
from tkinter import Frame

from functions import *


class pages_help(Frame):
    def __init__(self, parent, controller, label_text,
                 background_image, previous_page, Width,
                 Height, Label_X, Label_Y,Button_X,Button_Y,button_width):
        super().__init__(parent)

        self.windowTitle = 'Help'

        backGround_image_and_text(self, background_image, 'Help')

        label = Label(self, text=label_text, width=Width, height=Height)
        label.place(x=Label_X, y=Label_Y)

        button = Button(self, text='Back',command=lambda : controller.show_frames(previous_page),width=button_width)
        button.place(x=Button_X, y=Button_Y)

        # self.backGround_image_and_texts(150,320,label_text,15,background_image)

    def backGround_image_and_texts(self, x, y, label_text, font_size, photo):
        self.backgrandImage = PhotoImage(file=photo)
        canvas = Canvas(self)
        canvas.pack(side='top', fill='both', expand=True)
        canvas.create_image(0, 0, image=self.backgrandImage, anchor="nw")
        canvas.create_text(x, y, text=label_text,
                           font=("Times New Roman", font_size, BOLD), activefill='blue',
                           disabledfill='red', fill='black')
        canvas.create_text(450, 50, text='Help',
                           font=("Times New Roman", 24, BOLD), activefill='blue',
                           disabledfill='red', fill='green')
