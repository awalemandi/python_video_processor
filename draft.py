import cv2 as cv

# video_path, fps, monochrome
capture = cv.VideoCapture('videos/video_1.mp4')

#capture video from webcam
# capture = cv.VideoCapture(0)

#defining fps and delay after each frame
fps=10
frame_delay = int(1000/fps)

# only works for live video source
# def changeRes(width, height):
#     capture.set(3, width)
#     capture.set(4, height)


while True:
    prev_frame = frame[:]
    ret, frame = capture.read()

    #convert each frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # cv.waitKey(frame_delay)

    #show video as stream of grayscale frames
    cv.imshow('Video', gray)


    # if cv.waitKey(frame_delay) & 0xFF == ord('q'):  # press q to quit
    #     break

    key = cv.waitKey(frame_delay)
    if key == ord('q'):
        break
    if key == ord('p'):
        cv.waitKey(-1) #wait until any key is pressed

capture.release()
cv.destroyAllWindows()

#graysclae function
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# resize function
# resized = cv.resize(img, (500, 500))



