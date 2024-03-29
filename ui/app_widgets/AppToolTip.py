""" AppToolTip class """

# imports
from tkinter import Toplevel, Label, LEFT, SOLID

from core import load_fonts, generate_grayscale_hex

"""code from 'https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse
-cursor-in-python'"""


class AppToolTip(object):
    """ AppToolTip class """

    def __init__(self, widget):
        self.widget, self.tipwindow, self.id, self.x, self.y = widget, None, None, 0, 0

    def showtip(self, text):
        print("showtip")
        # showtip method for ToolTip class
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox('insert')
        x = x + self.widget.winfo_rootx() + 60
        y = y + cy + self.widget.winfo_rooty() + 30
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry('+%d+%d' % (x, y))
        label = Label(tw, text=self.text)
        label.configure(justify=LEFT,
                        relief=SOLID, bd=1,
                        bg=generate_grayscale_hex(60),
                        fg=generate_grayscale_hex(220),
                        font=load_fonts()['Default'])
        label.pack(ipadx=1)

    def hidetip(self):
        print("hidetip")
        # hidetip method for ToolTip class
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
