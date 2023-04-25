import tkinter as tk
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
from tkinter import ttk
# from tkinter.ttk import Checkbutton
# Userfunction
import datetime
import checkdate
import get_need_val
import find_claim_number
import create_path

fonts_name = "Arial"
link_all_cl = 'd:/SSH/Managers/SSH/Database/'
fonts_size = '14'

claim_f = {
        # Основные данные
        'number': '1000',
        'family': 'family',
        'name': 'name',
        'fathername': 'fathername',
        'iin': '123123123123',
        'adresse': 'adresse',
        'region': 'region',
        # Дата подачи заявления
        'day': '03',
        'month': '04',
        'year': '2023',
        # Статус заявки
        'status': False,
        # номер телефонов
        'tel_n': '1231231212',
        'tel_n_name': 'ph_nam_cl'
           }


#######################################################################################################################
#                                       LOCAL FUNCTIONS                                                               #
#######################################################################################################################
def check_claim():
    new_c_n = get_need_val.get_value(claim_num_title_num.get())
    claim_num_title_num.delete(0, tk.END)
    claim_num_title_num.insert(0, new_c_n)
    fullpath = create_path.createpath(link_all_cl, "claims_list.xlsx")
    ch_cl = find_claim_number.ch_claim(new_c_n, fullpath, c_muser, c_yuser)
    if not (ch_cl):
        showerror(title="Проверьте данные", message="Заявка с таким номером уже есть", master=cl_dscr)
    else:
        showerror(title="Проверьте данные", message="Заявки с таким номером еще нет", master=cl_dscr)
        new_c_n = str(new_c_n)
        while len(new_c_n) < 4:
            new_c_n = "0" + new_c_n
            claim_num_title_num.delete(0, tk.END)
            claim_num_title_num.insert(0, new_c_n)

def select():
    result = ""
    if food.get() == 1: result = f"{result}приготовление пищи; "
    if heating.get() == 1: result = f"{result}отопление; "
    if hot_water.get() == 1: result = f"{result}горячее водоснабжение; "
    claim_goal_entr.delete(0, tk.END)
    claim_goal_entr.insert(0, result)


