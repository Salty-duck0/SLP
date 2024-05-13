import tkinter as tk
import customtkinter as ctk

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
        tool_panel.grid_rowconfigure(0,weight=1)
        tool_panel.grid_columnconfigure(0,weight=1)

        grayscale_button = ctk.CTkButton(filter_panel, text="Grayscale")
        grayscale_button.grid(row=0, column=0, padx = 5, pady=10)

        color_conversion_button = ctk.CTkButton(filter_panel, text="Color Conversion")
        color_conversion_button.grid(row=1, column=0, padx = 5, pady=10)

        color_switch_button = ctk.CTkButton(filter_panel, text="Color Switch")
        color_switch_button.grid(row=2, column=0, padx = 5, pady=10)

        extract_channel_button = ctk.CTkButton(filter_panel, text="Extract Channel")
        extract_channel_button.grid(row=3, column=0, padx = 5, pady=10)

        mix_channel_button = ctk.CTkButton(filter_panel, text="Mix Channel")
        mix_channel_button.grid(row=4, column=0, padx = 5, pady=10)

        negative_button = ctk.CTkButton(filter_panel, text="Negative")
        negative_button.grid(row=5, column=0, padx = 5, pady=10)

        threshold_button = ctk.CTkButton(filter_panel, text="Threshold")
        threshold_button.grid(row=6, column=0, padx = 5, pady=10)

        denoise_button = ctk.CTkButton(filter_panel, text="Denoise")
        denoise_button.grid(row=7, column=0, padx = 5, pady=10)

        deblur_button = ctk.CTkButton(filter_panel, text="Deblur")
        deblur_button.grid(row=8, column=0, padx = 5, pady=10)

        stabilization_button = ctk.CTkButton(filter_panel, text="Stabalization")
        stabilization_button.grid(row=9, column=0, padx = 5, pady=10)

        get_frame_button = ctk.CTkButton(filter_panel, text="Get Frame",command=app.get_video_frame)
        get_frame_button.grid(row=10, column=0, padx = 5, pady=10)

        filters_button = ctk.CTkButton(filter_panel, text="Filters", command=app.show_filters_options)
        filters_button.grid(row=0, column=1, padx = 5, pady=10)

        adjust_button = ctk.CTkButton(filter_panel, text="Adjust", command=app.show_adjust_options)
        adjust_button.grid(row=1, column=1, padx = 5, pady=10)

        # Left lower column 
        draw_rect_button = ctk.CTkButton(tool_panel, text="Draw Rectangle", command=app.start_drawing)
        draw_rect_button.grid(row=0, column=0, padx = 10, pady=10,sticky="new")

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

        app.right_lower_panel = ctk.CTkFrame(right_column, border_width=2, border_color="gray")
        app.right_lower_panel.grid(row=1, column=0, sticky="nsew", padx=(5, 5), pady=10)
        app.right_lower_panel.grid_rowconfigure(0,weight=1)
        app.right_lower_panel.grid_columnconfigure(0,weight=1)


        app.filter_options_frame_right = ctk.CTkFrame(filter_results_panel)

        MedianFilter = ctk.CTkCheckBox(app.filter_options_frame_right, text="Median Filter")
        MedianFilter.grid(row=0, column=0, sticky="w")

        Bilateral_Filter = ctk.CTkCheckBox(app.filter_options_frame_right, text="Bilateral Filter")
        Bilateral_Filter.grid(row=1, column=0, sticky="w")

        Laplace_Filter = ctk.CTkCheckBox(app.filter_options_frame_right, text="Laplace Filter")
        Laplace_Filter.grid(row=2, column=0, sticky="w")

        Average_Filter = ctk.CTkCheckBox(app.filter_options_frame_right, text="Average Filter")
        Average_Filter.grid(row=3, column=0, sticky="w")

        Canny_Filter = ctk.CTkCheckBox(app.filter_options_frame_right, text="Canny Filter")
        Canny_Filter.grid(row=4, column=0, sticky="w")
        
        Apply_Filter = ctk.CTkButton(app.right_lower_panel, text="Apply", command=app.apply_filter,)
        Apply_Filter.grid(row=0, column=0, padx = 10, pady=10,sticky="new")

        app.filter_options_frame_right.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        app.adjust_options_frame_right = ctk.CTkFrame(filter_results_panel)
        app.adjust_options_frame_right.grid_rowconfigure(0, weight=1)
        app.adjust_options_frame_right.grid_columnconfigure(0, minsize=100)
        app.adjust_options_frame_right.grid_columnconfigure(1, weight=1)
        app.adjust_options_frame_right.grid_propagate(False)

        sliders_info = [
            ("Contrast Brightness", 0),
            ("Exposure", 1),
            ("Hue Saturation", 2),
            ("Curves", 3),
            ("Levels", 4),
            ("Histogram Equalizer", 5),
            ("Contrast Stretch", 6)
        ]

        for name, row in sliders_info:
            label = ctk.CTkLabel(app.adjust_options_frame_right, text=name)
            label.grid(row=row, column=0, sticky="w", padx=(0, 5))

            slider = ctk.CTkSlider(app.adjust_options_frame_right, from_=0, to=100)
            slider.grid(row=row, column=1, sticky="ew")
                
        app.extract_channels_options_frame_right = ctk.CTkFrame(filter_results_panel) 
        
        app.extractChannels_radiobutton = ctk.CTkRadioButton(app.extract_channels_options_frame_right, text="Extract Channels")
        app.extractChannels_radiobutton.grid(row=0, column=0, sticky="w")
        
        app.selected_channel = ctk.StringVar()

        Red_Channel = ctk.CTkRadioButton(app.extract_channels_options_frame_right, text="Red Channel", variable=app.selected_channel, value="red")
        Red_Channel.grid(row=1, column=0, sticky="w")

        Green_Channel = ctk.CTkRadioButton(app.extract_channels_options_frame_right, text="Green Channel", variable=app.selected_channel, value="green")
        Green_Channel.grid(row=2, column=0, sticky="w")

        Blue_Channel = ctk.CTkRadioButton(app.extract_channels_options_frame_right, text="Blue Channel", variable=app.selected_channel, value="blue")
        Blue_Channel.grid(row=3, column=0, sticky="w")

        app.extract_channels_options_frame_right.grid_forget()
        app.adjust_options_frame_right.grid_forget()
        app.filter_options_frame_right.grid_forget()