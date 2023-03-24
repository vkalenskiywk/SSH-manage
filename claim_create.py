import tkinter as tk
from tkinter import *
from tkinter.ttk import Checkbutton
import datetime

#Получение текущей даты. Приведение к текстовому формату, 2 символа в месяце
c_d = str(datetime.datetime.now().day)
c_m = str(datetime.datetime.now().month)
if len(c_m) == 1:
    c_m = '0'+c_m
c_y = str(datetime.datetime.now().year)

#***********************************************************************************************************************
#Создание главной формы для заполнения данных по заявке
window = tk.Tk()
window.title("Новая заявка")
#window.geometry('500x250')

#***********************************************************************************************************************
#создается рамка для даты
frm_date = tk.Frame(relief=tk.FLAT, bg = "snow", master=window)#, width=500, height=100)
frm_date.pack(fill=tk.BOTH, expand=True)

ent_date_day = tk.Entry(master=frm_date, justify='center')
ent_date_day.insert(0, c_d)
lbl_date_day = tk.Label(master=frm_date, text="День", bg = "snow", fg="black")
ent_date_day.grid(row=0, column=0, sticky="e")
lbl_date_day.grid(row=1, column=0)

ent_date_mon = tk.Entry(master=frm_date, justify='center')
ent_date_mon.insert(0, c_m)
lbl_date_mon = tk.Label(master=frm_date, text="Месяц", bg = "snow", fg="black")
ent_date_mon.grid(row=0, column=1, sticky="e")
lbl_date_mon.grid(row=1, column=1)

ent_date_yr = tk.Entry(master=frm_date, justify='center')
ent_date_yr.insert(0, c_y)
lbl_date_yr = tk.Label(master=frm_date, text="Год", bg = "snow", fg="black")
ent_date_yr.grid(row=0, column=2, sticky="e")
lbl_date_yr.grid(row=1, column=2)

#***********************************************************************************************************************
#Чекбокс для указания статуса заявки (завершенная, новая)
claim_state_chk = BooleanVar()
claim_state_chk.set(False)  # задайте проверку состояния чекбокса
claim_state = Checkbutton(master=frm_date, text='Завершенное', var=claim_state_chk)
claim_state.grid(column=3, row=0)

#***********************************************************************************************************************
#Ввод основных данных
#создается рамка для ввода основных данных
frm_form = tk.Frame(relief=tk.FLAT, bg= "snow", master=window)
frm_form.pack(fill=tk.BOTH, expand=True)


# Создает ярлык и текстовое поле для ввода фамилии.
lbl_family_name = tk.Label(master=frm_form, text="Фамилия:", bg = "snow", fg="black")
ent_family_name = tk.Entry(master=frm_form, width=50)
lbl_family_name.grid(row=0, column=0, sticky="e")
ent_family_name.grid(row=0, column=1)

# Создает ярлык и текстовое поле для ввода имени.
lbl_first_name = tk.Label(master=frm_form, text="Имя:", bg = "snow", fg="black")
ent_first_name = tk.Entry(master=frm_form, width=50)
lbl_first_name.grid(row=1, column=0, sticky="e")
ent_first_name.grid(row=1, column=1)

# Создает ярлык и текстовое поле для ввода отчества.
lbl_father_name = tk.Label(master=frm_form, text="Отчество (если есть):", bg = "snow", fg="black")
ent_father_name = tk.Entry(master=frm_form, width=50)
lbl_father_name.grid(row=2, column=0, sticky="e")
ent_father_name.grid(row=2, column=1)

# Создает ярлык и текстовое поле для ввода ИИН.
lbl_iin = tk.Label(master=frm_form, text="ИИН:", bg = "snow", fg="black")
ent_iin = tk.Entry(master=frm_form, width=50)
lbl_iin.grid(row=3, column=0, sticky="e")
ent_iin.grid(row=3, column=1)

# Создает ярлык и текстовое поле для ввода адреса газификации.
lbl_address = tk.Label(master=frm_form, text="Адрес газификации:", bg = "snow", fg="black")
ent_address = tk.Entry(master=frm_form, width=50)
lbl_address.grid(row=4, column=0, sticky="e")
ent_address.grid(row=4, column=1)

