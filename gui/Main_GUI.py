import tkinter as tk
from tkinter import ttk
import cv2
import time
from tkinter import filedialog
from datetime import timedelta
import customtkinter as ctk
from PIL import Image, ImageTk
import CTkMenuBar as CtkMB

def dummy_function(choice):
    print("Option selected:", choice)

def icon_function():
    print("Icon clicked")
    
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Media Files", "*.mp4 *.avi")])
    if file_path:
        media_player_app.open_video(file_path)

def save_file():
    if media_player_app.current_file:
        files = [('All Files', '*.*'), ('MP4 Files', '*.mp4'), ('AVI Files', '*.avi')]
        save_path = filedialog.asksaveasfilename(filetypes=files, defaultextension=files)
        if save_path:
            # Implement video saving logic here
            print(f"Saving video to: {save_path}")

def exit_app():
    if tk.messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        app.destroy()

def show_filters_options():
    filter_options_frame.pack(pady=10)
    adjust_options_frame.pack_forget()

def show_adjust_options():
    adjust_options_frame.pack(pady=10)  
    filter_options_frame.pack_forget()

app = ctk.CTk()
app.geometry("800x500")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MediaPlayerApp(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.video_capture = None
        self.current_file = None
        self.playing_video = False
        self.video_paused = False
        self.create_widgets()

    def create_widgets(self):
        self.media_canvas = tk.Canvas(self, width=800, height=400, background='black', highlightbackground="gray75")
        self.media_canvas.pack(pady=10, fill=tk.BOTH, expand=True)
        # Original FPS label
        self.original_fps_label = ctk.CTkLabel(self, text="Original FPS: ", font=("Arial", 12, "bold"))
        self.original_fps_label.pack(pady=5)

        # Current FPS label
        self.current_fps_label = ctk.CTkLabel(self, text="Current FPS: ", font=("Arial", 12, "bold"))
        self.current_fps_label.pack(pady=5)

        # CTkSlider
        self.progress_slider = ctk.CTkSlider(
            self,
            from_=0,
            to=100,
            command=self.seek_video
        )
        self.progress_slider.set(0)
        self.progress_slider.pack(fill="x", padx=10, pady=5)

        self.select_file_button = ctk.CTkButton(
            self,
            text="Select File",
            font=("Arial", 12, "bold"),
            command=self.select_file,
            corner_radius=5
        )
        self.select_file_button.pack(pady=5)
        self.control_buttons_frame = ctk.CTkFrame(self)
        self.control_buttons_frame.pack(pady=5)
        self.play_button = ctk.CTkButton(
            self.control_buttons_frame,
            text="Play",
            font=("Arial", 12, "bold"),
            command=self.play_video,
            corner_radius=5
        )
        self.play_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.pause_button = ctk.CTkButton(
            self.control_buttons_frame,
            text="Pause",
            font=("Arial", 12, "bold"),
            command=self.pause_video,
            corner_radius=5
        )
        self.pause_button.pack(side=tk.LEFT, padx=10, pady=5)
        self.stop_button = ctk.CTkButton(
            self.control_buttons_frame,
            text="Stop",
            font=("Arial", 12, "bold"),
            command=self.stop,
            corner_radius=5
        )
        self.stop_button.pack(side=tk.LEFT, pady=5)
        self.fast_forward_button = ctk.CTkButton(
            self.control_buttons_frame,
            text="Fast Forward",
            font=("Arial", 12, "bold"),
            command=self.fast_forward,
            corner_radius=5
        )
        self.fast_forward_button.pack(side=tk.LEFT, padx=10, pady=5)
        self.rewind_button = ctk.CTkButton(
            self.control_buttons_frame,
            text="Rewind",
            font=("Arial", 12, "bold"),
            command=self.rewind,
            corner_radius=5
        )
        self.rewind_button.pack(side=tk.LEFT, pady=5)

        # Time label
        self.time_label = ctk.CTkLabel(self, text="", font=("Arial", 12, "bold"))
        self.time_label.pack(pady=5)

    def select_file(self):
        self.playing_video = False
        file_path = filedialog.askopenfilename(
            filetypes=[("Media Files", "*.mp4 *.avi")]
        )
        if file_path:
            self.current_file = file_path
            self.play_video()

    def play_video(self):
        if not self.playing_video:
            self.video_capture = cv2.VideoCapture(self.current_file)
            self.original_fps = self.video_capture.get(cv2.CAP_PROP_FPS)
            self.original_fps_label.configure(text=f"Original FPS: {self.original_fps:.2f}")
            self.video_duration = self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT) / self.original_fps
            self.progress_slider.configure(to=self.video_duration)
            self.playing_video = True
            self.update_video_progress()

    def update_video_progress(self):
        if self.playing_video and not self.video_paused:
            start_time = time.time()
            ret, frame = self.video_capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_image = ImageTk.PhotoImage(Image.fromarray(frame))
                self.media_canvas.create_image(0, 0, anchor=tk.NW, image=frame_image)
                self.media_canvas.image = frame_image

                current_time = self.video_capture.get(cv2.CAP_PROP_POS_MSEC) / 1000
                self.progress_slider.set(current_time)
                current_time_str = str(timedelta(seconds=current_time))[:-3]
                total_duration_str = str(timedelta(seconds=self.video_duration))[:-3]
                self.time_label.configure(text=f"{current_time_str}/{total_duration_str}")

            end_time = time.time()
            elapsed_time = end_time - start_time
            current_fps = 1 / elapsed_time
            self.current_fps_label.configure(text=f"Current FPS: {current_fps:.2f}")

        if self.playing_video and not self.video_paused:
            self.after(1, self.update_video_progress)



    def seek_video(self, value):
        if self.playing_video:
            seek_time = float(value)
            self.video_capture.set(cv2.CAP_PROP_POS_MSEC, seek_time * 1000)

    def fast_forward(self):
        if self.playing_video:
            current_frame = self.video_capture.get(cv2.CAP_PROP_POS_FRAMES)
            self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, current_frame + 100)

    def rewind(self):
        if self.playing_video:
            current_frame = self.video_capture.get(cv2.CAP_PROP_POS_FRAMES)
            self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, max(0, current_frame - 100))

    def pause_video(self):
        if self.playing_video:
            if self.video_paused:
                self.video_paused = False
                self.pause_button.configure(text="Pause")
                self.update_video_progress()
            else:
                self.video_paused = True
                self.pause_button.configure(text="Resume")


    def stop(self):
        if self.playing_video:
            self.video_capture.release()
            self.playing_video = False
            self.media_canvas.delete("all")


