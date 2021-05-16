import cv2 as cv
import numpy as np

file_path = "videos/video_1.mp4"

cap = cv.VideoCapture(file_path)
first_iter = True

while True:
    ret, frame = cap.read()

    if first_iter:
        avg = np.float32(frame)
        first_iter = False

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    threshold, thresh = cv.threshold(frame, 100, 255, cv.THRESH_BINARY)
    cv.accumulateWeighted(frame, avg, 0.005)

    background = cv.convertScaleAbs(avg)

    mask = cv.bitwise_xor(frame, background)

    segment = cv.absdiff(frame, background)

    masked_result = cv.bitwise_or(segment, frame)


    cv.imshow('input', frame)
    cv.imshow('gray', gray)
    cv.imshow('threshed', thresh)

    cv.imwrite("results/", result)

    #Check for keypress every frame_delay duration
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv.waitKey(-1) #wait until any key is pressed

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()