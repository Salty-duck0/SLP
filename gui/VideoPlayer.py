import tkinter as tk
from tkinter import ttk
import vlc
from tkinter import filedialog
from datetime import timedelta
import customtkinter as ctk

ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class MediaPlayerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Media Player")
        self.geometry(f"{1500}x{900}")
        self.initialize_player()

    def initialize_player(self):
        self.instance = vlc.Instance()
        self.media_player = self.instance.media_player_new()
        self.current_file = None
        self.playing_video = False
        self.video_paused = False
        self.create_widgets()

    def create_widgets(self):
        self.media_canvas = tk.Canvas(self, width=800, height=400,background='black',highlightbackground="gray75") 
        self.media_canvas.pack(pady=10, fill=tk.BOTH, expand=True)
        
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
        file_path = filedialog.askopenfilename(
            filetypes=[("Media Files", "*.mp4 *.avi")]
        )
        if file_path:
            self.current_file = file_path
            self.play_video()

    def play_video(self):
        if not self.playing_video:
            media = self.instance.media_new(self.current_file)
            self.media_player.set_media(media)
            self.media_player.set_hwnd(self.media_canvas.winfo_id())
            self.media_player.play()
            self.playing_video = True
            self.update_video_progress()

    def update_video_progress(self):
        if self.playing_video:
            total_duration = self.media_player.get_length()
            current_time = self.media_player.get_time()
            if total_duration > 0:
                progress_percentage = (current_time / total_duration) * 100
                self.progress_slider.set(progress_percentage)
                current_time_str = str(timedelta(milliseconds=current_time))[:-3]
                total_duration_str = str(timedelta(milliseconds=total_duration))[:-3]
                self.time_label.configure(text=f"{current_time_str}/{total_duration_str}")
        self.after(10, self.update_video_progress)

    def seek_video(self, value):
        if self.playing_video:
            total_duration = self.media_player.get_length()
            if total_duration > 0:
                seek_time = int((int(value) / 100) * total_duration) 
                self.media_player.set_time(seek_time)


    def fast_forward(self):
        if self.playing_video:
            current_time = self.media_player.get_time() + 5000
            self.media_player.set_time(current_time)

    def rewind(self):
        if self.playing_video:
            current_time = self.media_player.get_time() - 5000
            self.media_player.set_time(current_time)

    def pause_video(self):
        if self.playing_video:
            if self.video_paused:
                self.media_player.play()
                self.video_paused = False
                self.pause_button.configure(text="Pause")
            else:
                self.media_player.pause()
                self.video_paused = True
                self.pause_button.configure(text="Resume")

    def stop(self):
        if self.playing_video:
            self.media_player.stop()
            self.playing_video = False

if __name__ == "__main__":
    app = MediaPlayerApp()
    app.mainloop()
