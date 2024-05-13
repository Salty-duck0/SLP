import cv2
def fit_canvas_and_RGB(frame,width,height):
    frame = cv2.resize(frame,(width,height))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

def grayScaleConversion(frame):
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return grayFrame

def rotate(frame):
    pass

def Verticalflip(frame):
    VerticalFilpped = cv2.flip(frame,1)
    return VerticalFilpped

def Horizontalflip(frame):
    HorizontalFilpped = cv2.flip(frame,0)
    return HorizontalFilpped
    

def sobelFilter(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    return grad


def medianFilter(img,kernelSize):
    median = cv2.medianBlur(img, kernelSize)
    return median


def AverageFilter(img,kernelSize):
    avgBlur = cv2.blur(img, kernelSize)
    return avgBlur

def bilateralFiltering(img , dValue, sigmaColor, sigmaSpace):
    bilateral = cv2.bilateralFilter(img, dValue, sigmaColor, sigmaSpace) 
    return bilateral

def laplaceFilter(img):
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    return laplacian

def CannyFilter(img ,t_lower,t_upper):
    edge = cv2.Canny(img, t_lower, t_upper) 
    return edge
    

def threshold(img, l_thres, u_thres):
    ret, thresh1 = cv2.threshold(img, l_thres, u_thres, cv2.THRESH_BINARY) 
    return thresh1

def adaptiveThreshold(img,max,blockSize, constant):
    thresh1 = cv2.adaptiveThreshold(img, max, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize,constant) 
    return thresh1

def track_object_on_frame(frame, tracker, bbox):
    timer = cv2.getTickCount()
    ret, bbox = tracker.update(frame)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    if ret:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv2.putText(frame, " Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
    cv2.putText(frame, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
    return frame, bbox, tracker