menu = CtkMB.CTkMenuBar(app)
button_1 = menu.add_cascade("File")
button_2 = menu.add_cascade("Edit")
button_3 = menu.add_cascade("Project")
button_4 = menu.add_cascade("Utilities")
button_5 = menu.add_cascade("View")
button_6 = menu.add_cascade("Option")

dropdown1 = CtkMB.CustomDropdownMenu(widget=button_1)
dropdown1.add_option(option="Open", command=open_file)
dropdown1.add_option(option="Save", command=save_file)
sub_menu = dropdown1.add_submenu("Export As")
sub_menu.add_option(option="MP4")
sub_menu.add_option(option="MKV")
dropdown1.add_separator()
dropdown1.add_option(option="Exit", command=exit_app)

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
dropdown6.add_option(option="Prefernces")

# Create a horizontal frame for the icons
icon_frame = ctk.CTkFrame(app, height=40)
icon_frame.pack(side="top", fill="x", pady=(5, 0))

# Load the SVG icons
icon_paths = ["gui\Assets\icon1.png","gui\Assets\icon1.png","gui\Assets\icon1.png","gui\Assets\icon1.png","gui\Assets\icon1.png","gui\Assets\icon1.png","gui\Assets\icon1.png","gui\Assets\icon1.png","gui\Assets\icon1.png","gui\Assets\icon1.png"]

for icon_path in icon_paths:
    # Load the SVG image
    icon_image = ctk.CTkImage(Image.open(icon_path), size=(24, 24))
    
    # Create a button with the SVG image
    icon_button = ctk.CTkButton(icon_frame, image=icon_image, text="", width=40, command=icon_function)
    icon_button.pack(side="left", padx=5)

