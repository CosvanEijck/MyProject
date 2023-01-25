import tkinter as tk
import customtkinter as ctk
from nevo_details_scripts import CSV


class MyGUI:
    def __init__(self):
        self.c = CSV()
        self.c.read_csv_file()
        self.c.filter_csv_list("Eenheid/Unit", "kcal")
        self.name_calorie_dictionary = self.c.create_dictionary(
            "Gehalte/Value", "Voedingsmiddelnaam/Dutch food name", "Engelse naam/Food name")
        self.food_names = list(self.name_calorie_dictionary.keys())
        self.appearance = ctk.set_appearance_mode("Dark")
        self.color_theme = ctk.set_default_color_theme("dark-blue")
        self.frame = None
        self.label = None
        self.entry = None
        self.listbox = None
        self.root = ctk.CTk()

    def update(self):
        self.listbox.delete(0, tk.END)
        for item in self.food_names:
            self.listbox.insert(tk.END, item)

    def fill_out(self, event=None):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.listbox.get(tk.ACTIVE))

    def check(self):
        typed = self.entry.get()
        length_of_typed = len(typed)
        if typed == '':
            self.food_names = list(self.name_calorie_dictionary.keys())
        else:
            self.food_names = []
            for item in self.food_names:
                if typed.lower() in item.lower()[0:length_of_typed]:
                    self.food_names.append(item)
        mg.update()

    def menu(self):
        self.root.title("Cocosh")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.label = ctk.CTkLabel(self.frame, text="Calorie counter", font=("Arial", 24))
        self.label.pack(pady=12, padx=10)
        self.entry = ctk.CTkEntry(self.frame, font=("Arial", 14), width=307)
        self.entry.pack()
        self.listbox = tk.Listbox(self.frame, width=50, bg="grey20")
        self.listbox.config(highlightbackground="grey30", highlightthickness=2)
        self.listbox.pack()
        mg.update()
        self.listbox.bind("<<ListboxSelect>>", self.fill_out())
        # self.entry.bind("<KeyRelease>", mg.check())
        self.root.mainloop()


if __name__ == '__main__':
    mg = MyGUI()
    mg.menu()

