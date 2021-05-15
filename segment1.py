import cv2 as cv
import numpy as np

file_path = "videos/video_2.mp4"

cap = cv.VideoCapture(file_path)
first_iter = True

while True:
    ret, frame = cap.read()

    if first_iter:
        avg = np.float32(frame)
        first_iter = False

    cv.accumulateWeighted(frame, avg, 0.005)

    background = cv.convertScaleAbs(avg)

    mask = cv.bitwise_xor(frame, background)

    mask2 = cv.bitwise_and(frame, mask)

    mask3 = cv.bitwise_and(frame, mask2)

    result = cv.bitwise_and(frame, mask3)



    cv.imshow("input", frame)
    cv.imshow("mask", mask)
    cv.imshow("result", result)

    #Check for keypress every frame_delay duration
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv.waitKey(-1) #wait until any key is pressed

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()