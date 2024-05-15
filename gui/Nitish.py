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

from frame_avg_final import *


class VideoEditorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1600x900")
        # self.resizable(False,False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.current_filter = None
        self.selected_filter = None

        self.current_frame = None

        self.rect_tracker = RectTracker()

        self.bbox = None
        self.tracker = cv2.TrackerCSRT_create()
        self.t = True

        self.output = None

        self.recording = False
        
        
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
    
    def set_rec_true(self):
        self.output = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 60.0, (self.media_canvas.winfo_width(),self.media_canvas.winfo_height()), True) 
        self.recording = True

    def set_rec_false(self):
         self.recording = False

        
    def open_file(self):
            self.stop()
            file_path = filedialog.askopenfilename(filetypes=[("Media Files", "*.mp4 *.avi")])
            if file_path:
                self.open_video(file_path)

    def save_file(self):
        print("Saved")
        self.output.release()

    def exit_app(self):
            if tk.messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
                self.destroy()

    def icon_function(self):
            print("Icon clicked")

    def check_right_column_options(self):
        # self.adjust_options_frame_right.grid_forget()
        # self.filter_options_frame_right.grid_forget()
        self.grayscale_text.grid_forget()
        self.color_conversion_text.grid_forget()
        self.color_switch_text.grid_forget()
        self.extract_channel_text.grid_forget()
        self.mix_channel_text.grid_forget()
        self.negative_text.grid_forget()
        self.threshold_text.grid_forget()
        self.denoise_text.grid_forget()
        self.object_tracking_text.grid_forget()
        self.stabilization_text.grid_forget()
        # self.filter_options_text.grid_forget()
        # self.adjust_options_text.grid_forget()
        self.horizontal_flip_text.grid_forget()
        self.vertical_flip_text.grid_forget()
        self.frame_avg_text.grid_forget()
        self.sobel_text.grid_forget()
        self.median_text.grid_forget()

    def show_frame_avg_options(self):
        self.check_right_column_options()
        self.frame_avg_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.current_filter = "FrameAverage"

    def show_sobel_options(self):
        self.check_right_column_options()
        self.sobel_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.current_filter = "SobelFilter"

    def show_median_options(self):
        self.check_right_column_options()
        self.median_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.current_filter = "MedianFilter"
            
    # def show_filters_options(self):
    #     self.check_right_column_options()
    #     self.filter_options_frame_right.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    #     self.filter_options_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")        

    def show_grayscale_options(self):
        self.check_right_column_options()
        self.grayscale_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.current_filter = "GraySacle"

    def show_color_conversion_options(self):
        self.check_right_column_options()
        self.color_conversion_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")

    def show_hflip_options(self):
        self.check_right_column_options()
        self.horizontal_flip_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.current_filter = "HorizontalFlip"

    def show_vflip_options(self):
        self.check_right_column_options()
        self.vertical_flip_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.current_filter = "VerticalFlip"

    def show_color_switch_options(self):
        self.check_right_column_options()
        self.color_switch_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.current_filter = "ColorSwitch"
    
    def show_extract_channel_options(self):
        self.check_right_column_options()
        self.extract_channel_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
    
    def show_mix_channel_options(self):
        self.check_right_column_options()
        self.mix_channel_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
    
    def show_negative_options(self):
        self.check_right_column_options()
        self.negative_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.current_filter = "Negative"
    
    def show_threshold_options(self):
        self.check_right_column_options()
        self.threshold_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        self.current_filter = "Threshold"
        
    
    def show_denoise_options(self):
        self.check_right_column_options()
        self.denoise_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
    
    def show_object_tracking_options(self):
        self.check_right_column_options()
        self.object_tracking_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")

        self.current_filter = "ObjectTracking"
        b = (self.rect_tracker.coor[0][0],self.rect_tracker.coor[0][1],self.rect_tracker.coor[1][0]-self.rect_tracker.coor[0][0],self.rect_tracker.coor[1][1]-self.rect_tracker.coor[0][1])
        self.tracker.init(self.current_frame,b )

    def show_stabilization_options(self):
        self.check_right_column_options()
        self.stabilization_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")
        
    # def show_adjust_options(self):
    #     self.check_right_column_options()
    #     self.adjust_options_frame_right.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    #     self.adjust_options_text.grid(row=0, column=0, padx=10, pady=10, sticky="new")

    def show_crop_options(self):
        self.check_right_column_options()
        self.current_filter = "Crop"
    
    def select_filter(self):
        self.selected_filter = self.current_filter

    def deseclect_filter(self):
        self.selected_filter = None 
            
    def apply_filter(self):
        match self.selected_filter:
            case "GraySacle" :
                self.current_frame = grayScaleConversion(self.current_frame)
            case "VerticalFlip":
                self.current_frame = Verticalflip(self.current_frame)
            case "HorizontalFlip":
                self.current_frame = Horizontalflip(self.current_frame)
            case "Negative":
                self.current_frame = 255 - self.current_frame
            case "ColorSwitch":
                self.current_frame = cv2.cvtColor(self.current_frame, cv2.COLOR_RGB2BGR)
            case "SobelFilter":
                self.current_frame = sobelFilter(self.current_frame)
            case "MedianFilter":
                self.current_frame = medianFilter(self.current_frame,___)
            case "AverageFilter":
                self.current_frame = averageFilter(self.current_frame,___)
            case "bilateralFilter":
                self.current_frame = bilateralFilter(self.current_frame,___,___,___)
            case "laplaceFilter":
                self.current_frame = laplaceFilter(self.current_frame)
            case "Threshold":
                self.current_frame = laplaceFilter(self.current_frame,128,255)
            case "AptiveThreshold":
                self.current_frame = adaptiveThreshold(self.current_frame,___,___)
            case "ObjectTracking":
                    self.current_frame, self.bbox, self.tracker = track_object_on_frame(self.current_frame, self.tracker , self.bbox)
                    self.current_frame = self.current_frame[self.bbox[1]:self.bbox[1]+self.bbox[3],self.bbox[0]:self.bbox[0]+self.bbox[2],:]
                    self.current_frame = cv2.resize(self.current_frame,(self.media_canvas.winfo_width(),self.media_canvas.winfo_height()))
            case "Crop":
                self.current_frame = self.current_frame[self.rect_tracker.coor[0][1]:self.rect_tracker.coor[1][1],self.rect_tracker.coor[0][0]:self.rect_tracker.coor[1][0],:]
                self.current_frame = cv2.resize(self.current_frame,(self.media_canvas.winfo_width(),self.media_canvas.winfo_height()))
            case "FrameAverage":
                img = process_video_in_memory(self.video_capture)[:, :, ::-1]
                image = ImageTk.PhotoImage(Image.fromarray(img))
                self.image_canvas.create_image(0, 0, anchor=tk.NW, image=image,tag = "frame")
                self.image_canvas.image = image



            
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
                ret, self.current_frame = self.video_capture.read()
                if ret:
                    self.current_frame = fit_canvas_and_RGB(self.current_frame,self.media_canvas.winfo_width(),self.media_canvas.winfo_height())
                    self.apply_filter()

                    if self.recording:
                        if(self.current_frame.shape[2] == 3):
                            self.current_frame = cv2.cvtColor(self.current_frame, cv2.COLOR_RGB2BGR)
                            self.output.write(self.current_frame)
                            self.current_frame = cv2.cvtColor(self.current_frame, cv2.COLOR_RGB2BGR)
                        else:
                            self.output.write(self.current_frame)

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
         