import cv2

def extract_and_save_altered_frames(original_video_path, saved_video_path, output_dir):
    try:
        cap_original = cv2.VideoCapture(original_video_path)
        cap_saved = cv2.VideoCapture(saved_video_path)
        
        frame_num = 0
        while cap_original.isOpened() and cap_saved.isOpened():
            ret_original, frame_original = cap_original.read()
            ret_saved, frame_saved = cap_saved.read()
            
            if not ret_original or not ret_saved:
                break
            
            if not (frame_original == frame_saved).all():
                cv2.imwrite(f"{output_dir}/altered_frame_{frame_num}.jpg", frame_saved)
                frame_num += 1
        
        cap_original.release()
        cap_saved.release()

        # Check if both videos have the same number of frames
        if frame_num != int(cap_original.get(cv2.CAP_PROP_FRAME_COUNT)):
            print("Warning: Videos have a different number of frames.")
    except Exception as e:
        print("Error:", e)

original_video_path = "race_car.mp4"
saved_video_path = "race_car-CSRT.mp4"
output_directory = "altered_frames"
extract_and_save_altered_frames(original_video_path, saved_video_path, output_directory)
