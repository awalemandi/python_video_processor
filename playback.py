import cv2 as cv

# standard resolutions:
# 240p = 352 x 240
# 360 p = 480 x 360
# 480p = 858 x 480
# 720p = 1280 x 720
# 1080p = 1920 x 1080
# 2160p = 3860 x 2160

def playback(video_file_path: str, fps: int, width: int, height: int, monochrome = False):

    #capture frames from video source
    capture = cv.VideoCapture(video_file_path)

    #calculate frame delay based on fps
    frame_delay = int(1000/fps)

    while True:
        ret, frame = capture.read()

        #resize frame to width x height
        resized_frame = cv.resize(frame, (width, height), fx=0, fy=0, interpolation=cv.INTER_CUBIC) 

        #convert frame to grayscale if monochrome
        if not monochrome:
            cv.imshow('Output', resized_frame)
        else:
            new_frame = cv.cvtColor(resized_frame, cv.COLOR_BGR2GRAY)

            cv.imshow('Output', new_frame)

        #Check for keypress every frame_delay duration
        key = cv.waitKey(frame_delay)
        if key == ord('q'):
            break
        if key == ord('p'):
            cv.waitKey(-1) #wait until any key is pressed
    
    capture.release()
    cv.destroyAllWindows()

playback('videos/coffee.mp4', 60, 1920, 1080, False)
