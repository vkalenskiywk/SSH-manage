#
#
# from tkinter import *
#
#
# def clicked():
#     import get_claims
#     claims = get_claims.get_claims()
#     r = 0
#     btn.destroy()
#     for claim in claims:
#         lbl = Label(window, text=claim, font=("Times New Roman", 14))
#         lbl.grid(column=0, row=r)
#         r += 1
#
#
# window = Tk()
# window.title("ТОО \"Строй Сервис Холдинг\"")
# # window.geometry('400x250')
# # lbl = Label(window, text="Привет", font=("Arial Bold", 50))
# # lbl.grid(column=0, row=0)
# btn = Button(window, text="Не нажимать!", command=clicked)
# btn.grid(column=1, row=0)
# window.mainloop()
#
# from tkinter import *
# from tkinter import ttk
# import re
#
#
# def is_valid(newval):
#     result = re.match("^\d{0,10}$", newval) is not None
#     if not result and len(newval) <= 12:
#         errmsg.set("Номер телефона должен быть в формате xxxxxxxxxx, где x представляет цифру")
#     else:
#         errmsg.set("")
#     return result
#
#
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
#
# check = (root.register(is_valid), "%P")
#
# errmsg = StringVar()
#
# phone_entry = ttk.Entry(validate="key", validatecommand=check)
# phone_entry.pack(padx=5, pady=5, anchor=NW)
#
# error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=250)
# error_label.pack(padx=5, pady=5, anchor=NW)
#
# root.mainloop()
#

# from tkinter import *
#
# window_screen = Tk()
# window_screen.title('Codeunderscored')
#
# theFrame = Frame(
#     window_screen,
#     width=500,
#     height=400
#     )
# theFrame.pack(expand=True, fill=BOTH)
#
# theCanvas=Canvas(
#     theFrame,
#     bg='#4A7A8C',
#     width=500,
#     height=400,
#     scrollregion=(0,0,700,700)
#     )
#
# vertibar=Scrollbar(
#     theFrame,
#     orient=VERTICAL
#     )
# vertibar.pack(side=RIGHT,fill=Y)
# vertibar.config(command=theCanvas.yview)
#
# horibar=Scrollbar(
#     theFrame,
#     orient=HORIZONTAL
#     )
# horibar.pack(side=BOTTOM,fill=X)
# horibar.config(command=theCanvas.xview)
#
# theCanvas.config(width=500,height=400)
#
# theCanvas.config(
#     xscrollcommand=horibar.set,
#     yscrollcommand=vertibar.set
#     )
# theCanvas.pack(expand=True,side=LEFT,fill=BOTH)
#
# window_screen.mainloop()


# # Import the library tkinter
# from tkinter import *
# from tkinter import messagebox
#
# # Creating an app
# app = Tk()
#
#
# # Create a function to compare the strings
# def compare_string():
#     # Taking the value in entry widget from user
#     # and storing it in variables
#     string1 = entry_widget1.get()
#     string2 = entry_widget2.get()
#
#     # Check if two strings are equal or not
#     if string1 == string2:
#         a = "Strings are same"
#     else:
#         a = "Strings are different"
#
#     # Show compared result to user when button is clicked
#     messagebox.showinfo("Compared Strings", a)
#
#
# # Create a function to concat the strings
#
#
# def concat_string():
#     # Taking the value in entry widget from user
#     # and storing it in variables
#     string1 = entry_widget1.get()
#     string2 = entry_widget2.get()
#
#     # Show concatenated result to user when button is clicked
#     messagebox.showinfo("Compared Strings",
#                         'Concatenated String: ' + string1 + string2)
#
#
# # Creating and displaying a canvas
# canvas_widget = Canvas(app, width=500,
#                        height=500)
# canvas_widget.pack()
#
# # Creating and placing the label in canvas
# label_widget1 = Label(app, text="Enter the string 1")
# canvas_widget.create_window(150, 160,
#                             window=label_widget1)
#
# # Creating and placing the label in canvas
# label_widget2 = Label(app, text="Enter the string 2")
# canvas_widget.create_window(350, 160,
#                             window=label_widget2)
#
# # Creating an input name on canvas
# # for input using widget Entry
# entry_widget1 = Entry(app)
# canvas_widget.create_window(150, 200,
#                             window=entry_widget1)
#
# # Creating another input name on canvas
# # for input using widget Entry
# entry_widget2 = Entry(app)
# canvas_widget.create_window(350, 200,
#                             window=entry_widget2)
#
# # Creating and placing the button on canvas to concat strings
# button_widget = Button(text='Concatenate the strings',
#                        command=concat_string)
# canvas_widget.create_window(150, 250, window=button_widget)
#
# # Creating and placing the button on canvas to compare strings
# button_widget = Button(text='Compare the strings',
#                        command=compare_string)
# canvas_widget.create_window(350, 250, window=button_widget)
#
# # Make the infinite loop for displaying app
# app.mainloop()





