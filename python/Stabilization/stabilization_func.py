from platform import node
import cv2
from vidstab import VidStab, layer_overlay

def stabilize(input_path, output_path, smoothing_window=30, border_type='black', border_size='auto', output_fourcc='MJPG',kp_method=None):
    '''
    input_path = file path to input video

    output_path = file path for output video

    smoothing_window = window size to use when smoothing trajectory (default = 30)

    border_type = How to handle negative space created by stabilization translations/rotations. Options: ['black', 'reflect', 'replicate']

    border_size =  Size of border in output. Positive values will pad video equally on all sides, negative values will crop video equally on all sides, 'auto' will attempt to minimally pad to avoid cutting off portions of transformed frames

    output_fourcc – FourCC is a 4-byte code used to specify the video codec.

    kp_method – String of the type of keypoint detector to use. Available options are: ["GFTT", "BRISK", "DENSE", "FAST", "HARRIS", "MSER", "ORB", "STAR"]. ["SIFT", "SURF"] are additional non-free options available depending on your build of OpenCV. The non-free detectors are not tested with this package.

    '''
    if kp_method is None:
        stabilizer = VidStab()  
    else: 
        stabilizer = VidStab(kp_method=kp_method)
    stabilizer.stabilize(input_path=input_path, output_path=output_path,             smoothing_window=smoothing_window, border_type=border_type, border_size=border_size, output_fourcc=output_fourcc)

stabilize(input_path="ostrich.mp4",output_path="ostrich_stabilzed.avi")

