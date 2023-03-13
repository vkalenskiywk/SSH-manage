def new_claim(cl_list = False):
    import tkinter as tk

    def clear_claim():
        ent_family_name.delete(0, tk.END)
        lbl_family_name.configure(text="Фамилия:", bg = "snow", fg="black")
        ent_first_name.delete(0, tk.END)
        ent_father_name.delete(0, tk.END)
        ent_iin.delete(0, tk.END)
        ent_address.delete(0, tk.END)
        lbl_address.configure(text="Адрес газификации:", bg="snow", fg="black")
        ent_region.delete(0, tk.END)
        lbl_region.configure(text="Регион:", bg="snow", fg="black")
        ent_cadastr.delete(0, tk.END)
        ent_phone1.delete(0, tk.END)
        lbl_phone1.configure(text="Телефон 1: +7", bg = "snow", fg="black")
        ent_phone2.delete(0, tk.END)

    def create_claim():
        error = 0
        family=ent_family_name.get()
        if len(family) == 0:
            lbl_family_name.configure(text="Введите фамилию!:", fg="red", bg = "black")
        else:
            lbl_family_name.configure(text="Фамилия:", bg="snow", fg="black")
        name=ent_first_name.get()
        fname=ent_father_name.get()
        iin=ent_iin.get()
        adresse=ent_address.get()
        if len(adresse) == 0:
            lbl_address.configure(text="Введите адрес газификации!:", fg="red", bg = "black")
        else:
            lbl_address.configure(text="Адрес газификации:", bg="snow", fg="black")
        region=ent_region.get()
        if len(region) == 0:
            lbl_region.configure(text="Введите регион!:", fg="red", bg = "black")
        else:
            lbl_region.configure(text="Регион:", bg="snow", fg="black")
        cadastr=ent_cadastr.get()
        phone1=ent_phone1.get()
        if len(phone1) == 0:
            lbl_phone1.configure(text="Введите номер телефона!: +7", fg="red", bg = "black")
        else:
            phone = [a for a in phone1 if a.isnumeric()]
            ent_phone1.delete(0,tk.END)
            phone = ''.join(phone)
            if len(phone) == 10:
                ent_phone1.insert(0,phone)
                lbl_phone1.configure(text="Телефон 1: +7", bg="snow", fg="black")
            else:
                lbl_phone1.configure(text="Введите корректный номер телефона!: +7", fg="red", bg="black")
                ent_phone1.insert(0, phone)
        phone2=ent_phone2.get()

    # Создание окна ввода данных по заявке
    window = tk.Toplevel()
    window.title("Новая заявка")
    #cjplftncz hfvrf
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3, bg = "snow", master=window)
    frm_form.pack()

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

    # Создает ярлык и текстовое поле для ввода кадастрового номера.
    lbl_cadastr = tk.Label(master=frm_form, text="Кадастровый номер:", bg = "snow", fg="black")
    ent_cadastr = tk.Entry(master=frm_form, width=50)
    lbl_cadastr.grid(row=6, column=0, sticky="e")
    ent_cadastr.grid(row=6, column=1)

    # Создает ярлык и текстовое поле для ввода телефона-1.
    lbl_phone1 = tk.Label(master=frm_form, text="Телефон 1: +7", bg = "snow", fg="black")
    ent_phone1 = tk.Entry(master=frm_form, width=50)
    lbl_phone1.grid(row=7, column=0, sticky="e")
    ent_phone1.grid(row=7, column=1)

    # Создает ярлык и текстовое поле для ввода телефона-2.
    lbl_phone2 = tk.Label(master=frm_form, text="Телефон 2: +7", bg = "snow", fg="black")
    ent_phone2 = tk.Entry(master=frm_form, width=50)
    lbl_phone2.grid(row=8, column=0, sticky="e")
    ent_phone2.grid(row=8, column=1)

    # Создает новую рамку `frm_buttons` для размещения кнопок
    frm_buttons = tk.Frame(master=window)
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # Создает кнопку "Отправить" и размещает ее
    btn_submit = tk.Button(master=frm_buttons, text="Отправить", command=create_claim, bg = "snow", fg="black")
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

    # Создает кнопку "Очистить" и размещает ее
    btn_clear = tk.Button(master=frm_buttons, text="Очистить", command=clear_claim, bg = "snow", fg="black")
    btn_clear.pack(side=tk.RIGHT, ipadx=10)

    window.mainloop()