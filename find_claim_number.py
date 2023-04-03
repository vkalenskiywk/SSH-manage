import os
import openpyxl
import tkinter as tk

def find_claim_number(link_all_cl, c_muser, c_yuser):
    claim_n = []
    claim_number = -1
    link_all_cl = link_all_cl.replace("\\", "/") #корректировка пути

    if link_all_cl[-1] != "/": #Установка слеша перед именем файла
        link_all_cl = link_all_cl+"/"
    #fullpath = link_all_cl+"claims_list.dbSSH" #Придумать решение для открытия файла с другим расширением. или защиту excel файла.
    fullpath = link_all_cl + "claims_list.xlsx"

    if (os.path.exists(fullpath) == True): #Если уже есть файл с внесенными данными
        # Требуется исправить несовместимость строчного типа для месяца и года и числового при определении очередности
        wb = openpyxl.load_workbook(fullpath)
        sheet = wb['claims_list']
        rows = sheet.max_row
        for i in range(2, rows+1):
            if (str(sheet.cell(row = i, column = 4).value) ==  c_muser) & (str(sheet.cell(row = i, column = 5).value) ==  c_yuser):
                claim_n.append(int(sheet.cell(row = i, column = 3).value))
        if len(claim_n) > 0: #Присвоение номеру заявки №1, если он свободен
            claim_n.sort()
            if claim_n[0] > 1:
                claim_number = 1
            else:
                for j in range(1, len(claim_n)): # Определение первого свободного номера
                    if claim_n[j]-claim_n[j-1] > 1:
                        claim_number = claim_n[j-1]+1
                        break
            if claim_number == -1:
                claim_number = claim_n[-1]+1
        else:
            claim_number = 1
    else:                                           #Если это самая первая заявка, вносимая в базу данных
        if not os.path.isdir(link_all_cl):          #Проверка, есть ли такой путь, и если нет, то его создание
            os.makedirs(link_all_cl)

        wb = openpyxl.Workbook()                    #Если это самая первая заявка, вносимая в базу данных
        wb.create_sheet(title='claims_list', index=0)
        sheet = wb['claims_list']                   # шапка таблицы №	claim_letter	number_in_data	month	year	claim	claim_location
        sheet.cell(row=1, column=1).value = "№"
        sheet.cell(row=1, column=2).value = "claim_letter"
        sheet.cell(row=1, column=3).value = "number_in_data"
        sheet.cell(row=1, column=4).value = "month"
        sheet.cell(row=1, column=5).value = "year"
        sheet.cell(row=1, column=6).value = "claim"
        sheet.cell(row=1, column=7).value = "claim_location"
        wb.save(fullpath)
        claim_number = 1

    claim_number = str(claim_number)
    while len(claim_number) <4:
        claim_number = "0"+claim_number
    return claim_number


    # main_window2 = tk.Tk()
    # frame_but = tk.Frame(master=main_window2, bg="snow")
    # frame_but.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    # lbl_region = tk.Label(master=main_window2, text=os.path.exists(fullpath), bg="snow", fg="black")  #
    # lbl_region.pack()
    # main_window2.mainloop()