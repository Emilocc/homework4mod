from tkinter import *
import random

window = Tk()
window.geometry("600x600")
window.title("Алхимик")

class Clay:
    image = PhotoImage(file=r"elements/pottery.png")


class Ground:
    image = PhotoImage(file=r"elements/water.png")

    def __add__(self,other):
        if isinstance(other,Water):


class Water:
    image=PhotoImage(file=r"")

    def __add__(self,other):
        if isinstance(other,Water):



canvas = Canvas(width=600, height=600)

window.mainloop()
