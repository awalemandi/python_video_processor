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

    cv.accumulateWeighted(frame, avg, 0.005)

    background = cv.convertScaleAbs(avg)

    result = background - frame

    cv.imshow('input', frame)
    cv.imshow('result', result)

    # cv.imwrite("results/result.mp4", result)

    #Check for keypress every frame_delay duration
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv.waitKey(-1) #wait until any key is pressed

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()