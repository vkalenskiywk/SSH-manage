import tkinter as tk
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
# from tkinter import ttk
# from tkinter.ttk import Checkbutton
# Userfunction
import datetime
import checkdate
import get_need_val





def new_claim(fonts_name, fonts_size):
    #GUI


    #Получение текущей даты. Приведение к текстовому формату, 2 символа в месяце
    c_d = str(datetime.datetime.now().day)
    c_m = str(datetime.datetime.now().month)
    if len(c_m) == 1:
        c_m = '0'+c_m
    c_y = str(datetime.datetime.now().year)
    font_size = fonts_size
    font_type = fonts_name

    #***********************************************************************************************************************
    #Создание главной формы для заполнения данных по заявке
    window = tk.Toplevel()
    # window = tk.Tk()
    window.title("Новая заявка")
    #window.geometry('500x250')

    #***********************************************************************************************************************
    #создается рамка для даты
    frm_date = tk.Frame(relief=tk.FLAT, bg = "snow", master=window)#, width=500, height=100)
    frm_date.pack(fill=tk.BOTH, expand=True)

    ent_date_day = tk.Entry(master=frm_date, justify='center', font=(font_type, font_size))
    ent_date_day.insert(0, c_d)
    lbl_date_day = tk.Label(master=frm_date, text="День", bg = "snow", fg="black", font=(font_type, font_size))
    ent_date_day.grid(row=0, column=0, sticky="e")
    lbl_date_day.grid(row=1, column=0)

    ent_date_mon = tk.Entry(master=frm_date, justify='center', font=(font_type, font_size))
    ent_date_mon.insert(0, c_m)
    lbl_date_mon = tk.Label(master=frm_date, text="Месяц", bg = "snow", fg="black", font=(font_type, font_size))
    ent_date_mon.grid(row=0, column=1, sticky="e")
    lbl_date_mon.grid(row=1, column=1)

    ent_date_yr = tk.Entry(master=frm_date, justify='center', font=(font_type, font_size))
    ent_date_yr.insert(0, c_y)
    lbl_date_yr = tk.Label(master=frm_date, text="Год", bg = "snow", fg="black", font=(font_type, font_size))
    ent_date_yr.grid(row=0, column=2, sticky="e")
    lbl_date_yr.grid(row=1, column=2)

    #***********************************************************************************************************************
    #Чекбокс для указания статуса заявки (завершенная, новая)

    # enabled_on = "Завершенное"
    # enabled_off = "Новое"
    # enabled = StringVar(value=enabled_off)
    # claim_state = Checkbutton(master=frm_date, textvariable=enabled, variable=enabled, offvalue=enabled_off, onvalue=enabled_on)
    # claim_state.grid(column=3, row=0)
    claim_state_chk = BooleanVar()
    claim_state_chk.set(False)  # задайте проверку состояния чекбокса
    claim_state = Checkbutton(master=frm_date, text='Завершенное', var=claim_state_chk, font=(font_type, font_size))
    claim_state.grid(column=3, row=0)

    #***********************************************************************************************************************
    #кнопка "Сегодня" для установки даты
    def insert_today():
        ent_date_mon.delete(0, tk.END)
        ent_date_mon.insert(0, c_m)
        ent_date_day.delete(0, tk.END)
        ent_date_day.insert(0, c_d)
        ent_date_yr.delete(0, tk.END)
        ent_date_yr.insert(0, c_y)
        lbl_date_day.configure(bg="snow", fg="black")
        lbl_date_mon.configure(bg="snow", fg="black")
        lbl_date_yr.configure(bg="snow", fg="black")



    btn_today = tk.Button(master=frm_date, text="сегодня", bg = "green", fg="black", command=insert_today, font=(font_type, font_size))
    btn_today.grid(column=3, row=1)

    #***********************************************************************************************************************
    #Ввод основных данных
    #создается рамка для ввода основных данных
    frm_form = tk.Frame(relief=tk.FLAT, bg= "snow", master=window)
    frm_form.pack(fill=tk.BOTH, expand=True)


    # Создает ярлык и текстовое поле для ввода фамилии.
    lbl_family_name = tk.Label(master=frm_form, text="Фамилия:", bg = "snow", fg="black", font=(font_type, font_size))
    ent_family_name = tk.Entry(master=frm_form, width=50, font=(font_type, font_size))
    lbl_family_name.grid(row=0, column=0, sticky="e")
    ent_family_name.grid(row=0, column=1)

    # Создает ярлык и текстовое поле для ввода имени.
    lbl_first_name = tk.Label(master=frm_form, text="Имя:", bg = "snow", fg="black", font=(font_type, font_size))
    ent_first_name = tk.Entry(master=frm_form, width=50, font=(font_type, font_size))
    lbl_first_name.grid(row=1, column=0, sticky="e")
    ent_first_name.grid(row=1, column=1)

    # Создает ярлык и текстовое поле для ввода отчества.
    lbl_father_name = tk.Label(master=frm_form, text="Отчество (если есть):", bg = "snow", fg="black", font=(font_type, font_size))
    ent_father_name = tk.Entry(master=frm_form, width=50, font=(font_type, font_size))
    lbl_father_name.grid(row=2, column=0, sticky="e")
    ent_father_name.grid(row=2, column=1)

    # Создает ярлык и текстовое поле для ввода ИИН.
    lbl_iin = tk.Label(master=frm_form, text="ИИН:", bg = "snow", fg="black", font=(font_type, font_size))
    ent_iin = tk.Entry(master=frm_form, width=50, font=(font_type, font_size))
    lbl_iin.grid(row=3, column=0, sticky="e")
    ent_iin.grid(row=3, column=1)

    # Создает ярлык и текстовое поле для ввода адреса газификации.
    lbl_address = tk.Label(master=frm_form, text="Адрес газификации:", bg = "snow", fg="black", font=(font_type, font_size))
    ent_address = tk.Entry(master=frm_form, width=50, font=(font_type, font_size))
    lbl_address.grid(row=4, column=0, sticky="e")
    ent_address.grid(row=4, column=1)

    # Создает ярлык и текстовое поле для ввода района.
    lbl_region = tk.Label(master=frm_form, text="Регион:", bg = "snow", fg="black", font=(font_type, font_size))
    ent_region = tk.Entry(master=frm_form, width=50, font=(font_type, font_size))
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
    lbl_tel_number[0] = tk.Label(master=frm_telnum, text="Телефон: +7", bg = "snow", fg="black", font=(font_type, font_size))
    ent_tel_number[0] = tk.Entry(master=frm_telnum, width=15, font=(font_type, font_size))
    lbl_tel_number[0].grid(row=0, column=0)#, sticky="e")
    ent_tel_number[0].grid(row=0, column=1)

    lbl_tel_name[0] = tk.Label(master=frm_telnum, text="контактное лицо:", bg = "snow", fg="black", font=(font_type, font_size))
    ent_tel_name[0] = tk.Entry(master=frm_telnum, width=20, font=(font_type, font_size))
    lbl_tel_name[0].grid(row=0, column=2)#, sticky="e")
    ent_tel_name[0].grid(row=0, column=3)


    #***********************************************************************************************************************
    #Добавление телефонов
    def add_tel():
        # global ent_tel_number, lbl_tel_number, ent_tel_name, lbl_tel_name
        ent_tel_number.append(tk.Entry(master=frm_telnum, width=15, font=(font_type, font_size)))
        ent_tel_number[-1].grid(row=len(ent_tel_number), column=1)

        lbl_tel_number.append(tk.Label(master=frm_telnum, text="Телефон: +7", bg = "snow", fg="black", font=(font_type, font_size)))
        lbl_tel_number[-1].grid(row=len(lbl_tel_number), column=0)

        ent_tel_name.append(tk.Entry(master=frm_telnum, width=20, font=(font_type, font_size)))
        ent_tel_name[-1].grid(row=len(ent_tel_name), column=3)

        lbl_tel_name.append(tk.Label(master=frm_telnum, text="контактное лицо:", bg = "snow", fg="black", font=(font_type, font_size)))
        lbl_tel_name[-1].grid(row=len(lbl_tel_name), column=2)
    #Удаление телефонов
    def remove_tel():
        # global ent_tel_number, lbl_tel_number, ent_tel_name, lbl_tel_name
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

    btn_add = tk.Button(master=frm_buttons, text="+ Добавить контактный номер", bg = "snow", fg="black", command=add_tel, font=(font_type, font_size))
    btn_add.pack(side=tk.RIGHT, padx=10, ipadx=10)

    btn_minus = tk.Button(master=frm_buttons, text="- Убрать контактный номер", bg = "snow", fg="black", command=remove_tel, font=(font_type, font_size))
    btn_minus.pack(side=tk.RIGHT, ipadx=10)

    #***********************************************************************************************************************
    #Функция очистки формы
    def clear_claim():
        # global ent_tel_number, lbl_tel_number, ent_tel_name, lbl_tel_name
        ent_date_mon.delete(0, tk.END)
        ent_date_mon.insert(0, c_m)
        ent_date_day.delete(0, tk.END)
        ent_date_day.insert(0, c_d)
        ent_date_yr.delete(0, tk.END)
        ent_date_yr.insert(0, c_y)
        ent_family_name.delete(0, tk.END)
        lbl_family_name.configure(text="Фамилия:", bg = "snow", fg="black")
        ent_first_name.delete(0, tk.END)
        lbl_first_name.configure(text="Имя:", bg="snow", fg="black")
        ent_father_name.delete(0, tk.END)
        ent_iin.delete(0, tk.END)
        lbl_iin.configure(text="ИИН:", bg="snow", fg="black")
        ent_address.delete(0, tk.END)
        lbl_address.configure(text="Адрес газификации:", bg="snow", fg="black")
        ent_region.delete(0, tk.END)
        lbl_region.configure(text="Регион:", bg="snow", fg="black")
        lbl_date_day.configure(bg="snow", fg="black")
        lbl_date_mon.configure(bg="snow", fg="black")
        lbl_date_yr.configure(bg="snow", fg="black")
        for i in range(len(ent_tel_number)):
            ent_tel_number[i].delete(0, tk.END)
            lbl_tel_number[i].configure(text="Телефон: +7", bg = "snow", fg="black")
            ent_tel_name[i].delete(0, tk.END)


    #***********************************************************************************************************************
    #***********************************************************************************************************************
    #***********************************************************************************************************************
    #Функции проверки и передачи данных на следующий этап
    def create_claim():
        global claim
        # global ent_tel_number
        # идентификатор ошибок в ключевых полях
        error = 0
        # Проверка поля фамилии, на внесение, удаление цифр.
        family=get_need_val.get_str(ent_family_name.get())
        ent_family_name.delete(0, tk.END)
        ent_family_name.insert(0, family)
        if len(family) == 0:
            lbl_family_name.configure(text="Введите фамилию!:", fg="red", bg = "black")
            error = 1
        else:
            lbl_family_name.configure(text="Фамилия:", bg="snow", fg="black")

        # Проверка поля имени, на внесение, удаление цифр
        name = get_need_val.get_str(ent_first_name.get())
        ent_first_name.delete(0, tk.END)
        ent_first_name.insert(0, name)
        if len(name) == 0:
            lbl_first_name.configure(text="Введите имя!:", fg="red", bg = "black")
            error = 1
        else:
            lbl_first_name.configure(text="Имя:", bg="snow", fg="black")

        # Удаление цифр из отчества
        fathername = get_need_val.get_str(ent_father_name.get())
        ent_father_name.delete(0, tk.END)
        ent_father_name.insert(0, fathername)

        # Проверка ИИН на внесение, удаление букв, пробелов, на количество цифр равное 12!
        iin = get_need_val.get_value(ent_iin.get())
        ent_iin.delete(0, tk.END)
        ent_iin.insert(0, iin)
        if len(iin) != 12:
            lbl_iin.configure(text="Введите корректный ИИН!:", fg="red", bg = "black")
            error = 1
        else:
            lbl_iin.configure(text="ИИН:", bg="snow", fg="black")

        # Проверка адреса на внесение
        adresse = ent_address.get()
        if len(adresse) == 0:
            lbl_address.configure(text="Введите адрес газификации!:", fg="red", bg="black")
            error = 1
        else:
            lbl_address.configure(text="Адрес газификации:", bg="snow", fg="black")

        # Проверка региона на внесение
        region = ent_region.get()
        if len(region) == 0:
            lbl_region.configure(text="Введите регион!:", fg="red", bg="black")
            error = 1
        else:
            lbl_region.configure(text="Регион:", bg="snow", fg="black")

        # Для проверки телефонного номера, на внесение, на 10 цифр
        for i in range(len(ent_tel_number)):
            phone1 = ent_tel_number[i].get()
            if len(phone1) == 0:
                lbl_tel_number[i].configure(text="Введите номер телефона!: +7", fg="red", bg="black")
                error = 1
            else:
                phone = get_need_val.get_value(phone1)
                ent_tel_number[i].delete(0, tk.END)

                if len(phone) == 10:
                    ent_tel_number[i].insert(0, phone)
                    lbl_tel_number[i].configure(text="Телефон: +7", bg="snow", fg="black")
                else:
                    lbl_tel_number[i].configure(text="Введите корректный номер телефона!: +7", fg="red", bg="black")
                    ent_tel_number[i].insert(0, phone)
                    error = 1

        # Для проверки даты, дни от 0 до 31, месяц от 1 до 12, год от 1900 до текущего. Если в месяц, день <10, добавляется 0!
        c_duser = get_need_val.get_value(ent_date_day.get())
        d_err = checkdate.checkdate_d(c_duser)
        if (d_err == 2) & (len(c_duser)<2):
            c_duser = '0'+c_duser
        c_muser = get_need_val.get_value(ent_date_mon.get())
        m_err = checkdate.checkdate_m(c_muser)
        if (m_err == 2) & (len(c_muser)<2):
            c_muser = '0'+c_muser
        c_yuser = get_need_val.get_value(ent_date_yr.get())
        y_err = checkdate.checkdate_y(c_yuser)

        ent_date_day.delete(0, tk.END)
        ent_date_mon.delete(0, tk.END)
        ent_date_yr.delete(0, tk.END)

        ent_date_day.insert(0, c_duser)
        ent_date_mon.insert(0, c_muser)
        ent_date_yr.insert(0, c_yuser)


        if d_err == 1:
            lbl_date_day.configure(fg="red", bg="black")
            error = 1
        else:
            lbl_date_day.configure(bg="snow", fg="black")

        if m_err == 1:
            lbl_date_mon.configure(fg="red", bg="black")
            error = 1
        else:
            lbl_date_mon.configure(bg="snow", fg="black")

        if y_err == 1:
            lbl_date_yr.configure(fg="red", bg="black")
            error = 1
        else:
            lbl_date_yr.configure(bg="snow", fg="black")

        # Проверка на получение всех данных
        if error:
            showerror(title="Проверьте данные", message="Проверьте корректность вводимых данных")
        else:
            showinfo(title="Данные", message="Контактные данные внесены")
            claim = 'tututu'


    #***********************************************************************************************************************
    #***********************************************************************************************************************
    #***********************************************************************************************************************

    #***********************************************************************************************************************
    # кнопки передачи данных далее
    frm_nextbuttons = tk.Frame(master=window)
    frm_nextbuttons.pack(fill=tk.X, ipadx=5, ipady=5)

    btn_next = tk.Button(master=frm_nextbuttons, text="Далее", bg = "snow", fg="black", command=create_claim, font=(font_type, font_size))
    btn_next.pack(side=tk.RIGHT, padx=10, ipadx=10)

    # Создает кнопку "Очистить" и размещает ее
    btn_clear = tk.Button(master=frm_nextbuttons, text="Очистить", bg = "snow", fg="black", command=clear_claim, font=(font_type, font_size))
    btn_clear.pack(side=tk.RIGHT, ipadx=10)
    #***********************************************************************************************************************
    window.mainloop()

    #Разное, что может понадобится для тестирования
    # if yerr == 0:
    #     showinfo(title="Info", message=str(c_yuser)+" в порядке")
    # else:
    #     showinfo(title="Info", message=str(c_yuser)+" не в порядке")