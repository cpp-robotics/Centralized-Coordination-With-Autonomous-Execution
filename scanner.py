import cv2 
import numpy as np

SLICEX = 10
SLICEY = 10
E = 50

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while 1:
        ret, frame = cap.read()
        frame = np.array(frame)
        frame = cv2.flip(frame,1)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) #cv2 shows stuff as BGR, so flip BGR values in the array to RGB 

        #processing
        h,w,_ = frame.shape
        cx = w//2
        cy = h//2
        
        top = cy-SLICEY
        bot = cy+SLICEY
        horz_slice = frame[top:bot:,:]

        left = cx-SLICEX
        right = cx+SLICEX
        vert_slice = frame[:, left:right,:]


        random_pixel_vert = vert_slice[int(np.random.rand()*10), int(np.random.rand()*10), :]

        if np.greater(random_pixel_vert[0], 255-E):
            print('Red detected on vertical')
        if np.greater(random_pixel_vert[1], 255-E):
            print('Green detected on vertical')
        if np.greater(random_pixel_vert[2], 255-E):
            print('Blue detected on vertical')

        random_pixel_horz = horz_slice[int(np.random.rand()*10), int(np.random.rand()*10), :]

        if np.greater(random_pixel_horz[0], 255-E):
            print('Red detected on vertical')
        if np.greater(random_pixel_horz[1], 255-E):
            print('Green detected on vertical')
        if np.greater(random_pixel_horz[2], 255-E):
            print('Blue detected on vertical')

        cv2.imshow('Cam View',  cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        cv2.imshow('Horz Slice', cv2.cvtColor(horz_slice, cv2.COLOR_BGR2RGB))

        cv2.imshow('Vert Slice', cv2.cvtColor(vert_slice, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(10) == ord('q'):
            break