# Создает ярлык и текстовое поле для ввода района.
lbl_region = tk.Label(master=frm_form, text="Регион:", bg = "snow", fg="black")
ent_region = tk.Entry(master=frm_form, width=50)
lbl_region.grid(row=5, column=0, sticky="e")
ent_region.grid(row=5, column=1)

#***********************************************************************************************************************
frm_telnum = tk.Frame(relief=tk.FLAT, bg= "snow", master=window)
frm_telnum.pack(fill=tk.BOTH, expand=True)

#Создает ярлык и текстовое поле для ввода телефона.
ent_tel_number = ['']
ent_tel_name = ['']
lbl_tel_number = ['']
lbl_tel_name = ['']

#Поля для ввода телефона и контактного имени
lbl_tel_number[0] = tk.Label(master=frm_telnum, text="Телефон: +7", bg = "snow", fg="black")
ent_tel_number[0] = tk.Entry(master=frm_telnum, width=10)
lbl_tel_number[0].grid(row=0, column=0)#, sticky="e")
ent_tel_number[0].grid(row=0, column=1)

lbl_tel_name[0] = tk.Label(master=frm_telnum, text="контактное лицо:", bg = "snow", fg="black")
ent_tel_name[0] = tk.Entry(master=frm_telnum, width=30)
lbl_tel_name[0].grid(row=0, column=2)#, sticky="e")
ent_tel_name[0].grid(row=0, column=3)


#***********************************************************************************************************************
#Добавление телефонов
def add_tel():
    global ent_tel_number, lbl_tel_number, ent_tel_name, lbl_tel_name
    ent_tel_number.append(tk.Entry(master=frm_telnum, width=10))
    ent_tel_number[-1].grid(row=len(ent_tel_number), column=1)

    lbl_tel_number.append(tk.Label(master=frm_telnum, text="Телефон: +7", bg = "snow", fg="black"))
    lbl_tel_number[-1].grid(row=len(lbl_tel_number), column=0)

    ent_tel_name.append(tk.Entry(master=frm_telnum, width=30))
    ent_tel_name[-1].grid(row=len(ent_tel_name), column=3)

    lbl_tel_name.append(tk.Label(master=frm_telnum, text="контактное лицо:", bg = "snow", fg="black"))
    lbl_tel_name[-1].grid(row=len(lbl_tel_name), column=2)
#Удаление телефонов
def remove_tel():
    global ent_tel_number, lbl_tel_number, ent_tel_name, lbl_tel_name
    if len(ent_tel_number)>1:
        ent_tel_number[-1].destroy()
        ent_tel_number.pop(-1)
    else:
        pass
    if len(lbl_tel_number)>1:
        lbl_tel_number[-1].destroy()
        lbl_tel_number.pop(-1)
    else:
        pass
    if len(ent_tel_name)>1:
        ent_tel_name[-1].destroy()
        ent_tel_name.pop(-1)
    else:
        pass
    if len(lbl_tel_name)>1:
        lbl_tel_name[-1].destroy()
        lbl_tel_name.pop(-1)
    else:
        pass

#***********************************************************************************************************************
#Кнопки добавления и удаления телефона
frm_buttons = tk.Frame(master=window)
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_add = tk.Button(master=frm_buttons, text="+ Добавить контактный номер", bg = "snow", fg="black", command=add_tel)
btn_add.pack(side=tk.RIGHT, padx=10, ipadx=10)

btn_minus = tk.Button(master=frm_buttons, text="- Убрать контактный номер", bg = "snow", fg="black", command=remove_tel)
btn_minus.pack(side=tk.RIGHT, ipadx=10)

#***********************************************************************************************************************
# кнопки передачи данных далее
frm_nextbuttons = tk.Frame(master=window)
frm_nextbuttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_next = tk.Button(master=frm_nextbuttons, text="Далее", bg = "snow", fg="black")
btn_next.pack(side=tk.RIGHT, padx=10, ipadx=10)
#***********************************************************************************************************************
window.mainloop()