def add_equip():  # +lk_f*len()

    ############ Внесение новых полей ##################

    equip_n_model_lbl.append(tk.Label(master=canvas_widget, text='Марка/модель оборудования №' + str(len(equip_n_model_lbl)+1),
                                    bg="snow", font=(fonts_name, str(int(fonts_size) - 2))))
    equip_n_comm_lbl.append(tk.Label(master=canvas_widget, text='Комментарий:',
                                   bg="snow", font=(fonts_name, str(int(fonts_size) - 2))))
    equip_n_cons_lbl.append(tk.Label(master=canvas_widget, text='Расход, м^3/ч',
                                   bg="snow", font=(fonts_name, str(int(fonts_size) - 2))))
    equip_n_sum_lbl.append(tk.Label(master=canvas_widget, text='Количество',
                                  bg="snow", font=(fonts_name, str(int(fonts_size) - 2))))

    equip_com.append(ttk.Combobox(values=equipments, master=canvas_widget, font=(fonts_name, str(int(fonts_size) - 2)),
                                state="readonly"))
    equip_n_model_ent.append(tk.Entry(master=canvas_widget, font=(fonts_name, fonts_size), state="disabled"))

    equip_n_sum_ent.append(tk.Entry(master=canvas_widget, font=(fonts_name, str(int(fonts_size) - 2))))

    equip_n_cons_ent.append(tk.Entry(master=canvas_widget, font=(fonts_name, fonts_size)))

    equip_n_comm_ent.append(tk.Entry(master=canvas_widget, font=(fonts_name, fonts_size)))

    ############ Создание новых областей ввода #########

    line_cnw.append(canvas_widget.create_line((lrs, lk_f+lk_f*len(line_cnw)), (lre, lk_f+lk_f*len(line_cnw)), fill="red", width=5))
    equip_n_model_lbl_cnw.append(canvas_widget.create_window((xcoordr1, ycoords1+lk_f*len(equip_n_model_lbl_cnw)), window=equip_n_model_lbl[-1], anchor=N))
    equip_n_sum_lbl_cnw.append(canvas_widget.create_window((xcoordl2, ycoords1+lk_f*len(equip_n_sum_lbl_cnw)), window=equip_n_sum_lbl[-1], anchor=N))
    equip_n_cons_lbl_cnw.append(canvas_widget.create_window((xcoordl3, ycoords1+lk_f*len(equip_n_cons_lbl_cnw)), window=equip_n_cons_lbl[-1], anchor=N))
    equip_n_comm_lbl_cnw.append(canvas_widget.create_window((xcoordl2, ycoords3+lk_f*len(equip_n_comm_lbl_cnw)), window=equip_n_comm_lbl[-1], anchor=N))

    equip_com_cnw.append(canvas_widget.create_window((xcoordr1, ycoords2+lk_f*len(equip_com_cnw)), window=equip_com[-1], anchor=N, width=760))
    equip_n_model_ent_cnw.append(canvas_widget.create_window((xcoordr1, ycoords3+lk_f*len(equip_n_model_ent_cnw)), window=equip_n_model_ent[-1], anchor=N,
                                                           width=760))

    equip_n_sum_ent_cnw.append(canvas_widget.create_window((xcoordl2, ycoords2+lk_f*len(equip_n_sum_ent_cnw)), window=equip_n_sum_ent[-1], anchor=N,
                                                         width=60))

    equip_n_cons_ent_cnw.append(canvas_widget.create_window((xcoordl3, ycoords2+lk_f*len(equip_n_cons_ent_cnw)), window=equip_n_cons_ent[-1], anchor=N,
                                                          width=120))

    equip_n_comm_ent_cnw.append(canvas_widget.create_window((xcoordl3, ycoords3+lk_f*len(equip_n_comm_ent_cnw)), window=equip_n_comm_ent[-1], anchor=N,
                                                          width=240))

    ##################### Изменение региона прокрутки
    canvas_widget.configure(scrollregion=canvas_widget.bbox("all"))#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def remove_equip():
    if len(equip_com) > 1:
        ########### Удаление крайних полей полей    ####################

        canvas_widget.delete(equip_n_model_lbl_cnw[-1])
        canvas_widget.delete(equip_n_comm_lbl_cnw[-1])
        canvas_widget.delete(equip_n_cons_lbl_cnw[-1])
        canvas_widget.delete(equip_n_sum_lbl_cnw[-1])
        canvas_widget.delete(equip_com_cnw[-1])
        canvas_widget.delete(equip_n_model_ent_cnw[-1])
        canvas_widget.delete(equip_n_sum_ent_cnw[-1])
        canvas_widget.delete(equip_n_cons_ent_cnw[-1])
        canvas_widget.delete(equip_n_comm_ent_cnw[-1])
        canvas_widget.delete(line_cnw[-1])
        ########### Удаление крайних областей ввода ####################

        equip_n_model_lbl[-1].destroy()
        equip_n_comm_lbl[-1].destroy()
        equip_n_cons_lbl[-1].destroy()
        equip_n_sum_lbl[-1].destroy()
        equip_com[-1].destroy()
        equip_n_model_ent[-1].destroy()
        equip_n_sum_ent[-1].destroy()
        equip_n_cons_ent[-1].destroy()
        equip_n_comm_ent[-1].destroy()

        ########### Удаление из массива              ####################

        equip_com.pop(-1)
        equip_n_model_ent.pop(-1)
        equip_n_comm_ent.pop(-1)
        equip_n_cons_ent.pop(-1)
        equip_n_sum_ent.pop(-1)
        equip_n_model_lbl.pop(-1)
        equip_n_comm_lbl.pop(-1)
        equip_n_cons_lbl.pop(-1)
        equip_n_sum_lbl.pop(-1)

        equip_com_cnw.pop(-1)
        equip_n_model_ent_cnw.pop(-1)
        equip_n_comm_ent_cnw.pop(-1)
        equip_n_cons_ent_cnw.pop(-1)
        equip_n_sum_ent_cnw.pop(-1)
        equip_n_model_lbl_cnw.pop(-1)
        equip_n_comm_lbl_cnw.pop(-1)
        equip_n_cons_lbl_cnw.pop(-1)
        equip_n_sum_lbl_cnw.pop(-1)
        line_cnw.pop(-1)

        ##################### Изменение региона прокрутки
        canvas_widget.configure(scrollregion=canvas_widget.bbox("all"))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    else:
        pass


#######################################################################################################################
# **********                            Main function for work                                              **********#
#######################################################################################################################



#######################################################################################################################
#                                       Получение основных переменных для номера заявки                               #
#######################################################################################################################

claim_letter = claim_f['family'][0].upper()
c_muser = claim_f['month']
c_yuser = claim_f['year']
claim_number = str(claim_f['number'])

