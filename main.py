import tkinter as tk
import new_claim
def create_claim():
        new_claim.new_claim()

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

button_claim_manage = tk.Button\
    (
        text="Корректировать заявки!",
        width=25,
        height=5,
        bg="snow",
        fg="black",
        command=create_claim,
        master=frame_but,
    )


button_claim = tk.Button\
    (
        text="Создать заявку",
        width=25,
        height=5,
        bg="snow",
        fg="black",
        command=create_claim,
        master=frame_but,
    )
button_has = tk.Button\
    (
        text="ОТ и ТБ",
        width=25,
        height=5,
        bg="snow",
        fg="black",
        command=create_claim,
        master=frame_but,
    )
button_medic = tk.Button\
    (
        text="Медкомиссия",
        width=25,
        height=5,
        bg="snow",
        fg="black",
        command=create_claim,
        master=frame_but,
    )


button_claim.pack(fill=tk.BOTH, expand=True)
button_claim_manage.pack(fill=tk.BOTH, expand=True)
button_has.pack(fill=tk.BOTH, expand=True)
button_medic.pack(fill=tk.BOTH, expand=True)
main_window.mainloop()
