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
    for item in food_names:
        if str(entry.get()).lower() == item.lower():
            listbox.grid_forget()


def check(e):
    typed = entry.get()
    length_of_typed = len(typed)
    if typed == '':
        data = []
        listbox.grid_forget()
    else:
        listbox.grid(column=0, row=2, sticky=tk.N, pady=5, padx=5)
        listbox.lift()
        data = []
        for item in food_names:
            if typed.lower() in item.lower()[0:length_of_typed]:
                data.append(item)
            elif typed.lower() == item.lower:
                listbox.grid_forget()
    update(data)


def add_to_table():
    typed = entry.get()
    listbox2 = tk.Listbox(root, height=1, width=50, bg="grey20")
    listbox2.config(highlightbackground="grey30", highlightthickness=2)
    listbox2.pack(padx=60, fill="both")
    listbox2.insert(tk.END, '   {}:    {} kcal'.format(typed, name_calorie_dictionary[typed]))


c = CSV()
c.read_csv_file()
c.filter_csv_list("Eenheid/Unit", "kcal")
name_calorie_dictionary = c.create_dictionary(
    "Gehalte/Value", "Engelse naam/Food name")
food_names = list(name_calorie_dictionary.keys())
appearance = ctk.set_appearance_mode("Dark")
color_theme = ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Cocosh")
root.geometry("500x400")
root.resizable(False, False)
frame = ctk.CTkFrame(root)
frame.pack(pady=10, padx=60, fill="both")
frame2 = ctk.CTkFrame(root)
frame2.pack(pady=10, padx=60, fill="both", expand=True)
frame2.columnconfigure(0, weight=4)
frame2.columnconfigure(1, weight=1)
label = ctk.CTkLabel(frame, text="Calorie counter", font=("Arial", 24))
label.pack(pady=5)
entry = ctk.CTkEntry(frame2, font=("Arial", 14), width=307)
entry.grid(column=0, row=1, sticky=tk.NW, pady=5, padx=5)
add_button = ctk.CTkButton(frame2, text="Add", font=("Arial", 14), command=add_to_table)
add_button.grid(column=1, row=1, sticky=tk.NE, pady=5, padx=5)
listbox = tk.Listbox(frame2, width=50, bg="grey20")
listbox.config(highlightbackground="grey30", highlightthickness=2)
listbox.bind("<<ListboxSelect>>", fill_out)
entry.bind("<KeyRelease>", check)
root.mainloop()