length_font, hight_font = get_need_val.GetTextDimensions('0', int(fonts_size)-2, fonts_name)

#######################################################################################################################
#                                       GUI                                                                           #
#######################################################################################################################

# Создание окна *************************************
cl_dscr = tk.Tk()
# cl_dscr = tk.Toplevel()
cl_dscr.title(claim_number)

##################################### Корректировка заявки ############################################################
# Создание рамки для корректировке номера заявки *************************************
frm_claimcorrect = tk.Frame(master=cl_dscr, bg="snow")
frm_claimcorrect.pack(fill=tk.X, ipadx=5, ipady=5)
# Область описания *************************************
claim_num_title = tk.Label(master=frm_claimcorrect, text="Заявлению присвоен следующий номер:  ",
                    bg="snow", fg="black",
                    font=(fonts_name, fonts_size))
claim_num_title.grid(row=0, column=0, sticky="e")
# Область буквы в номере заявки *************************************
claim_num_title_let = tk.Label(master=frm_claimcorrect, text=claim_letter, bg="snow",
                           fg="black",
                           font=(fonts_name, fonts_size))
claim_num_title_let.grid(row=0, column=1, sticky="e")
# Область корректировки номера *************************************
claim_num_title_num = tk.Entry(master=frm_claimcorrect, width=4, font=(fonts_name, fonts_size))
claim_num_title_num.grid(row=0, column=2, sticky="e")
claim_num_title_num.insert(0, claim_number)
# Область даты заявки *************************************
claim_num_title_dat = tk.Label(master=frm_claimcorrect, text="-"+c_muser+"-"+c_yuser, bg="snow",
                               fg="black",
                               font=(fonts_name, fonts_size))
claim_num_title_dat.grid(row=0, column=3, sticky="e")
# Кнопки "ПРОВЕРИТЬ" *************************************
btn_next2 = tk.Button(master=frm_claimcorrect, text="Проверить", bg="snow", fg="black",
                     font=(fonts_name, fonts_size), command=check_claim)
btn_next2.grid(row=0, column=4, sticky="e")
##################################### Ввод объекта ####################################################################
# Создание рамки
frm_claim_obj = tk.Frame(master=cl_dscr, bg="snow")
frm_claim_obj.pack(fill=tk.X, ipadx=5, ipady=5)
claim_object_label = tk.Label(master=frm_claim_obj, text="Выдача технических условий на:",
                    bg="snow", fg="black",
                    font=(fonts_name, fonts_size))
claim_object_label.grid(row=0, column=0, sticky="e")
claim_object_entr = tk.Entry(master=frm_claim_obj, width=30, font=(fonts_name, fonts_size))
claim_object_entr.grid(row=0, column=1, sticky="e")

claim_cadastr_label = tk.Label(master=frm_claim_obj, text="Кадастровый номер участка:",
                    bg="snow", fg="black",
                    font=(fonts_name, fonts_size))
claim_cadastr_label.grid(row=1, column=0, sticky="e")
claim_cadastr_entr = tk.Entry(master=frm_claim_obj, width=30, font=(fonts_name, fonts_size))
claim_cadastr_entr.grid(row=1, column=1, sticky="e")

claim_area_label = tk.Label(master=frm_claim_obj, text="площадь, м^2:",
                    bg="snow", fg="black",
                    font=(fonts_name, fonts_size))
claim_area_label.grid(row=2, column=0, sticky="e")
claim_area_entr = tk.Entry(master=frm_claim_obj, width=30, font=(fonts_name, fonts_size))
claim_area_entr.grid(row=2, column=1, sticky="e")

##################################### Ввод целей   ####################################################################

frm_claim_goal = tk.Frame(master=cl_dscr, bg="snow")
frm_claim_goal.pack(fill=tk.X, ipadx=5, ipady=5)
claim_goal_label = tk.Label(master=frm_claim_goal, text="необходим в целях:",
                    bg="snow", fg="black",
                    font=(fonts_name, fonts_size), anchor="nw", justify="left")
claim_goal_entr = tk.Entry(master=frm_claim_goal, font=(fonts_name, fonts_size))
claim_goal_label.pack(fill=BOTH, expand=True)
claim_goal_entr.pack(fill=BOTH, expand=True)

food = IntVar()
food_checkbutton = Checkbutton(master=frm_claim_goal, text="приготовление пищи", variable=food,
                               font=(fonts_name, str(int(fonts_size)-2)), bg="snow", command=select)
