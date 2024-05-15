import cv2
import numpy as np

def process_video_in_memory(vidcap, ylims=None, xlims=None, rotate=True):
    """
    Process a video file in memory to calculate the mean image.

    Args:
    - moviefile (str): Path to the input video file.
    - ylims (tuple, optional): Tuple containing the vertical limits (top and bottom) for cropping the video frames.
    - xlims (tuple, optional): Tuple containing the horizontal limits (left and right) for cropping the video frames.
    - rotate (bool, optional): If True, rotate each frame by 180 degrees.

    Returns:
    - mean_image (numpy.ndarray): The mean image calculated from the video frames.
    """
    # Default crop limits (covering the entire frame)
    if ylims is None:
        ylims = (0, None)  # Cover from the top to the bottom
    if xlims is None:
        xlims = (0, None)  # Cover from the left to the right

    nframes = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Initialize variables to store cumulative sum and count of frames
    sum_frames = None
    count = 0

    # Read and process each frame
    while True:
        success, image = vidcap.read()
        if not success:
            break  # End of video
        
        # Crop the image to the desired size
        image = image[ylims[0]:ylims[1], xlims[0]:xlims[1]]

        # Rotate if needed
        # if rotate:
        #     image = np.rot90(image, 2)

        # Add current frame to cumulative sum
        if sum_frames is None:
            sum_frames = np.zeros_like(image, dtype=np.float64)
        sum_frames += image.astype(np.float64)
        
        count += 1

    # Calculate mean
    mean_image = (sum_frames / count).astype(np.uint8)

    # kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    # im = cv2.filter2D(mean_image, -1, kernel)

    return mean_image

# # Example usage
# if __name__ == "__main__":
#     moviefile = 'C://Users//nitis//OneDrive//Desktop//SLP//gui//output.avi'
#     mean_image_cv2 = process_video_in_memory(moviefile)
#     cv2.imshow("Mean Image", mean_image_cv2)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

