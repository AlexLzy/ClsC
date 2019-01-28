__version__ = "0.1"
__author__ = "Humbaba"
__date__ = "2019, during the winter holiday"

import re
from cmd import Cmd

class ClsC():

    def __init__(self):
        try:
            with open('./ClsC.txt', "r") as f:
                self.clsc = f.read()
                self.cleaned = re.sub("[[(<].*?[])>]", "", self.clsc)
                self.cleaned = re.sub("[^\u4e00-\u9fa5]+", ",", self.cleaned).strip(",")
        except FileNotFoundError:
            i = input('没有找到目录下的Clsc.txt。请阅读readme.md并检查。\
                  \n按回车键退出。')
            exit(1)

        try:
            with open('./conf.txt', "r") as f:
                br = re.compile("禁用字.*?(.*?);;")
                self.banned = re.findall(br, f.read())
        except FileNotFoundError:
            i = input("没有在目录下找到conf.txt配置文件。请阅读readme.md并检查。\
                      \n按回车键继续。")


    def variable(self):
        f = re.findall('\(.*?一作.*?\)', self.clsc)
        return f #查找文章中的备考字。

    def repeatch(self, arg):
        for i in set(self.cleaned):
            if not arg:
                if i != "," and self.cleaned.count(i) > 1 and i not in self.banned:
                    yield i #一词多义
            if arg == "__raw_data__":
                if i != "," and self.cleaned.count(i) > 1:
                    yield i

class Main(Cmd):

    def __init__(self):
        super().__init__()
        self.prompt = ">>"
        self.c = ClsC()
        self.intro = "欢迎使用ClsC古文处理" + __version__ + "版本。输入help来查看文档。"

    def do_rep(self, line): #这个方法可以列出重复字。注意：不是归纳。
        def file(arg):
            with open("./重复字.txt", "w")as f:
                for c in self.c.repeatch(arg):
                    f.write(c)

        def printty(arg):
            for c in self.c.repeatch(arg):
                print(c)

        if not line:
            printty("")
        elif "-r" in line:
            if "-f" in line:
                file("__raw_data__")
            elif "__internal__" in line:
                return [o for o in self.c.repeatch("__raw_data__")]
            else:
                printty("__raw_data__")
        elif "-f" in line:
            file("")
        elif "__internal__" in line:
            return [o for o in self.c.repeatch("")]
            #这样应该不太规范？让这个方法既可以直接被在命令行中被调用也可以被其他方法调用

        #真TM累赘
        #干干巴巴的，麻麻赖赖的，一点都不简洁

    def help_rep(self):
        print("简单地返回古文中重复的字。不会包括conf.txt中禁用的字以防止过度冗余的结果出现。")

    def do_sum_rep(self,line):
        ch = self.do_rep("__internal__")
        if not line:
            for character in ch:
                print("重复出现的词：" + character)
                for p in self.c.cleaned.split(","):#这里是每一个字的重复字查找。
                    if character in p:
                        print(p)
                print("============\n")
        elif "-f" in line:
            with open("./一词多义归纳") as f:
                f.write("重复出现的词：" + character)
                for p in self.c.cleaned.split(","):#这里是每一个字的重复字查找。
                     if character in p:
                         f.write(p)
                f.write("=============\n")

    def help_sum_rep(self):
        print("""\t\t这个方法可以返回古文中包含重复字的分句，可以被方便地用作“一词多义”古文现象的研究。
        不会包括conf.txt中的禁用字以防止大量冗余结果的出现。
        参数：
        -f     在目录中生成归纳文件
        -r     忽略禁用字。（不推荐！很可能会生成大量冗余无意义结果！）
        """)

    def do_exit(self, lines):
        return True

    def default(self, line):
        print("没有找到命令:" + str(line))


__name__ = "__testing__"

if __name__ == "__testing__":
    m = Main()
    print("程序目前处于测试版本")
    m.cmdloop()