heating = IntVar()
heating_checkbutton = Checkbutton(master=frm_claim_goal, text="отопление", variable=heating,
                                  font=(fonts_name, str(int(fonts_size)-2)), bg="snow", command=select)
hot_water = IntVar()
hot_water_checkbutton = Checkbutton(master=frm_claim_goal, text="горячее водоснабжение", variable=hot_water,
                                    font=(fonts_name, str(int(fonts_size)-2)), bg="snow", command=select)
food_checkbutton.pack(anchor=NW)
heating_checkbutton.pack(anchor=NW)
hot_water_checkbutton.pack(anchor=NW)

##################################### Ввод оборудования ###############################################################

frm_claim_equip = tk.Frame(master=cl_dscr, bg="snow")
frm_claim_equip.pack(fill=tk.X, pady=5)

#Для примера. Потом оборудование будет браться из БД
# equipments = ['', 'иное', 'navien', 'viessman sdfhgdhgbnhjhtgvcdvfbdgsfdvbgsafdvfbsgrafsd', 'ПГ-2', 'ПГ-3', 'ПГ-4']
equipments = ['ввести вручную', 'navien', 'viessman', 'ПГ-2', 'ПГ-3', 'ПГ-4']

#Определение ширины виджета выбора оборудования
leng = 1
for i in equipments:
    if len(i) > leng:
        leng = len(i)
if leng < 10:
    leng = 10
elif leng > 30:
    leng = 30

#Создание массивов для виджетов ввода оборудования
equip_com = ['']
# equip_sum = ['']
equip_n_model_ent = ['']
equip_n_comm_ent = ['']
equip_n_cons_ent = ['']
equip_n_sum_ent = ['']

equip_n_model_lbl = ['']
equip_n_comm_lbl = ['']
equip_n_cons_lbl = ['']
equip_n_sum_lbl = ['']


equip_com_cnw = ['']
equip_sum_cnw = ['']
equip_n_model_ent_cnw = ['']
equip_n_comm_ent_cnw = ['']
equip_n_cons_ent_cnw = ['']
equip_n_sum_ent_cnw = ['']
equip_n_model_lbl_cnw = ['']
equip_n_comm_lbl_cnw = ['']
equip_n_cons_lbl_cnw = ['']
equip_n_sum_lbl_cnw = ['']
line_cnw = ['']

# Кнопка создания дополнительного поля по оборудованию
add_equip_butt = tk.Button(master=frm_claim_equip, font=(fonts_name, str(int(fonts_size)-2)),
                           text="Добавить оборудование", command=add_equip)
rem_equip_butt = tk.Button(master=frm_claim_equip, font=(fonts_name, str(int(fonts_size)-2)),
                           text="Убрать оборудование", command=remove_equip)
add_equip_butt.grid(column=0, row=0, columnspan=2)
rem_equip_butt.grid(column=2, row=0, columnspan=2)

#Область ввода оборудования

frame_eq = tk.LabelFrame(master=cl_dscr, bg="snow")#, width=1100, height=500)
frame_eq.pack(side=LEFT)
canvas_widget = Canvas(master=frame_eq, width=1300, height=300, bg="snow")

canvas_widget.pack(side=LEFT)

# equip_sum[0] = tk.Entry(master=cl_dscr, width=3, font=(fonts_name, str(int(fonts_size)-2)))

# Описание полей
equip_n_model_lbl[0] = tk.Label(master=canvas_widget, text = 'Марка/модель оборудования №'+ str(len(equip_com)),
                              bg="snow", font=(fonts_name, str(int(fonts_size)-2)))
equip_n_comm_lbl[0] = tk.Label(master=canvas_widget, text = 'Комментарий:',
                              bg="snow", font=(fonts_name, str(int(fonts_size)-2)))
equip_n_cons_lbl[0] = tk.Label(master=canvas_widget, text = 'Расход, м^3/ч',
                              bg="snow", font=(fonts_name, str(int(fonts_size)-2)))
equip_n_sum_lbl[0] = tk.Label(master=canvas_widget, text = 'Количество',
                              bg="snow", font=(fonts_name, str(int(fonts_size)-2)))

lrs = 0                     # Начальная позиция горизонтальной линии
lre = 1300                  # Конечная позиция горизонтальной линии
lk = 0                      # Отступ горизонтальной линии
lk_f = 40+7*hight_font      # Отступ финишной горизонтальной линии


xcoordr1 = 390
xcoordl2 = 780+130
xcoordl3 = 780+130+260
ycoords1 = 10
ycoords2 = 20+2*hight_font
ycoords3 = 40+4*hight_font

