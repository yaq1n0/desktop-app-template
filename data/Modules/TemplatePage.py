# <template> page class

# imports

from data.MyClasses import *
from data.MyFunctions import *


class TemplatePage(object):
    def __init__(self, root):
        self.root = root

    def defaults(self):
        self.createFrame()

    def createFrame(self):
        self.mainFrame = MyFrame(self.root, GrayScale(20))
