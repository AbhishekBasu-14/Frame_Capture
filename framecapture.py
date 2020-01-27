import cv2 
import os 
  
# Read the video from specified path 
cap = cv2.VideoCapture("ArUco_bot.mp4") 
  
try: 
      
    # creating a folder named Generated 
    if not os.path.exists('Generated'): 
        os.makedirs('Generated') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
  
while(True): 
      
    # reading from frame 
    ret,frame = cap.read() 
  
    if ret:

        # if video is still left continue creating images 
        name = './Generated/frame.jpg'
        print ('Creating...' + name + str(currentframe))
        cv2.imwrite(name, frame)
        #total frames is 325, so 6th sec corresponds to 150th frame
        #if currentframe==150:
        #cv2.imwrite(name, frame)

  
        # writing the extracted imaage
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break
  
# Release all space and windows once done 
cap.release() 
cv2.destroyAllWindows() 