line = canvas_widget.create_line((lrs, lk), (lre, lk), fill="red", width=5)
line_cnw[0] = canvas_widget.create_line((lrs, lk_f), (lre, lk_f), fill="red", width=5)
equip_n_model_lbl_cnw[0] = canvas_widget.create_window((xcoordr1, ycoords1), window=equip_n_model_lbl, anchor=N)
equip_n_sum_lbl_cnw[0] = canvas_widget.create_window((xcoordl2, ycoords1), window=equip_n_sum_lbl, anchor=N)
equip_n_cons_lbl_cnw[0] = canvas_widget.create_window((xcoordl3, ycoords1), window=equip_n_cons_lbl, anchor=N)
equip_n_comm_lbl_cnw[0] = canvas_widget.create_window((xcoordl2, ycoords3), window=equip_n_comm_lbl, anchor=N)



# Выбор/ввод оборудования

equip_com[0] = ttk.Combobox(values=equipments, master=canvas_widget, font=(fonts_name, str(int(fonts_size) - 2)),
                                state="readonly")
equip_com_cnw[0] = canvas_widget.create_window((xcoordr1, ycoords2), window=equip_com[0], anchor=N, width=760)

equip_n_model_ent[0] = tk.Entry(master=canvas_widget, font=(fonts_name, fonts_size), state="disabled")
equip_n_model_ent_cnw[0] = canvas_widget.create_window((xcoordr1, ycoords3), window=equip_n_model_ent[0], anchor=N, width=760)

# Количество оборудования

equip_n_sum_ent[0] = tk.Entry(master=canvas_widget, font=(fonts_name, str(int(fonts_size) - 2)))
equip_n_sum_ent_cnw[0] = canvas_widget.create_window((xcoordl2, ycoords2), window=equip_n_sum_ent[0], anchor=N, width=60)

# Расход

equip_n_cons_ent[0] = tk.Entry(master=canvas_widget, font=(fonts_name, fonts_size))
equip_n_cons_ent_cnw[0] = canvas_widget.create_window((xcoordl3, ycoords2), window=equip_n_cons_ent[0], anchor=N, width=120)

# Ввод комментария (при необходимости)

equip_n_comm_ent[0] = tk.Entry(master=canvas_widget, font=(fonts_name, fonts_size))
equip_n_comm_ent_cnw[0] = canvas_widget.create_window((xcoordl3, ycoords3), window=equip_n_comm_ent[0], anchor=N, width=240)


# Установка скролла вертикального
sb_ver = Scrollbar(master=frame_eq, orient=VERTICAL, command=canvas_widget.yview)
sb_ver.pack(side=RIGHT, fill=Y)

canvas_widget.configure(yscrollcommand=sb_ver.set)
canvas_widget.configure(scrollregion=canvas_widget.bbox("all"))


cl_dscr.mainloop()

#######################################################################################################################
######################################  Для тестов  ###################################################################

# canvas_widget.bind('<Configure>', lambda e: canvas_widget.configure(scrollregion=canvas_widget.bbox('all')))

# eq_insert_fr = Frame(master=canvas_widget)
# canvas_widget.create_window((0, 0), window=eq_insert_fr, anchor='nw')

# for i in range(2):
#     # equip_sum[0] = tk.Entry(master=cl_dscr, width=3, font=(fonts_name, str(int(fonts_size)-2)))
#     l = (i+1)*3
#     q = ""
#     for j in range(l):
#         q=q+"0"
#     visa, lengha = get_need_val.GetTextDimensions(q, int(fonts_size)-2, fonts_name)
#     equip_sum.append(tk.Entry(master=canvas_widget, width=l, font=(fonts_name, str(int(fonts_size)-2))))
#     equip_sum[i+1].insert(0, q)
#     x = lengha/2
#     y = visa/2
#     equip_sum[i + 1].insert(0, str(lengha)+"^"+str(visa))
#     # equip_sum[i + 1].grid(row = i, column = 0, sticky=W)
#     canvas_widget.create_window(x, (i+1)*visa, window=equip_sum[i+1], anchor=NW)


