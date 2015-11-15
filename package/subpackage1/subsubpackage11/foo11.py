#!/usr/bin/python
# -*- coding: UTF-8 -*-

from package.subpackage1 import foo1


def speak():
    print("This is foo11 speaking, I'm from pakcage.subpackage1.subsubpackage11")
    print("I invoked foo1: ")
    foo1.speak()