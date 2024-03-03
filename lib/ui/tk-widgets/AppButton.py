""" AppButton class """

# imports
from tkinter import Button, RIDGE

<<<<<<< Updated upstream:lib/widgets/AppButton.py
from lib.AppState import AppState
from lib.functions import generate_grayscale_hex
=======
from lib.preferences import *
from lib.functions import *
>>>>>>> Stashed changes:lib/ui/tk-widgets/AppButton.py


class AppButton(Button):
    """ AppButton class """
    bgcolor, fgcolor, relwidth, relheight = generate_grayscale_hex(40), generate_grayscale_hex(220), 0.10, 0.05
    abgcolor, afgcolor = bgcolor, fgcolor

    def __init__(self, parent, text, command, relx, rely):
        self.text, self.command, self.relx, self.rely = text, command, relx, rely

        Button.__init__(self, parent)

        self.configure_()
        self.place_()

    def configure_(self):
        # load AppState fonts
        fonts = AppState().fonts

        self.configure(text=self.text, command=self.command,
                       font=fonts['DefaultBold'],
                       bg=self.bgcolor, fg=self.fgcolor,
                       activebackground=self.abgcolor, activeforeground=self.afgcolor,
                       relief=RIDGE, highlightthickness=0, bd=0)

    def place_(self):
        self.place(relx=self.relx, rely=self.rely, relwidth=self.relwidth, relheight=self.relheight)