

from tkinter import *


def clicked():
    import get_claims
    claims = get_claims.get_claims()
    r = 0
    btn.destroy()
    for claim in claims:
        lbl = Label(window, text=claim, font=("Times New Roman", 14))
        lbl.grid(column=0, row=r)
        r += 1


window = Tk()
window.title("ТОО \"Строй Сервис Холдинг\"")
# window.geometry('400x250')
# lbl = Label(window, text="Привет", font=("Arial Bold", 50))
# lbl.grid(column=0, row=0)
btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()