__version__ = "0.1"
__author__ = "Humbaba"
__date__ = "2019, during the winter holiday"

import re
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
                self.clsc_file = f.read()
        except FileNotFoundError:
            self.__terminal__.write("没有找到需要分析的古诗文。\n \
                                    请按回车键退出程序，检查之后重试。\n")
            sys.exit(1)

    def parsed(self):
        '''这个方法与list的sorted()有相似之处，调用它会直接返回处理过的对象，而
        不是处理对象。

        返回（parsedfile,title, author, var)格式的的一个tuple，
        其中 parsedfile指由每一短句组成的List，不包含备考字
        var指（一般穿插在古文中）的备考字。
        '''
        rule = re.compile(u'[^\u4e00-\u9fa5]+')
        f = re.sub('[0-9]', '', self.clsc_file)
        var = re.findall('[({[].*?一作.*?[)}]', self.clsc_file)
        f = re.sub('[({[].*?一作.*?[)}]', '', f)
        parsedfile = re.sub(rule, ',', f).strip().split(',')[:-1]
        title = parsedfile[0]
        author = parsedfile[1]     #这里有可能会出现作者和朝代的解析问题
        return (parsedfile, title, author, var)


