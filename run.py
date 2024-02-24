# template for Python Desktop App using Tkinter

from os import execv
from sys import executable, argv
# imports
from tkinter import Tk

from data.Modules import StartPage
from data.MyFunctions import GrayScale, makeGeometry
from data.MyVariables.preferences import dev
from data.MyVariables.preferences import height as config_height
from data.MyVariables.preferences import width as config_width


# functions
def programRestart(*args):
    if dev:
        print('[program] restart')

    # code from 'https://blog.petrzemek.net/2014/03/23/restarting-a-python-script-within-itself/'
    execv(executable, ['python'] + argv)

    return None


def programQuit(*args):
    if dev:
        print('[program] quit')

    exit()

    return None


# creating root
root = Tk()
root.title('MyApp')
root.iconbitmap('data/images/favicon.ico')
root.resizable(False, False)
root.geometry(makeGeometry(root, config_width, config_height))
root.configure(bg=GrayScale(20))

# creating StartPage instance 'startPage'
startPage = StartPage(root)


def raiseStart(*args):
    root.geometry(makeGeometry(root, int(config_height / 2), config_height))
    startPage.mainFrame.tkraise()


raiseStart()

# binds
root.bind('<Control-q>', programQuit)
root.bind('<Control-r>', programRestart)
root.bind('<Escape>', raiseStart)

# mainloop
root.mainloop()
