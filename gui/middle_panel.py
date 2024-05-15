import tkinter as tk
import customtkinter as ctk
import cv2

def create_columns(app):
        # Left column for filters and adjust options
        main_panel = ctk.CTkFrame(app, border_width=2, border_color="gray")
        main_panel.grid(row=2,sticky="nsew", pady=10)

        main_panel.grid_rowconfigure(0,weight=1)
        main_panel.grid_columnconfigure(0,weight=1)
        main_panel.grid_columnconfigure(1,weight=2)
        main_panel.grid_columnconfigure(2,weight=1)


        left_column = ctk.CTkFrame(main_panel, border_width=2, border_color="gray")
        left_column.grid(row=0, column=0, sticky="nsew", padx=(5, 0), pady=10)

        left_column.grid_columnconfigure(0,weight=1)
        left_column.grid_rowconfigure(0,weight=1)
        left_column.grid_rowconfigure(1,weight=1)

        filter_panel = ctk.CTkScrollableFrame(left_column, border_width=2, border_color="gray")
        filter_panel.grid(row=0, column=0, sticky="nsew", padx=(5, 5), pady=10)
        filter_panel.grid_columnconfigure(0,weight=1)
        filter_panel.grid_columnconfigure(1,weight=1)

        tool_panel = ctk.CTkFrame(left_column, border_width=2, border_color="gray")
        tool_panel.grid(row=1, column=0, sticky="nsew", padx=(5, 5), pady=10)
        # tool_panel.grid_rowconfigure(0,weight=1)
        # tool_panel.grid_rowconfigure(1,weight=1)
        # tool_panel.grid_rowconfigure(2,weight=1)
        tool_panel.grid_columnconfigure(0,weight=1)


        grayscale_button = ctk.CTkButton(filter_panel, text="Grayscale", command = app.show_grayscale_options)
        grayscale_button.grid(row=0, column=0, padx = 5, pady=10)

        color_conversion_button = ctk.CTkButton(filter_panel, text="Color Conversion", command = app.show_color_conversion_options)
        color_conversion_button.grid(row=1, column=0, padx = 5, pady=10)

        color_switch_button = ctk.CTkButton(filter_panel, text="Color Switch",command = app.show_color_switch_options)
        color_switch_button.grid(row=2, column=0, padx = 5, pady=10)

        extract_channel_button = ctk.CTkButton(filter_panel, text="Extract Channel",command = app.show_extract_channel_options)
        extract_channel_button.grid(row=3, column=0, padx = 5, pady=10)

        mix_channel_button = ctk.CTkButton(filter_panel, text="Mix Channel",command = app.show_mix_channel_options)
        mix_channel_button.grid(row=4, column=0, padx = 5, pady=10)

        negative_button = ctk.CTkButton(filter_panel, text="Negative",command = app.show_negative_options)
        negative_button.grid(row=5, column=0, padx = 5, pady=10)

        threshold_button = ctk.CTkButton(filter_panel, text="Threshold",command = app.show_threshold_options)
        threshold_button.grid(row=6, column=0, padx = 5, pady=10)

        denoise_button = ctk.CTkButton(filter_panel, text="Denoise",command = app.show_denoise_options)
        denoise_button.grid(row=7, column=0, padx = 5, pady=10)

        object_tracking_button = ctk.CTkButton(filter_panel, text="Object Tracking",command = app.show_object_tracking_options)
        object_tracking_button.grid(row=8, column=0, padx = 5, pady=10)

        stabilization_button = ctk.CTkButton(filter_panel, text="Stabalization",command =  app.show_stabilization_options)
        stabilization_button.grid(row=9, column=0, padx = 5, pady=10)

        get_frame_button = ctk.CTkButton(filter_panel, text="Get Frame",command=app.get_video_frame)
        get_frame_button.grid(row=10, column=0, padx = 5, pady=10)

        # filters_button = ctk.CTkButton(filter_panel, text="Filters", command=app.show_filters_options)
        # filters_button.grid(row=0, column=1, padx = 5, pady=10)

        # adjust_button = ctk.CTkButton(filter_panel, text="Adjust", command=app.show_adjust_options)
        # adjust_button.grid(row=1, column=1, padx = 5, pady=10)

        crop_button = ctk.CTkButton(filter_panel, text="Crop", command=app.show_crop_options)
        crop_button.grid(row=0, column=1, padx = 5, pady=10)

        hflip_button = ctk.CTkButton(filter_panel, text="Horizontal Flip", command=app.show_hflip_options)
        hflip_button.grid(row=1, column=1, padx = 5, pady=10)

        vflip_button = ctk.CTkButton(filter_panel, text="Vertical Flip", command=app.show_vflip_options)
        vflip_button.grid(row=2, column=1, padx = 5, pady=10)

        frame_avg_button = ctk.CTkButton(filter_panel, text="Frame Average", command=app.show_frame_avg_options)
        frame_avg_button.grid(row=3, column=1, padx = 5, pady=10)

        Sobel_button = ctk.CTkButton(filter_panel, text="Sobel", command=app.show_sobel_options)
        Sobel_button.grid(row=4, column=1, padx = 5, pady=10)

        Median_button = ctk.CTkButton(filter_panel, text="Median", command=app.show_median_options)
        Median_button.grid(row=5, column=1, padx = 5, pady=10)

        # Left lower column 
        draw_rect_button = ctk.CTkButton(tool_panel, text="Draw Rectangle", command=app.start_drawing)
        draw_rect_button.grid(row=0, column=0, padx = 10, pady=10,sticky="new")

        rec_start_button = ctk.CTkButton(tool_panel, text="Start Rec", command=app.set_rec_true)
        rec_start_button.grid(row=1, column=0, padx = 10, pady=10,sticky="new")

        rec_stop_button = ctk.CTkButton(tool_panel, text="Stop Rec", command=app.set_rec_false)
        rec_stop_button.grid(row=2, column=0, padx = 10, pady=10,sticky="new")

        # Middle column for canvas
        middle_column = ctk.CTkTabview(main_panel, border_width=2, border_color="gray")
        middle_column.grid(row=0, column=1, sticky="new", padx=5, pady=5)

        middle_column.add("Video")
        middle_column.add("Image")

        middle_column.tab("Image").grid_rowconfigure(0, weight=1)
        middle_column.tab("Image").grid_columnconfigure(0, weight=1)
        middle_column.tab("Video").grid_rowconfigure(0, weight=1)
        middle_column.tab("Video").grid_columnconfigure(0, weight=1)


        app.media_canvas = tk.Canvas(middle_column.tab("Video"), width=1280, height=720, background='black', highlightbackground="gray75")
        app.media_canvas.grid(row=0, column=0, sticky="nsew")

        app.image_canvas = tk.Canvas(middle_column.tab("Image"), width=1280, height=720, background='black', highlightbackground="gray75")
        app.image_canvas.grid(row=0, column=0, sticky="nsew")

        middle_column.grid_rowconfigure(0, weight=1)
        middle_column.grid_columnconfigure(0, weight=1)

        # Right column for filter and adjust options settings
        right_column = ctk.CTkFrame(main_panel, border_width=2, border_color="gray")
        right_column.grid(row=0, column=2, sticky="nsew", padx=(5, 0), pady=10)
        
        right_column.grid_columnconfigure(0,weight=1)
        right_column.grid_rowconfigure(0,weight=1)
        right_column.grid_rowconfigure(1,weight=1)
        right_column.grid_propagate(False)

        filter_results_panel = ctk.CTkFrame(right_column, border_width=2, border_color="gray")
        filter_results_panel.grid(row=0, column=0, sticky="nsew", padx=(5, 5), pady=10)
        filter_results_panel.grid_columnconfigure(0,weight=1)
        filter_results_panel.grid_columnconfigure(1,weight=1)

        # app.grayscale_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.grayscale_text.grid(row = 0, column =0)

        # app.color_conversion_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.color_conversion_text.grid(row = 0, column =0)

        # app.color_switch_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.color_switch_text.grid(row = 0, column =0)

        # app.extract_channel_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.extract_channel_text.grid(row = 0, column =0)

        # app.mix_channel_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.mix_channel_text.grid(row = 0, column =0)

        # app.negative_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.negative_text.grid(row = 0, column =0)

        # app.threshold_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.threshold_text.grid(row = 0, column =0)

        # app.denoise_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.denoise_text.grid(row = 0, column =0)

        # app.object_tracking_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.object_tracking_text.grid(row = 0, column =0)

        # app.stabilization_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.stabilization_text.grid(row = 0, column =0)

        # app.filter_options_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.filter_options_text.grid(row = 0, column =0)

        # app.adjust_options_text = ctk.CTkLabel(master=right_column,text = "Grayscale filter is used to convert an image to grayscale")
        # app.adjust_options_text.grid(row = 0, column =0)

        app.grayscale_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.grayscale_text.insert("0.0", "Grayscale filter is used to convert an image to grayscale")
        app.grayscale_text.grid(row = 0, column =0)

        app.color_conversion_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.color_conversion_text.insert("0.0", "Color converion")
        app.color_conversion_text.grid(row = 0, column =0)

        app.color_switch_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.color_switch_text.insert("0.0", "Color switch")
        app.color_switch_text.grid(row = 0, column =0)

        app.extract_channel_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.extract_channel_text.insert("0.0", "Extract Channel")
        app.extract_channel_text.grid(row = 0, column =0)

        app.mix_channel_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.mix_channel_text.insert("0.0", "Mix Channel")
        app.mix_channel_text.grid(row = 0, column =0)

        app.negative_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.negative_text.insert("0.0", "Negative")
        app.negative_text.grid(row = 0, column =0)

        app.threshold_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.threshold_text.insert("0.0", "Threshold")
        app.threshold_text.grid(row = 0, column =0)

        app.denoise_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.denoise_text.insert("0.0", "Denoise")
        app.denoise_text.grid(row = 0, column =0)

        app.object_tracking_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.object_tracking_text.insert("0.0", "Deblur")
        app.object_tracking_text.grid(row = 0, column =0)

        app.stabilization_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.stabilization_text.insert("0.0", "Stabilization")
        app.stabilization_text.grid(row = 0, column =0)

        app.horizontal_flip_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.horizontal_flip_text.insert("0.0", "Horizontal")
        app.horizontal_flip_text.grid(row = 0, column =0)

        app.vertical_flip_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.vertical_flip_text.insert("0.0", "Vertical")
        app.vertical_flip_text.grid(row = 0, column =0)

        app.frame_avg_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.frame_avg_text.insert("0.0", "Frame Average")
        app.frame_avg_text.grid(row = 0, column =0)

        app.sobel_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.sobel_text.insert("0.0", "Frame Average")
        app.sobel_text.grid(row = 0, column =0)

        app.median_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        app.median_text.insert("0.0", "Frame Average")
        app.median_text.grid(row = 0, column =0)

        # app.filter_options_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        # app.filter_options_text.insert("0.0", "Filter options")
        # app.filter_options_text.grid(row = 0, column =0)

        # app.adjust_options_text = ctk.CTkTextbox(master=filter_results_panel, width=150, corner_radius=0)
        # app.adjust_options_text.insert("0.0", "Adjust options")
        # app.adjust_options_text.grid(row = 0, column =0)
        

        app.right_lower_panel = ctk.CTkFrame(right_column, border_width=2, border_color="gray")
        app.right_lower_panel.grid(row=1, column=0, sticky="nsew", padx=(5, 5), pady=10)
        # app.right_lower_panel.grid_rowconfigure(0,weight=1)
        app.right_lower_panel.grid_columnconfigure(0,weight=1)


        # app.filter_options_frame_right = ctk.CTkFrame(filter_results_panel)

        # MedianFilter = ctk.CTkCheckBox(app.filter_options_frame_right, text="Median Filter")
        # MedianFilter.grid(row=0, column=0, pady=5,sticky="w")

        # Bilateral_Filter = ctk.CTkCheckBox(app.filter_options_frame_right, text="Bilateral Filter")
        # Bilateral_Filter.grid(row=1, column=0, pady=5,sticky="w")

        # Laplace_Filter = ctk.CTkCheckBox(app.filter_options_frame_right, text="Laplace Filter")
        # Laplace_Filter.grid(row=2, column=0, pady=5,sticky="w")

        # Average_Filter = ctk.CTkCheckBox(app.filter_options_frame_right, text="Average Filter")
        # Average_Filter.grid(row=3, column=0, pady=5,sticky="w")

        # Canny_Filter = ctk.CTkCheckBox(app.filter_options_frame_right, text="Canny Filter")
        # Canny_Filter.grid(row=4, column=0, pady=5,sticky="w")
        
        Apply_Filter = ctk.CTkButton(app.right_lower_panel, text="Apply",command=app.select_filter)
        Apply_Filter.grid(row=0, column=0, padx = 10, pady=10,sticky="new")

        Deselect_Filter = ctk.CTkButton(app.right_lower_panel, text="Deselect",command=app.deseclect_filter)
        Deselect_Filter.grid(row=1, column=0, padx = 10, pady=10,sticky="new")

        # app.filter_options_frame_right.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        # app.filter_options_frame_right.grid_columnconfigure(0, weight=1)
        # app.filter_options_frame_right.grid_propagate(False)
        
        # app.adjust_options_frame_right = ctk.CTkFrame(filter_results_panel)
        # app.adjust_options_frame_right.grid_rowconfigure(0, weight=1)
        # app.adjust_options_frame_right.grid_columnconfigure(0, minsize=100)
        # app.adjust_options_frame_right.grid_columnconfigure(1, weight=1)
        # app.adjust_options_frame_right.grid_propagate(False)

        sliders_info = [
            ("Contrast Brightness", 0),
            ("Exposure", 1),
            ("Hue Saturation", 2),
            ("Curves", 3),
            ("Levels", 4),
            ("Histogram Equalizer", 5),
            ("Contrast Stretch", 6)
        ]

        # for name, row in sliders_info:
        #     label = ctk.CTkLabel(app.adjust_options_frame_right, text=name)
        #     label.grid(row=row, column=0, sticky="w", padx=(0, 5))

        #     slider = ctk.CTkSlider(app.adjust_options_frame_right, from_=0, to=100)
        #     slider.grid(row=row, column=1, sticky="ew")
                
        # app.extract_channels_options_frame_right = ctk.CTkFrame(filter_results_panel) 
        
        # app.extractChannels_radiobutton = ctk.CTkRadioButton(app.extract_channels_options_frame_right, text="Extract Channels")
        # app.extractChannels_radiobutton.grid(row=0, column=0, sticky="w")
        
        # app.selected_channel = ctk.StringVar()

        # Red_Channel = ctk.CTkRadioButton(app.extract_channels_options_frame_right, text="Red Channel", variable=app.selected_channel, value="red")
        # Red_Channel.grid(row=1, column=0, sticky="w")

        # Green_Channel = ctk.CTkRadioButton(app.extract_channels_options_frame_right, text="Green Channel", variable=app.selected_channel, value="green")
        # Green_Channel.grid(row=2, column=0, sticky="w")

        # Blue_Channel = ctk.CTkRadioButton(app.extract_channels_options_frame_right, text="Blue Channel", variable=app.selected_channel, value="blue")
        # Blue_Channel.grid(row=3, column=0, sticky="w")

        # app.filter_options_frame_right.grid_forget()
        # app.adjust_options_frame_right.grid_forget()
        app.grayscale_text.grid_forget()
        app.color_conversion_text.grid_forget()
        app.color_switch_text.grid_forget()
        app.extract_channel_text.grid_forget()
        app.mix_channel_text.grid_forget()
        app.negative_text.grid_forget()
        app.threshold_text.grid_forget()
        app.denoise_text.grid_forget()
        app.object_tracking_text.grid_forget()
        app.stabilization_text.grid_forget()
        # app.filter_options_text.grid_forget()
        # app.adjust_options_text.grid_forget()
        app.horizontal_flip_text.grid_forget()
        app.vertical_flip_text.grid_forget()
        app.frame_avg_text.grid_forget()
        app.sobel_text.grid_forget()
        app.median_text.grid_forget()