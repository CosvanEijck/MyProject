import tkinter as tk
import customtkinter as ctk
from nevo_details_scripts import CSV


def update(data):
    listbox.delete(0, tk.END)
    for item in data:
        listbox.insert(tk.END, item)


def fill_out(e):
    entry.delete(0, tk.END)
    entry.insert(0, listbox.get(tk.ANCHOR))


def check(e):
    typed = entry.get()
    length_of_typed = len(typed)
    if typed == '':
        data = []
        listbox.pack_forget()
    else:
        listbox.pack()
        data = []
        for item in food_names:
            if typed.lower() in item.lower()[0:length_of_typed]:
                data.append(item)
    update(data)


c = CSV()
c.read_csv_file()
c.filter_csv_list("Eenheid/Unit", "kcal")
name_calorie_dictionary = c.create_dictionary(
    "Gehalte/Value", "Voedingsmiddelnaam/Dutch food name", "Engelse naam/Food name")
food_names = list(name_calorie_dictionary.keys())
appearance = ctk.set_appearance_mode("Dark")
color_theme = ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Cocosh")
root.geometry("500x400")
root.resizable(False, False)
frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
frame.rowconfigure(for i in range(10), )
frame.columnconfigure(1, weight=1)
label = ctk.CTkLabel(frame, text="Calorie counter", font=("Arial", 24))
label.pack(pady=12, padx=10)
entry = ctk.CTkEntry(frame, font=("Arial", 14), width=307)
entry.pack(side="left")
add_button = ctk.CTkButton(frame, text="Add",font=("Arial", 14))
add_button.pack(pady=12, padx=10, side="left")
listbox = tk.Listbox(frame, width=50, bg="grey20")
listbox.config(highlightbackground="grey30", highlightthickness=2)
listbox.bind("<<ListboxSelect>>", fill_out)
entry.bind("<KeyRelease>", check)
root.mainloop()


