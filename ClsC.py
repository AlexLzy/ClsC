__version__ = "0.1"
__author__ = "Humbaba"
__date__ = "2019, during the winter holiday"

import re
import sys


class ClsC():
    # 注意：全部的ClsC四个字母都是ClsC, 没有Clsc或是clsc，以免造成混淆。

    def __init__(self):

        self.__terminal__ = sys.stdout
        try:
            with open('conf.txt', "r") as f:
                self.conf = f.readlines()
        except FileNotFoundError:
            self.__terminal__.write("没有找到conf.txt。\n")
        try:
            with open('ClsC.txt', "r") as f:
                self.ClsC_file = f.read()
        except FileNotFoundError:
            self.__terminal__.write("没有找到需要分析的古诗文。\n \
                                    请按回车键退出程序，检查之后重试。\n")
            sys.exit(1)

    def parsed(self):
        '''
        ClsC.parsed() - 初步分析并返回古文的一些信息

        USAGE:
            ClsC.repeatch()

        CATEGORY:
            古文处理

        DESCRIPTION:  #XXX：如何较为标准地描述返回的tuple的结构？
            返回一个由古文的基础信息组成的tuple，其结构为

            (parsedfile, title, author, var):
                parsedfile:
                    由古文中每一个短句（由标点符号分割）组成的list
                    包含作者和朝代

                title:
                    古文的标题（截取第一个短句）

                author:
                    作者（和朝代）

                var:
                    古文中的备考字
        '''

        rule = re.compile(u'[^\u4e00-\u9fa5]+')
        f = re.sub('[0-9]', '', self.ClsC_file)
        var = re.findall('[({[].*?一作.*?[)}]', self.ClsC_file)
        f = re.sub('[({[].*?一作.*?[)}]', '', f)
        parsedfile = re.sub(rule, ',', f).strip().split(',')[:-1]
        title = parsedfile[0]
        author = parsedfile[1]     # 这里有可能会出现作者和朝代的解析问题
        return (parsedfile, title, author, var)

    def repeatch(self, arg=''):
        '''
        ClsC.repeatch() - 处理古文中的重复字

        USAGE:
            ClsC.repeatch(arg='')

        CATEGORY:
            古文处理

        DESCRIPTION:
            处理古文中的重复字

            -l, --log
                将结果输出到repeatch.txt中

            -v, --verbose
                啰嗦模式，生成对重复字的归纳
        '''
        # TODO: 可以试着将作者和朝代都直接排除掉
        # XXX:
        # 这里排除冗余结果是用在内部直接排除作者和朝代还是
        # 通过禁用字功能排除还有待商榷。
        try:
            if '-l' or '--log' in arg:
                sys.stdout = open('repeatch.txt', 'w')
                # 将结果写入文件,文件名为repeatch.txt且只能在代码内部更改。
            for e in set(''.join(self.parsed()[0])):  # e是古文中的每'一个字'
                if ''.join(self.parsed()[0]).count(e) == 1:
                    continue  # 如果只出现一次就跳过
                if '-v' or '--verbose' in arg:  # 唠叨模式，其实可以用来做归纳
                    sys.stdout.write("重复的字："+c+"\n==================\n")
                    for s in self.parsed()[0]:  # s指古文中的每一个短句
                        if e in s:
                            sys.stdout.write(s+"\n")
                    sys.stdout.write("\n")
                else:
                    sys.stdout.write(e+"\n")
        finally:
            sys.stdout = self.__terminal__


c = ClsC()
c.repeatch()
