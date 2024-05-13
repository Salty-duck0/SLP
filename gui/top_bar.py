import CTkMenuBar as CtkMB
import customtkinter as ctk
from PIL import Image, ImageTk

def create_menu(app):
        
        menu = CtkMB.CTkMenuBar(app)
        button_1 = menu.add_cascade("File")
        button_2 = menu.add_cascade("Edit")
        button_3 = menu.add_cascade("Project")
        button_4 = menu.add_cascade("Utilities")
        button_5 = menu.add_cascade("View")
        button_6 = menu.add_cascade("Option")
    
        # Grid configuration for the menu
        menu.grid(row=0,column=0,sticky="nsew")
        
        dropdown1 = CtkMB.CustomDropdownMenu(widget=button_1)
        dropdown1.add_option(option="Open", command=app.open_file)
        dropdown1.add_option(option="Save", command=app.save_file)
        sub_menu = dropdown1.add_submenu("Export As")
        sub_menu.add_option(option="MP4")
        sub_menu.add_option(option="MKV")
        dropdown1.add_separator()
        dropdown1.add_option(option="Exit", command=app.exit_app)

        dropdown2 = CtkMB.CustomDropdownMenu(widget=button_2)
        dropdown2.add_option(option="Cut")
        dropdown2.add_option(option="Copy")
        dropdown2.add_option(option="Paste")

        dropdown3 = CtkMB.CustomDropdownMenu(widget=button_3)
        dropdown3.add_option(option="Settings")
        dropdown3.add_option(option="Build")

        dropdown4 = CtkMB.CustomDropdownMenu(widget=button_4)
        dropdown4.add_option(option="Terminal")
        dropdown4.add_option(option="Extensions")

        dropdown5 = CtkMB.CustomDropdownMenu(widget=button_5)
        dropdown5.add_option(option="Zoom In")
        dropdown5.add_option(option="Zoom Out")

        dropdown6 = CtkMB.CustomDropdownMenu(widget=button_6)
        dropdown6.add_option(option="Settings")


def create_icon_frame(app):
        
    icon_frame = ctk.CTkFrame(app, height=40)
    icon_frame.grid(row=1,sticky="ew", pady=5)

    icon_paths = ["Assets\icon1.png"]*10

    for index, icon_path in enumerate(icon_paths):
        icon_image = ctk.CTkImage(Image.open(icon_path), size=(24, 24))
        icon_button = ctk.CTkButton(icon_frame, image=icon_image, text="", width=40, command=app.icon_function)
        icon_button.grid(row=0, column=index, padx=5)