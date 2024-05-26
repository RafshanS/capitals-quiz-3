from tkinter import *


Button_text = ("Arial", 40, "bold")
subtitle_text = ("Arial", 20)
Title_text = ("Arial", 50)


def start_menu ():
    startmenu = Tk()
    startmenu.title("Welcome To The Asian Countries Capital Quiz")
    startmenu.size(width=1000, height = 600)
    startmenu.config(bg = "#C1E1C1")
    menu = TkLabel(startmenu, text = ("Welcome To The Asian Countries Capital Quiz"),
                   colour = "#4263f5" ,
                   background_colour = "#C1E1C1",
                   font = Title_text)
    menu.place(x=150, y=20)
    





start_menu.mainloop()