# Create a frame for the columns
column_frame = ctk.CTkFrame(app)
column_frame.pack(side="top", fill="both", expand=True, pady=(5, 5))  # Add padding of 5 pixels at the top and bottom

# Create three columns with distinct separations
column1 = ctk.CTkFrame(column_frame, border_width=2, border_color="gray")
column1.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

column2 = ctk.CTkFrame(column_frame, border_width=2, border_color="gray")
column2.grid(row=0, column=1, sticky="nsew", padx=5)

column3 = ctk.CTkFrame(column_frame, border_width=2, border_color="gray")
column3.grid(row=0, column=2, sticky="nsew", padx=(5, 0))

# Configure the column frame to expand the columns
column_frame.grid_columnconfigure(0, weight=1)
column_frame.grid_columnconfigure(1, weight=1)
column_frame.grid_columnconfigure(2, weight=1)
column_frame.grid_rowconfigure(0, weight=1)

# Create a frame for the bottom padding
bottom_frame = ctk.CTkFrame(app, height=5)
bottom_frame.pack(side="bottom", fill="x")

# Create a frame for the Filters button and options
filters_frame = ctk.CTkFrame(column1)
filters_frame.pack(pady=10)

# Create the Filters button
filters_button = ctk.CTkButton(filters_frame, text="Filters", command=show_filters_options)
filters_button.pack()

# Create a frame for the filter options (initially hidden)
filter_options_frame = ctk.CTkFrame(column3)

# Create checkboxes for each filter option within the filter_options_frame
grayscale_checkbox = ctk.CTkCheckBox(filter_options_frame, text="Grayscale Conversion")
grayscale_checkbox.grid(row=0, column=0, sticky="w")

color_conversion_checkbox = ctk.CTkCheckBox(filter_options_frame, text="Color Conversion")
color_conversion_checkbox.grid(row=1, column=0, sticky="w")

color_switch_checkbox = ctk.CTkCheckBox(filter_options_frame, text="Color Switch")
color_switch_checkbox.grid(row=2, column=0, sticky="w")

extract_channel_checkbox = ctk.CTkCheckBox(filter_options_frame, text="Extract Channel")
extract_channel_checkbox.grid(row=3, column=0, sticky="w")

mix_channels_checkbox = ctk.CTkCheckBox(filter_options_frame, text="Mix Channels")
mix_channels_checkbox.grid(row=4, column=0, sticky="w")

# Configure the grid to expand options
filter_options_frame.grid_columnconfigure(0, weight=1)

def show_filters_options():
    filter_options_frame.pack(pady=10)

# Create a frame for the Adjust button and options
adjust_frame = ctk.CTkFrame(column1)
adjust_frame.pack(pady=10)

# Create the Adjust button
adjust_button = ctk.CTkButton(adjust_frame, text="Adjust", command=show_adjust_options)
adjust_button.pack()

# Create a frame for the adjust options (initially hidden)
adjust_options_frame = ctk.CTkFrame(column3)

# Create sliders for each adjust option
contrast_brightness_slider = ctk.CTkSlider(adjust_options_frame, from_=0, to=100)
contrast_brightness_slider.pack()

exposure_slider = ctk.CTkSlider(adjust_options_frame, from_=0, to=100)
exposure_slider.pack()

hue_saturation_slider = ctk.CTkSlider(adjust_options_frame, from_=0, to=100)
hue_saturation_slider.pack()

curves_slider = ctk.CTkSlider(adjust_options_frame, from_=0, to=100)
curves_slider.pack()

levels_slider = ctk.CTkSlider(adjust_options_frame, from_=0, to=100)
levels_slider.pack()

histogram_equalizer_slider = ctk.CTkSlider(adjust_options_frame, from_=0, to=100)
histogram_equalizer_slider.pack()

contrast_stretch_slider = ctk.CTkSlider(adjust_options_frame, from_=0, to=100)
contrast_stretch_slider.pack()

def show_adjust_options():
    adjust_options_frame.pack(pady=10)

# Create an instance of the MediaPlayerApp and add it to the middle column
media_player_app = MediaPlayerApp(column2)
media_player_app.pack(fill="both", expand=True)

app.mainloop()
