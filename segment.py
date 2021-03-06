import cv2 as cv
import numpy as np
from pathlib import Path

def segment(file_path: str, target_path=''):
    # Edit name post processing
    processed_name = Path(file_path).stem +'_processed'

    #default target path if not provided
    if target_path == '':
        target_path = f'{processed_name}.mp4'

    fps = 20
    res = (400, 240)

    #define codec
    fourcc = cv.VideoWriter_fourcc(*'MP4V')
    out = cv.VideoWriter(target_path, fourcc, fps, res)

    cap = cv.VideoCapture(file_path)
    first_iter = True

    while True:
        ret, frame = cap.read()

        #get the background without moving object
        if first_iter:
            avg = np.float32(frame)
            first_iter = False

        cv.accumulateWeighted(frame, avg, 0)

        background = cv.convertScaleAbs(avg)

        #get object  with exclusion
        mask = cv.bitwise_xor(frame, background)

        #get object by subtraccting background from original frame
        segment = cv.absdiff(frame, background)

        #improve result by union of both
        result = cv.bitwise_and(segment, frame)

        # Write result frame to output video
        out.write(result)

        cv.imshow('input', frame)
        cv.imshow('result', result)

        #Check for keypress every frame_delay duration
        key = cv.waitKey(1)
        if key == ord('q'):
            break
        if key == ord('p'):
            cv.waitKey(-1) #wait until any key is pressed

    # When everything done, release the capture
    cap.release()
    out.release()
    cv.destroyAllWindows()

if __name__ == '__main__': segment()