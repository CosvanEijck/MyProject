import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")


class MyGUI:
    def __init__(self):
        self.appearance = ctk.set_appearance_mode("Dark")
        self.color_theme = ctk.set_default_color_theme("dark-blue")
        self.frame = None
        self.label = None
        self.entry = None
        self.root = ctk.CTk()

    def menu(self):
        self.root.title("Cocosh")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.label = ctk.CTkLabel(self.frame, text="Calorie counter", font=("Arial", 24))
        self.label.pack(pady=12, padx=10)
        self.entry = ctk.CTkEntry(self.frame, font=("Arial", 14))
        self.entry.pack()
        self.root.mainloop()


if __name__ == '__main__':
    mg = MyGUI()
    mg.menu()

