#
#
# from tkinter import *
#
#
# def clicked():
#     import get_claims
#     claims = get_claims.get_claims()
#     r = 0
#     btn.destroy()
#     for claim in claims:
#         lbl = Label(window, text=claim, font=("Times New Roman", 14))
#         lbl.grid(column=0, row=r)
#         r += 1
#
#
# window = Tk()
# window.title("ТОО \"Строй Сервис Холдинг\"")
# # window.geometry('400x250')
# # lbl = Label(window, text="Привет", font=("Arial Bold", 50))
# # lbl.grid(column=0, row=0)
# btn = Button(window, text="Не нажимать!", command=clicked)
# btn.grid(column=1, row=0)
# window.mainloop()

from tkinter import *
from tkinter import ttk
import re


def is_valid(newval):
    result = re.match("^\d{0,10}$", newval) is not None
    if not result and len(newval) <= 12:
        errmsg.set("Номер телефона должен быть в формате xxxxxxxxxx, где x представляет цифру")
    else:
        errmsg.set("")
    return result


root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

check = (root.register(is_valid), "%P")

errmsg = StringVar()

phone_entry = ttk.Entry(validate="key", validatecommand=check)
phone_entry.pack(padx=5, pady=5, anchor=NW)

error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.pack(padx=5, pady=5, anchor=NW)

root.mainloop()