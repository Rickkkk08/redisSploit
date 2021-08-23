#!/usr/bin/env python3
import sys
from lib.Parser import Parser
from lib.Printer import Printer
from lib.Controller import Controller

# Judge system version
if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, we need Python 3.x\n")
    sys.exit(1)


class Program:
    def __init__(self):
        # Receiving parameters
        self.options = Parser().options
        # Print Banner
        Printer()
        # start attack
        Controller(self.options)


if __name__ == '__main__':
    main = Program()
