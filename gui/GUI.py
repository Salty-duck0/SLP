import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog
import CTkMenuBar as CtkMB

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x500")

def exit_app():
    if tk.messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        app.destroy()

class Menubar(CtkMB.CTkMenuBar):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    

    def create_menu_bar(self):
        self.button_1 = self.add_cascade("File")
        self.button_2 = self.add_cascade("Edit")
        self.button_3 = self.add_cascade("Settings")
        self.button_4 = self.add_cascade("About")

        self.dropdown1 = CtkMB.CustomDropdownMenu(widget=self.button_1)
        self.dropdown1.add_option(option="Open", command=lambda: print("Open"))
        self.dropdown1.add_option(option="Save")

        self.dropdown1.add_separator()

        self.sub_menu = self.dropdown1.add_submenu("Export As")
        self.sub_menu.add_option(option=".TXT")
        self.sub_menu.add_option(option=".PDF")
    

menu = Menubar(app)

menu.create_menu_bar()

app.mainloop()
