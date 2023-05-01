with open("SSH_manage.dbini", 'r') as f:
    lines = f.readlines()
for settings in lines:
    comands = settings.strip()
    if comands:
        # print(comands[0])
        # print(str(len(comands))+ " Len")
        if comands[0] == '1':
            link_root = comands[3:]

        elif comands[0] == '3':
            link_all_cl = comands[3:]
        elif comands[0] == '5':
            link_eq = comands[3:]
        elif comands[0] == '7':
            fonts_name = comands[3:]
        elif comands[0] == '9':
            fonts_size = comands[3:]


#gfdsfjshg



# print(comands)

import tkinter as tk
import claim_create
def create_claim():
        # pass
        button_claim.configure(state="disabled")
        claim_create.new_claim(fonts_name, fonts_size, link_all_cl, link_root, link_eq)
        # button_claim.configure(state='active')
        # compl = claim_create.new_claim(fonts_name, fonts_size, link_all_cl, link_root, link_eq)
        # if compl:
        #     button_claim.configure(state='active')
        # print(claim)

main_window = tk.Tk()
frame_but = tk.Frame(master=main_window, width=200, height=100, bg="snow")
frame_but.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

button_claim = tk.Button\
    (
        text="Создать заявку!",
        width=25,
        height=5,
        bg="snow",
        fg="black",
        command=create_claim,
        master=frame_but,
    )
#
# button_claim_manage = tk.Button\
#     (
#         text="Корректировать заявки!",
#         width=25,
#         height=5,
#         bg="snow",
#         fg="black",
#         command=create_claim,
#         master=frame_but,
#     )
#
# button_has = tk.Button\
#     (
#         text="ОТ и ТБ",
#         width=25,
#         height=5,
#         bg="snow",
#         fg="black",
#         command=create_claim,
#         master=frame_but,
#     )
# button_medic = tk.Button\
#     (
#         text="Медкомиссия",
#         width=25,
#         height=5,
#         bg="snow",
#         fg="black",
#         command=create_claim,
#         master=frame_but,
#     )
#
#
button_claim.pack(fill=tk.BOTH, expand=True)
# button_claim_manage.pack(fill=tk.BOTH, expand=True)
# button_has.pack(fill=tk.BOTH, expand=True)
# button_medic.pack(fill=tk.BOTH, expand=True)
# main_window.grab_set()
main_window.mainloop()
