import customtkinter as ctk

def create_media_player(app):
        # Media player below the three columns
        media_player_frame = ctk.CTkFrame(app)
        media_player_frame.grid(row=3,column=0,sticky="nsew", pady=10)

        # media_player_frame.grid_columnconfigure(0,weight=1)
        media_player_frame.grid_rowconfigure(0,weight=1)
        media_player_frame.grid_rowconfigure(1,weight=1)
        i = 0
        for i in range(10):
            media_player_frame.grid_columnconfigure(i,weight=1)
        
        # app.select_file_button = ctk.CTkButton(
        #     media_player_frame,
        #     text="Select File",
        #     font=("Arial", 12, "bold"),
        #     command=app.select_file,
        #     corner_radius=5
        # )
        # app.select_file_button.grid(row = 0, column=0,padx=5,sticky="sew")

        # app.play_button = ctk.CTkButton(
        #     media_player_frame,
        #     text="Play",
        #     font=("Arial", 12, "bold"),
        #     command=app.play_video,
        #     corner_radius=5
        # )
        # app.play_button.grid(row = 0, column=1,padx=(0,5),sticky="sew")

        app.pause_button = ctk.CTkButton(
            media_player_frame,
            text="Pause",
            font=("Arial", 12, "bold"),
            command=app.pause_video,
            corner_radius=5
        )
        app.pause_button.grid(row = 0, column=3,padx=(0,5),sticky="sew")

        app.stop_button = ctk.CTkButton(
            media_player_frame,
            text="Stop",
            font=("Arial", 12, "bold"),
            command=app.stop,
            corner_radius=5
        )
        app.stop_button.grid(row = 0, column=4,padx=(0,5),sticky="sew")

        app.fast_forward_button = ctk.CTkButton(
            media_player_frame,
            text="Fast Forward",
            font=("Arial", 12, "bold"),
            command=app.fast_forward,
            corner_radius=5
        )
        app.fast_forward_button.grid(row = 0, column=5,padx=(0,5),sticky="sew")

        app.rewind_button = ctk.CTkButton(
            media_player_frame,
            text="Rewind",
            font=("Arial", 12, "bold"),
            command=app.rewind,
            corner_radius=5
        )
        app.rewind_button.grid(row = 0, column=6,padx=(0,5),sticky="sew")

        # app.getFrame_button = ctk.CTkButton(
        #     media_player_frame,
        #     text="Get Frame",
        #     font=("Arial", 12, "bold"),
        #     command=app.get_video_frame,
        #     corner_radius=5
        # )
        # app.getFrame_button.grid(row = 0, column=6,padx=(0,5),sticky="sew")
        # app.draw_rect_button = ctk.CTkButton(
        #     media_player_frame, text="Draw Rectangle", command=app.start_drawing)
        # app.draw_rect_button.grid(row = 0, column=7,padx=(0,5),sticky="sew")

        app.progress_slider = ctk.CTkSlider(
            media_player_frame,
            from_=0,
            to=100,
            command=app.seek_video
        )
        

        app.progress_slider.set(0)
        app.progress_slider.grid(row = 1, column= 3,columnspan = 4,pady = (5,0),sticky="ew")

        app.time_label = ctk.CTkLabel(media_player_frame, text="", font=("Arial", 12, "bold"))
        # app.time_label.pack(pady=5)

        app.original_fps_label = ctk.CTkLabel(media_player_frame, text="Original FPS: ", font=("Arial", 12, "bold"))
        # app.original_fps_label.grid(row = 1, column=0,sticky="ew")

        app.current_fps_label = ctk.CTkLabel(media_player_frame, text="Current FPS: ", font=("Arial", 12, "bold"))
        # app.current_fps_label.grid(pady=5)
        # app.image_canvas.bind("<Button-1>", app.start_rect)
        # app.image_canvas.bind("<B1-Motion>", app.draw_rect)
        # app.image_canvas.bind("<ButtonRelease-1>", app.stop_rect)