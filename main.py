import tkinter as tk

window = tk.Tk()

button = tk.Button\
    (
        text="Создать заявку!",
        width=25,
        height=5,
        bg="snow",
        fg="black",
    )

button.pack()
window.mainloop()