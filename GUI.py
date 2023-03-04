import tkinter as tk
from tkinter import Entry
from tkinter import Frame
from tkinter import Label
from tkinter import Canvas
import os
import Pmw


class GUI:
    def __init__(self, firstFile, secondFile):
        self.__root = tk.Tk()
        self.__root.resizable(False, False)
        canvas = Canvas()
        v = tk.IntVar()
        self.__root.title("tkdiff")
        frame1 = Frame(self.__root, padx=5, pady=5)
        frame2 = Frame(self.__root, padx=5, pady=5)
        frame1.grid(row=0, column=0)
        frame2.grid(row=0, column=1)

        label1 = Label(frame1, text="File1")
        label2 = Label(frame2, text="File2")
        label1.grid(row=0, column=0)
        label2.grid(row=0, column=0)

        path1 = Entry(frame1, width=45, borderwidth=2)
        path2 = Entry(frame2, width=45, borderwidth=2)
        path1.grid(row=2, column=0)
        path2.grid(row=2, column=0)
        path1.insert(0, os.getcwd() + "/" + firstFile)
        path2.insert(0, os.getcwd() + "/" + secondFile)
        self.__file_lines1 = Pmw.ScrolledText(frame1, borderframe=1,
                                              text_width=60, text_height=25,
                                              hscrollmode="static", text_wrap='none', vscrollmode="static")
        self.__file_lines1.grid(row=5, column=0)

        self.__file_lines2 = Pmw.ScrolledText(frame2, borderframe=1,
                                       text_width=60, text_height=25,
                                       hscrollmode="static", text_wrap='none', vscrollmode="static")
        self.__file_lines2.grid(row=5, column=0)

        self.__file_lines1.tag_configure('yellow', background='yellow')
        self.__file_lines2.tag_configure('yellow', background='yellow')
        self.__file_lines1.tag_configure('green', background='green')
        self.__file_lines2.tag_configure('green', background='green')
        self.__file_lines1.tag_configure('red', background='red')
        self.__file_lines2.tag_configure('red', background='red')
        self.__file_lines1.tag_configure('blue', background='blue')
        self.__file_lines2.tag_configure('blue', background='blue')
        self.__file_lines1.tag_configure('orange', background='orange')
        self.__file_lines2.tag_configure('orange', background='orange')
        frame3 = Frame(self.__root, padx=5, pady=5)
        frame3.grid(row=1, column=0, columnspan=2)
        label3 = Label(frame3, text="green:same	", fg="green")
        label3.grid(row=1, column=0)
        label4 = Label(frame3, text="yellow:changed	", fg="yellow")
        label4.grid(row=1, column=1)
        label5 = Label(frame3, text="red:deleted	", fg="red")
        label5.grid(row=1, column=2)
        label6 = Label(frame3, text="blue:added	", fg="blue")
        label6.grid(row=1, column=3)
        label7 = Label(frame3, text="orange:chars changed	", fg="orange")
        label7.grid(row=1, column=4)

    def add_red_text(self, n, text, start, end):
        if n == 0:
            self.__file_lines1.insert("end", text)
            self.__file_lines1.tag_add("red", start, end)
        else:
            self.__file_lines2.insert("end", text)
            self.__file_lines2.tag_add("red", start, end)

    def add_yellow_text(self, n, text, start, end):
        if n == 0:
            self.__file_lines1.insert("end", text)
            self.__file_lines1.tag_add("yellow", start, end)
        else:
            self.__file_lines2.insert("end", text)
            self.__file_lines2.tag_add("yellow", start, end)

    def add_blue_text(self, n, text, start, end):
        if n == 0:
            self.__file_lines1.insert("end", text)
            self.__file_lines1.tag_add("blue", start, end)
        else:
            self.__file_lines2.insert("end", text)
            self.__file_lines2.tag_add("blue", start, end)

    def add_orange_text(self, n, text, start, end):
        if n == 0:
            self.__file_lines1.insert("end", text)
            self.__file_lines1.tag_add("orange", start, end)
        else:
            self.__file_lines2.insert("end", text)
            self.__file_lines2.tag_add("orange", start, end)

    def add_green_text(self, n, text, start, end):
        if n == 0:
            self.__file_lines1.insert("end", text)
            self.__file_lines1.tag_add("green", start, end)
        else:
            self.__file_lines2.insert("end", text)
            self.__file_lines2.tag_add("green", start, end)

    def highLightText(self, n, color, start, end):
        if n == 0:
            self.__file_lines1.tag_add(color, start, end)
        else:
            self.__file_lines2.tag_add(color, start, end)
    def mainLoop(self):
        self.__root.mainloop()
