__version__ = "0.1"
__author__ = "Humbaba"
__date__ = "2019, during the winter holiday"

import re
from cmd import Cmd
import sys

class Clsc():
    def __init__(self):
        self.__terminal__ = sys.stdout
        try:
            with open('conf.txt', "r") as f:
                self.conf = f.readlines()
        except FileNotFoundError:
            self.__terminal__.write("没有找到conf.txt。\n")
        try:
            with open('ClsC.txt', "r") as f:
                self.clsc_file = f.readlines
        except FileNotFoundError:
            self.__terminal__.write("没有找到需要分析的古诗文。\n \
                                    请按回车键退出程序，检查之后重试。\n")
            sys.exit(1)

