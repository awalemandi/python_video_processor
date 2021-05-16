from sys import argv
import cv2 as cv

def playback(video_file_path: str, fps: int, width: int, height: int, monochrome: bool):

    #capture frames from video source
    capture = cv.VideoCapture(video_file_path)

    is_playing = True

    #calculate frame delay based on fps
    frame_delay = int(1000/fps)

    # retrieve the total number of frames
    frame_count = int(capture.get(cv.CAP_PROP_FRAME_COUNT))

    while True:
        if is_playing:
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
        #wait until any key is pressed
        if key == ord('p'):
            is_playing = not is_playing

        # check if 'b' is pressed and rewind video to the previous frame, but do not play
        if key == ord('b') and not is_playing:
            cur_frame_number = capture.get(cv.CAP_PROP_POS_FRAMES)
            
            prev_frame = cur_frame_number
            if (cur_frame_number > 1):
                prev_frame -= 1
            
            capture.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

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