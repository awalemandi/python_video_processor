from sys import argv
import cv2 as cv

def playback(video_file_path: str, fps: int, width: int, height: int, monochrome: bool):

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

#script with input prompt
def playback_input():
    video_source = input('Video source: ')
    fps = input('FPS: ')
    width = input('Video width: ')
    height = input('Video height: ')
    gray = input('Monochrome (y or n): ')
    if gray == 'y' or 'Y':
        monochrome = True
    if gray == 'n' or 'N':
        monochrome = False
    playback(video_source, int(fps), int(width), int(height), monochrome)

def main():
    if len(argv) == 1:
        playback_input()

    if len(argv) >1 and len(argv) != 6:
        print('Usage: python3 -m playback_script.py [video source] [fps] [width] [height] [monochrome]')
        exit()

    else:
        playback(argv[1], int(argv[2]), int(argv[3]), int(argv[4]), eval(argv[5]))

if __name__ == '__main__': main()