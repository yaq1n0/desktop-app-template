""" AppEntryBox class """

# imports
from tkinter import Entry, RIDGE

from core import generate_grayscale_hex, load_fonts
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
        self.configure(width=self.charwidth, font=load_fonts()['Default'],
                       bg=self.bgcolor, fg=self.fgcolor,
                       relief=RIDGE, highlightthickness=2, bd=0)

    def entryPlace(self):
        self.place(relx=self.relx, rely=self.rely)

    def createLabel(self):
        self.label = AppLabel(self.parent, self.text, self.relx, self.rely - 0.050)
        self.label.configure(font=load_fonts()['Large'])
