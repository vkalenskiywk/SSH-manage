import tkinter as tk
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
# from tkinter import ttk
# from tkinter.ttk import Checkbutton
# Userfunction
import datetime
import checkdate
import get_need_val
import find_claim_number
import create_path



def create(claim_f, link_all_cl, link_eq, link_root, fonts_name, fonts_size):
#######################################################################################################################
#                                       LOCAL FUNCTIONS                                                               #
#######################################################################################################################
    def check_claim():
        new_c_n = get_need_val.get_value(claim_num_title_num.get())
        claim_num_title_num.delete(0, tk.END)
        claim_num_title_num.insert(0, new_c_n)
        fullpath = create_path.createpath(link_all_cl, "claims_list.xlsx")
        ch_cl = find_claim_number.ch_claim(new_c_n, fullpath, c_muser, c_yuser)
        if not(ch_cl):
            showerror(title="Проверьте данные", message="Заявка с таким номером уже есть", master=cl_dscr)
        else:
            showerror(title="Проверьте данные", message="Заявкb с таким номером еще нет", master=cl_dscr)
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


#######################################################################################################################
#                                       GUI                                                                           #
#######################################################################################################################
    # Создание окна *************************************
    # cl_dscr = tk.Tk()
    cl_dscr = tk.Toplevel()
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


    # Запуск поля
    cl_dscr.mainloop()







# Разное, что может понадобится для тестирования
# claim_f = {
    #     # Основные данные
    #     'number': claim_number,
    #     'family': family,
    #     'name': name,
    #     'fathername': fathername,
    #     'iin': iin,
    #     'adresse': adresse,
    #     'region': region,
    #     # Дата подачи заявления
    #     'day': c_duser,
    #     'month': c_muser,
    #     'year': c_yuser,
    #     # Статус заявки
    #     'status': claim_status,
    #     # номер телефонов
    #     'tel_n': ph_nmb_cl,
    #     'tel_n_name': ph_nam_cl
    #        }