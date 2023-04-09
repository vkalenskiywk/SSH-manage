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


#######################################################################################################################
# **********                            Main function for work                                              **********#
#######################################################################################################################



#######################################################################################################################
#                                       GUI                                                                           #
#######################################################################################################################
    claim_letter = claim_f['family'][0].upper()
    c_muser = claim_f['month']
    c_yuser = claim_f['year']
    claim_number = str(claim_f['number'])
    cl_dscr = tk.Tk()
    cl_dscr.title(claim_number)

    frm_claimcorrect = tk.Frame(master=cl_dscr, bg="snow")
    frm_claimcorrect.pack(fill=tk.X, ipadx=5, ipady=5)
    claim_num_title = tk.Label(master=frm_claimcorrect, text="Заявлению присвоен следующий номер:  ",
                        bg="snow", fg="black",
                        font=(fonts_name, fonts_size))
    claim_num_title.grid(row=0, column=0, sticky="e")
    claim_num_title_let = tk.Label(master=frm_claimcorrect, text=claim_letter, bg="snow",
                               fg="black",
                               font=(fonts_name, fonts_size))
    claim_num_title_let.grid(row=0, column=1, sticky="e")

    claim_num_title_num = tk.Entry(master=frm_claimcorrect, width=4, font=(fonts_name, fonts_size))
    claim_num_title_num.grid(row=0, column=2, sticky="e")
    claim_num_title_num.insert(0, claim_number)

    claim_num_title_dat = tk.Label(master=frm_claimcorrect, text="-"+c_muser+"-"+c_yuser, bg="snow",
                                   fg="black",
                                   font=(fonts_name, fonts_size))
    claim_num_title_dat.grid(row=0, column=3, sticky="e")

    btn_next2 = tk.Button(master=frm_claimcorrect, text="Проверить", bg="snow", fg="black",
                         font=(fonts_name, fonts_size), command=check_claim)
    btn_next2.grid(row=0, column=4, sticky="e")


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