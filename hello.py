try:
    from tkinter import *
except ImportError:
    from Tkinter import *


def main():
    root = Tk()

    w = Label(root, text="Hello, world!")
    w.pack()

    root.mainloop()

#comments
if __name__ == '__main__':
    main()
