#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, random

try:
    from tkinter import *
except ImportError:
    from Tkinter import *    

def main():
    assert os.path.exists("names.txt"), 'Cannot find names.txt.'
    namesFileRead = open("names.txt", 'r')
    content = namesFileRead.readlines()
    namesFileRead.close()
    name = content[random.randint(0, len(content) - 1)].rstrip('\r\n')
    
    root = Tk()
    
    w = Label(root, text = "Hello, " + name + "!")
    w.pack()
    
    root.mainloop()

#comments
if __name__ == '__main__': main()
