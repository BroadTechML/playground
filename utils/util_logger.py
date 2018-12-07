# -*- coding: utf-8 -*-
# Date: 2018/11/30 0030
# Author: Stone
# log

import sys


class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


'''
eg:

from util_logger import Logger

sys.stdout = Logger("mylog.log")
'''
