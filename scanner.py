import cv2 
import numpy as np

SLICEX = 10
SLICEY = 10
E = 20

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
        horzslice = frame[top:bot:,:]

        left = cx-SLICEX
        right = cx+SLICEX
        vertslice = frame[:, left:right,:]

        #find color

        sumv = np.zeros((1,3))
        sumh = np.zeros((1,3))
        
        for i in range(h):
            for j in range(SLICEX*2):
                sumv+=vertslice[i,j,:]
        
        for i in range(SLICEY*2):
            for j in range(w):
                sumh+=horzslice[i,j,:]

        average_color_vert = sumv//(h*SLICEX*2)
        average_color_horz = sumh//(w*SLICEY*2)

        if average_color_vert[:,0] > 255-E:
            print('Red detected on vertical')
        elif average_color_vert[:,1] > 255-E:
            print('Green detected on vertical')
        elif average_color_vert[:,2] > 255-E:
            print('Blue Detected on vertical')

        if average_color_horz[:,0] > 255-E:
            print('Red detected on horizontal')
        elif average_color_horz[:,1] > 255-E:
            print('Green detected on horizontal')
        elif average_color_horz[:,2] > 255-E:
            print('Blue Detected on horizontal')

        cv2.imshow('Cam View',  cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        cv2.imshow('Horz Slice', cv2.cvtColor(horzslice, cv2.COLOR_BGR2RGB))

        cv2.imshow('Vert Slice', cv2.cvtColor(vertslice, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(10) == ord('q'):
            break
