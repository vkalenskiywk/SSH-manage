import tkinter as tk

def add_eq():
    global ent_family_name
    ent_family_name.append(tk.Entry(master=frm_form, width=50))
    ent_family_name[-1].grid(row=len(ent_family_name), column=0)

def remove_eq():
    global ent_family_name
    if len(ent_family_name)>1:
        ent_family_name[-1].destroy()
        ent_family_name.pop(-1)
    else:
        pass


window = tk.Tk()
window.title("Новая заявка")
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3, bg = "snow", master=window)
frm_form.pack()

ent_family_name = ['']


ent_family_name[0] = tk.Entry(master=frm_form, width=50)
ent_family_name[0].grid(row=0, column=0)

frm_buttons = tk.Frame(master=window)
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_add = tk.Button(master=frm_buttons, text="Добавить оборудование", command=add_eq, bg = "snow", fg="black")
btn_add.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_minus = tk.Button(master=frm_buttons, text="убрать строчку", command=remove_eq, bg = "snow", fg="black")
btn_minus.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()