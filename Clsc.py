__version__ = "0.1"
__author__ = "Humbaba"
__date__ = "2019, during the winter holiday"

import re
from cmd import Cmd
import sys

class Outputter():
    def __init__(self, file_name="default.txt"):
        self.terminal = sys.stdout
        self.file = open(file_name, 'w+')

    def write(self, content, method):
        if method == "terminal":
            print(content)
        elif method == "file":
            sys.stdout = self.file
            print(content)

