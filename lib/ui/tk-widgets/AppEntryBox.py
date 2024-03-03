""" AppEntryBox class """

# imports
from tkinter import Entry, RIDGE

<<<<<<< Updated upstream:lib/widgets/AppEntryBox.py
from lib.app_root import generate_fonts
from lib.functions import generate_grayscale_hex
=======
from lib.preferences import *
from lib.functions import *
>>>>>>> Stashed changes:lib/ui/tk-widgets/AppEntryBox.py
from .AppLabel import AppLabel


class AppEntryBox(Entry):
    """ AppEntryBox class """
    charwidth, bgcolor, fgcolor = 20, generate_grayscale_hex(20), generate_grayscale_hex(220)

    def __init__(self, parent, text, relx, rely):
        self.parent, self.text, self.relx, self.rely = parent, text, relx, rely

        Entry.__init__(self, self.parent)

        self.defaults()

    def defaults(self):
        self.entryConfigure()
        self.entryPlace()
        self.createLabel()

    def entryConfigure(self):
        self.configure(width=self.charwidth, font=generate_fonts()['Default'],
                       bg=self.bgcolor, fg=self.fgcolor,
                       relief=RIDGE, highlightthickness=2, bd=0)

    def entryPlace(self):
        self.place(relx=self.relx, rely=self.rely)

    def createLabel(self):
        self.label = AppLabel(self.parent, self.text, self.relx, self.rely - 0.050)
        self.label.configure(font=generate_fonts()['Large'])