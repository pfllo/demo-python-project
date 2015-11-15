#!/usr/bin/python
# -*- coding: UTF-8 -*-

from package.subpackage1 import foo1
from package.subpackage2 import foo2
from package.subpackage1.subsubpackage11 import foo11


def main():
    print("Hi,")
    print("This is the entrance of the demo package.")
    print("")

    print("Testing foo1: ")
    foo1.speak()
    print("")

    print("Testing foo2: ")
    foo2.speak()
    print("")

    print("Testing foo11: ")
    foo11.speak()

if __name__ == "__main__":
    main()