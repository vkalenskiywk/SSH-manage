import os
import openpyxl
import tkinter as tk

def find_claim_number(link_all_cl, c_muser, c_yuser):
    claim_n = []
    claim_number = -1
    link_all_cl = link_all_cl.replace("\\", "/") #корректировка пути


    if link_all_cl[-1] != "/": #Установка слеша перед именем файла
        link_all_cl = link_all_cl+"/"
    fullpath = link_all_cl+"claims_list.dbSSH"

    # main_window2 = tk.Tk()
    # frame_but = tk.Frame(master=main_window2, bg="snow")
    # frame_but.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    # lbl_region = tk.Label(master=main_window2, text=link_all_cl, bg="snow", fg="black")  #
    # lbl_region.pack()
    # main_window2.mainloop()

    if (os.path.exists(fullpath) == True):
        wb = openpyxl.load_workbook(fullpath)
        sheet = wb['claims_list']
        rows = sheet.max_row
        for i in range(2, rows+1):
            if (str(sheet.cell(row = i, column = 4).value) ==  c_muser) & (str(sheet.cell(row = i, column = 5).value) ==  c_yuser):
                claim_n.append(int(sheet.cell(row = i, column = 4).value))
        if len(claim_n) > 0:
            claim_n.sort()
            for j in range(1, claim_n):
                if claim_n[j]-claim_n[j-1] > 1:
                    claim_number = claim_n[j-1]+1
                    break
            if claim_number == -1:
                claim_number = claim_n[-1]+1
        else:
            claim_number = 1
    else:
        wb = openpyxl.Workbook()
        wb.create_sheet(title='claims_list', index=0)
        sheet = wb['claims_list'] #№	claim_letter	number_in_data	month	year	claim	claim_location
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