# equip_com[0] = ttk.Combobox(values=equipments, master=eq_insert_fr, font=(fonts_name, str(int(fonts_size) - 2)),
#                                 state="readonly", width=leng)
# equip_com[0].grid(column=0, row=0, columnspan=3)
#
# equip_sum[0] = tk.Entry(master=eq_insert_fr, width=3, font=(fonts_name, str(int(fonts_size)-2)))
#
# equip_n_model_ent[0] = tk.Entry(master=eq_insert_fr, font=(fonts_name, fonts_size), state="disabled")
#
# equip_n_cons_ent[0] = tk.Entry(master=eq_insert_fr, font=(fonts_name, fonts_size), state="disabled")
#
# equip_n_model_ent[0].grid(column=0, row=3, padx=5)
# equip_n_type_ent[0].grid(column=1, row=3, padx=5)
# equip_n_cons_ent[0].grid(column=2, row=3, padx=5)
# equip_n_sum_ent[0].grid(column=3, row=3, padx=5)


#######################################################

# for i in range(2):
#     # equip_sum[0] = tk.Entry(master=cl_dscr, width=3, font=(fonts_name, str(int(fonts_size)-2)))
#     l = (i + 1) * 3
#     q = ""
#     for j in range(l):
#         q = q + "0"
#     visa, lengha = get_need_val.GetTextDimensions(q, int(fonts_size) - 2, fonts_name)
#     equip_sum.append(tk.Entry(master=canvas_widget, width=l, font=(fonts_name, str(int(fonts_size) - 2))))
#     equip_sum[-1].insert(0, q)
#     x = lengha / 2
#     y = visa / 2
#     equip_sum[-1].insert(0, str(lengha) + "^" + str(visa))
#     # equip_sum[i + 1].grid(row = i, column = 0, sticky=W)
#     canvas_widget.create_window(x, (i + 1) * visa * 10, window=equip_sum[-1], anchor=NW)


# equip_com.append(ttk.Combobox(values=equipments, master=eq_insert_fr, font=(fonts_name, str(int(fonts_size) - 2)),
#                             state="readonly", width=leng))
# equip_com[-1].grid(column=0, row=(1+(len(equip_com)-1)*3), columnspan=3)
# equip_sum.append(tk.Entry(master=eq_insert_fr, width=3, font=(fonts_name, str(int(fonts_size) - 2))))
# equip_sum[-1].grid(column=3, row=(1+(len(equip_sum)-1)*3), pady=5)
#
# equip_n_model_lbl.append(tk.Label(master=eq_insert_fr, text='Модель оборудования',
#                                 bg="snow", font=(fonts_name, str(int(fonts_size) - 2))))
# equip_n_comm_lbl.append(tk.Label(master=eq_insert_fr, text='Тип оборудования',
#                                bg="snow", font=(fonts_name, str(int(fonts_size) - 2))))
# equip_n_cons_lbl.append(tk.Label(master=eq_insert_fr, text='Расход, м^3/ч',
#                                bg="snow", font=(fonts_name, str(int(fonts_size) - 2))))
# equip_n_sum_lbl.append(tk.Label(master=eq_insert_fr, text='Количество',
#                               bg="snow", font=(fonts_name, str(int(fonts_size) - 2))))
# equip_n_model_lbl[-1].grid(column=0, row=(2+(len(equip_n_model_lbl)-1)*3), padx=5)
# equip_n_comm_lbl[-1].grid(column=1, row=(2+(len(equip_n_comm_lbl)-1)*3), padx=5)
# equip_n_cons_lbl[-1].grid(column=2, row=(2+(len(equip_n_cons_lbl)-1)*3), padx=5)
# equip_n_sum_lbl[-1].grid(column=3, row=(2+(len(equip_n_sum_lbl)-1)*3), padx=5)
# equip_n_model_ent.append(tk.Entry(master=eq_insert_fr, font=(fonts_name, fonts_size), state="disabled"))
# equip_n_type_ent.append(tk.Entry(master=eq_insert_fr, font=(fonts_name, fonts_size), state="disabled"))
# equip_n_cons_ent.append(tk.Entry(master=eq_insert_fr, font=(fonts_name, fonts_size), state="disabled"))
# equip_n_sum_ent.append(tk.Entry(master=eq_insert_fr, font=(fonts_name, fonts_size), state="disabled"))
# equip_n_model_ent[-1].grid(column=0, row=(3+(len(equip_n_model_ent)-1)*3), padx=5)
# equip_n_type_ent[-1].grid(column=1, row=(3+(len(equip_n_type_ent)-1)*3), padx=5)
# equip_n_cons_ent[-1].grid(column=2, row=(3+(len(equip_n_cons_ent)-1)*3), padx=5)
# equip_n_sum_ent[-1].grid(column=3, row=(3+(len(equip_n_sum_ent)-1)*3), padx=5)