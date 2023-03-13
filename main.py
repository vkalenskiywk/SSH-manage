import tkinter as tk
import new_claim
def create_claim():
        new_claim.new_claim()

main_window = tk.Tk()

button = tk.Button\
    (
        text="Создать заявку!",
        width=25,
        height=5,
        bg="snow",
        fg="black",
        command=create_claim,
    )

button.pack()
main_window.mainloop()