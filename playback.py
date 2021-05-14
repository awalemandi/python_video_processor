import cv2 as cv

def playback(video_file_path: str, fps: int, monochrome = False):

    # def make_1080p():
    #     capture.set(3, 1920)
    #     capture.set(4, 1080)

    # def make_720p():
    #     capture.set(3, 1280)
    #     capture.set(4, 720)

    # def make_480p():
    #     capture.set(3, 640)
    #     capture.set(4, 480)

    #capture frames from video source
    capture = cv.VideoCapture(video_file_path)

    #calculate frame delay based on fps
    frame_delay = int(1000/fps)

    while True:
        # prev_frame = frame[:]
        ret, frame = capture.read()

        #convert frame to grayscale if monochrome
        if not monochrome:
            cv.imshow('Output', frame)
        else:
            new_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            cv.imshow('Output', new_frame)

        #Check for keypress every frame_delay duration
        key = cv.waitKey(frame_delay)
        if key == ord('q'):
            break
        if key == ord('p'):
            cv.waitKey(-1) #wait until any key is pressed
    
    capture.release()
    cv.destroyAllWindows()

playback('videos/video_2.mp4', 30, True)
