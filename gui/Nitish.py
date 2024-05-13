import tkinter as tk
import cv2
import time
from tkinter import filedialog
from datetime import timedelta
import customtkinter as ctk
from PIL import Image, ImageTk
from filters import *
from rect_tracker import RectTracker
from top_bar import *
from middle_panel import *
from bottom_bar import *


class VideoEditorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1600x900")
        # self.resizable(False,False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.current_filter = None
        self.selected_filter = "SobelFilter"

        self.rect_tracker = RectTracker()

        self.bbox = None
        self.tracker = cv2.legacy.TrackerBoosting_create()
        self.t = True
        
        
        self.video_capture = None
        self.current_file = None
        self.playing_video = False
        self.video_paused = False

        self.grid_rowconfigure(2,weight=3)
        self.grid_rowconfigure(3,weight=1)

        self.grid_columnconfigure(0,weight=1)

        
        create_menu(self)
        create_icon_frame(self)
        create_columns(self)
        create_media_player(self)

        
    def open_file(self):
            file_path = filedialog.askopenfilename(filetypes=[("Media Files", "*.mp4 *.avi")])
            if file_path:
                self.open_video(file_path)

    def save_file(self):
            if self.current_file:
                files = [('All Files', '*.*'), ('MP4 Files', '*.mp4'), ('AVI Files', '*.avi')]
                save_path = filedialog.asksaveasfilename(filetypes=files, defaultextension=files)
                if save_path:
                    print(f"Saving video to: {save_path}")

    def exit_app(self):
            if tk.messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
                self.destroy()

    def icon_function(self):
            print("Icon clicked")
            
    def show_filters_options(self):
        if self.adjust_options_frame_right.winfo_ismapped():
            self.adjust_options_frame_right.grid_forget()

        if self.filter_options_frame_right.winfo_ismapped():
            self.filter_options_frame_right.grid_forget()
        else:
            self.filter_options_frame_right.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    def show_adjust_options(self):
        if self.filter_options_frame_right.winfo_ismapped():
            self.filter_options_frame_right.grid_forget()

        if self.adjust_options_frame_right.winfo_ismapped():
            self.adjust_options_frame_right.grid_forget()
        else:
            self.adjust_options_frame_right.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
            
    def show_extractChannels_options(self):
        if self.extract_channels_options_frame_right.winfo_ismapped():
            self.extract_channels_options_frame_right.grid_forget()   
        else:
            self.extract_channels_options_frame_right.grid(row=0, column=0, padx=10, pady=10, sticky="ew") 

    def show_threshold_slider(self):
        if self.threshold_image_frame_right.winfo_ismapped():
            self.threshold_image_frame_right.grid_forget()  
        else:
            self.threshold_image_frame_right.grid(row=0, column=0, padx=10, pady=10, sticky="ew") 
            
    def apply_filter(self):
        pass

            
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
            print(self.rect_tracker.coor)
            if self.playing_video and not self.video_paused:
                start_time = time.time()
                ret, self.current_frame = self.video_capture.read()
                if ret:
                    self.current_frame = fit_canvas_and_RGB(self.current_frame,self.media_canvas.winfo_width(),self.media_canvas.winfo_height())

                    match self.selected_filter:
                        case "GraySacle" :
                            self.current_frame = grayScaleConversion(self.current_frame)
                        case "VerticalFlip":
                            self.current_frame = Verticalflip(self.current_frame)
                        case "HorizontalFlip":
                            self.current_frame = Horizontalflip(self.current_frame)
                        case "SobelFilter":
                            self.current_frame = sobelFilter(self.current_frame)

                    # bbox = cv2.selectROI(frame, False)
                    # print(bbox)
                    # raise TypeError
                    # if self.t:
                    #      self.t = False
                    #      self.tracker.init(frame, self.bbox)
                         
                    # frame, bbox, self.tracker = track_object_on_frame(frame, self.tracker , self.bbox)
                    # print(self.bbox)

                    # if(self.grayscale_checkbox.get()):
                    #     self.current_frame = cv2.cvtColor(self.current_frame, cv2.COLOR_BGR2GRAY)
                    # else:
                    #      

                    frame_image = ImageTk.PhotoImage(Image.fromarray(self.current_frame))
                    self.media_canvas.create_image(0, 0, anchor=tk.NW, image=frame_image,tag = "video")
                    self.media_canvas.image = frame_image

                    current_time = self.video_capture.get(cv2.CAP_PROP_POS_MSEC) / 1000
                    self.progress_slider.set(current_time)
                    current_time_str = str(timedelta(seconds=current_time))[:-3]
                    total_duration_str = str(timedelta(seconds=self.video_duration))[:-3]
                    self.time_label.configure(text=f"{current_time_str}/{total_duration_str}")

                end_time = time.time()
                elapsed_time = end_time - start_time
                if(elapsed_time!=0):
                    current_fps = 1 / elapsed_time
                # self.current_fps_label.configure(text=f"Current FPS: {current_fps:.2f}")

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

    def open_video(self, file_path):
        self.current_file = file_path
        self.play_video()
    
    def get_video_frame(self):
        image = ImageTk.PhotoImage(Image.fromarray(self.current_frame))
        self.image_canvas.create_image(0, 0, anchor=tk.NW, image=image,tag = "frame")
        self.image_canvas.image = image
    
    def start_drawing(self):
        self.image_canvas.delete("box")
        self.rect_tracker.coor = None
        self.rect_tracker.autodraw(canvas=self.image_canvas, fill="", outline="blue", width=2)

if __name__ == "__main__":
    video_editor_app = VideoEditorApp()
    # video_editor_app.after(0, lambda:video_editor_app.state('zoomed'))
    video_editor_app.mainloop()
         